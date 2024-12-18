# クイズを出題

import random
from sound import play_correct, play_wrong, play_count, play_quiz
from keyboard_utils import input_int, input_boolean
from message import animation_correct, animation_wrong
import asyncio
import msvcrt
import keyboard


class Quiz:
    MAX_CHALLENGE = 10  # 入力できる回数
    TARGET_TIME = 3  # カウントダウンする秒数
    FILE_NAME = r'log_data\guest.txt'
    RED = '\033[31m'  # テキストの色（赤）
    CYAN = '\033[36m'  # テキストの色（シアン）
    END = '\033[0m'  # テキストの色（デフォルト）
    DECO = '*' * 70

    def __init__(self, digit: int) -> None:
        self.digit = digit  # 桁数
        self.ans_str = ""  # あてる数字
        self.user_str = ""  # ユーザの解答
        self.count = 1  # カウント回数の初期化
        self.user_cnt = 1  # 入力する桁数(1=百の位)
        self.title = f'                            {self.digit}桁モード'  # タイトル

    # 正解の生成
    def create_ans(self) -> str:
        while True:
            ans_num = random.randint(0, 9)
            # 数字が重複していないか
            if str(ans_num) in self.ans_str:
                continue
            self.ans_str += str(ans_num)
            # 指定した桁数分生成したか
            if len(self.ans_str) == self.digit:
                break
        return self.ans_str

    # ユーザの入力に対してのチェック
    async def input_check(self) -> str:
        while True:
            if keyboard.is_pressed('esc'):
                await self.back_menu()
            # 入力された数字は1つか
            if len(self.user_input) != 1 or not self.user_input.isdigit():
                print('[エラー!!] 数字は1つずつ入力してください')
                continue
            # 数字が重複していないか
            elif self.user_str.count(str(self.user_input)) != 0:
                print('[エラー!!] 同じ数字は使用できません')
                continue
            # ユーザの入力を文字列に変換
            else:
                break
        # return self.user_str_piece

    # ユーザの解答の入力
    async def input_user(self) -> None:
        for _ in range(self.digit):
            self.user_input = await self.async_input(f'{self.user_cnt}つ目の数字を入力してください: ')
            await self.input_check()
            self.user_cnt += 1  # 入力回数のカウントアップ
            self.user_str += str(self.user_input)  # 入力した文字列の結合

    # 非同期で入力を受け付ける
    async def async_input(self, prompt: str) -> int:
        print(prompt, end="", flush=True)
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, input)

    # hit(数字と桁位置の両方が同じ)の回数をカウント
    def hit_count(self) -> int:
        self.hit = 0
        for answer, user in zip(self.ans_str, self.user_str):
            if answer == user:
                self.hit += 1  # hitの回数をカウントアップ
        return self.hit

    # blow(数字のみ同じ)の回数をカウント
    def blow_count(self) -> int:
        self.blow = 0
        for digit in self.user_str:
            if digit in self.ans_str:
                self.blow += 1  # blowの回数をカウントアップ
        self.blow -= self.hit  # hitの回数分を引く
        return self.blow

    # カウントダウン
    async def count_down(self):
        print(' よーい...')
        print('\033[?25l', end='')  # カーソル消去
        for i in range(self.TARGET_TIME, 0, -1):
            print(f'\b\b {i}', end='', flush=True)  # 即表示
            # sleep(1)  # 1秒間スリープ
            await play_count()
        print('\bスタート！')
        print('\033[?25h', end='')  # カーソル表示

    # ファイルに記録（hitとblowの回数）
    def write_file_count(self) -> None:
        with open(self.FILE_NAME, 'a') as f:
            f.write(f'hit: {self.hit} | blow: {self.blow} | your answer is {self.user_str}\n')

    # ファイルに記録（正解）
    def write_file_collect(self) -> None:
        with open(self.FILE_NAME, 'a') as f:
            f.write(f'correct answer in {self.count}\n\n')

    # ファイルに記録（不正解）
    def write_file_fall(self) -> None:
        with open(self.FILE_NAME, 'a') as f:
            f.write("You couldn't answer correctly.\n")
            f.write(f'The correct answer is {self.ans_str}\n\n')

    # 再挑戦するかどうか
    async def retry(self):
        if not input_boolean('もう一度挑戦しますか？'):
            print()
            import main_menu
            await main_menu.execute()
        else:
            self.ans_str = ""
            self.user_cnt = 1
            self.user_str = ""
            await self.main()

    # メニューに戻る
    async def back_menu(self):
        import main_menu
        await main_menu.execute()

    # 判定
    async def main(self):
        print(f'\n{self.DECO}')
        print(self.title)
        print(f'{self.DECO}\n')
        print(f'挑戦できる回数は{self.MAX_CHALLENGE}回です！')
        if not input_boolean('準備は良いですか？'):
            print('また挑戦してね！')
            await asyncio.sleep(0.7)
            print()
            await self.back_menu()
        print('それでは始めます')
        await self.count_down()
        self.create_ans()
        print(f'テスト用: {self.ans_str}')  # 使用する際はコメントアウト
        while self.count <= self.MAX_CHALLENGE:
            print(f'\n------- {self.count}回目の挑戦！！ --------\n')
            await play_quiz()
            await self.input_user()
            print(f'あなたが入力した値: {self.user_str}')
            self.hit = self.hit_count()
            self.blow = self.blow_count()
            self.write_file_count()

            if self.hit == self.digit:
                task1 = asyncio.create_task(animation_correct())
                task2 = asyncio.create_task(play_correct())
                await asyncio.gather(task1, task2)
                print(f'\n{self.RED}正解です!! {self.count}回で当たりました!!{self.END}')
                self.write_file_collect()
                print(f'\n{self.DECO}\n')
                await self.retry()
            else:
                print(f'{self.CYAN}hit: {self.hit} | blow: {self.blow}{self.END}')
                self.count += 1
                self.user_str = ""
                self.user_cnt = 1
        else:
            # 最大回数を超えた場合の処理
            task1 = asyncio.create_task(animation_wrong())
            task2 = asyncio.create_task(play_wrong())
            await asyncio.gather(task1, task2)
            print(f'\n残念! 正解は{self.ans_str}でした。')
            self.write_file_fall()
            print(f'\n{self.DECO}\n')
            await self.retry()


if __name__ == '__main__':
    quiz = Quiz(digit=3)
    asyncio.run(quiz.main())

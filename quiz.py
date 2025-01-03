# クイズを出題
import random
from sound import play_correct, play_wrong, play_count, play_quiz
from keyboard_utils import input_boolean
from message import animation_correct, animation_wrong
import asyncio
import file_utils
from datetime import datetime


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
        self.clear = False
        self.log = []  # ログ

    def create_ans(self) -> str:
        """ 正解の生成をするメソッド """
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

    async def input_check(self, input_data: str) -> None:
        """ 入力された値に対してのチェックをするメソッド """
        if len(input_data) != self.digit:
            raise Exception('[エラー!!] 3桁で入力してください')
        # 入力された数字が重複されていないか確認
        if len(set(input_data)) != self.digit:
            raise Exception('[エラー!!] 重複しない数字を使用してください')

    async def input_user(self) -> None:
        """ ユーザの解答の入力を求めるメソッド """
        while True:
            # ユーザーの入力を取得
            input_int = await self.async_input("回答を入力してください: ")
            try:
                await self.input_check(input_int)
                break
            except Exception as e:
                print(e)
                continue
        self.user_str = str(input_int)

    async def async_input(self, prompt: str) -> str:
        """ 非同期で入力を受け付けるメソッド """
        print(prompt, end="", flush=True)
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, input)

    def hit_count(self) -> int:
        """ hit(数字と桁位置の両方が同じ)の回数をカウントするメソッド """
        self.hit = 0
        for answer, user in zip(self.ans_str, self.user_str):
            if answer == user:
                self.hit += 1  # hitの回数をカウントアップ
        return self.hit

    def blow_count(self) -> int:
        """ blow(数字のみ同じ)の回数をカウントするメソッド """
        self.blow = 0
        for digit in self.user_str:
            if digit in self.ans_str:
                self.blow += 1  # blowの回数をカウントアップ
        self.blow -= self.hit  # hitの回数分を引く
        return self.blow

    async def count_down(self):
        """ カウントダウンをするメソッド """
        print(' よーい...')
        print('\033[?25l', end='')  # カーソル消去
        for i in range(self.TARGET_TIME, 0, -1):
            print(f'\b\b {i}', end='', flush=True)  # 即表示
            # sleep(1)  # 1秒間スリープ
            await play_count()
        print('\bスタート！')
        print('\033[?25h', end='')  # カーソル表示

    def append_log(self) -> None:
        """ ファイルに記録(hitとblowの回数)するメソッド """
        log_data = {"input": self.user_str, "hit": self.hit, "blow": self.blow}
        self.log.append(log_data)

    def write_log(self) -> None:
        """ ファイルに記録をするメソッド """
        log = {}
        log["datetime"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log["answer"] = int(self.ans_str)
        log["clear"] = self.clear
        log["log"] = self.log
        file_utils.add_log(log)

    async def retry(self):
        """" 再挑戦するかどうかの入力を求めるメソッド """
        if not input_boolean('もう一度挑戦しますか？'):
            print()
            await self.back_menu()
        else:
            self.ans_str = ""
            self.user_cnt = 1
            self.user_str = ""
            await self.main()

    async def back_menu(self):
        """ メニューに戻るメソッド """
        import main_menu
        await main_menu.execute()

    async def main(self):
        """ メインの関数 """
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
            self.append_log()

            if self.hit == self.digit:
                task1 = asyncio.create_task(animation_correct())
                task2 = asyncio.create_task(play_correct())
                await asyncio.gather(task1, task2)
                print(f'\n{self.RED}正解です!! {self.count}回で当たりました!!{self.END}')
                print(f'\n{self.DECO}\n')
                self.clear = True
                self.write_log()
                await self.retry()
            else:
                print(
                    f'{self.CYAN}hit: {self.hit} | blow: {self.blow}{self.END}'
                    )
                self.count += 1
                self.user_str = ""
                self.user_cnt = 1
        else:
            # 最大回数を超えた場合の処理
            task1 = asyncio.create_task(animation_wrong())
            task2 = asyncio.create_task(play_wrong())
            await asyncio.gather(task1, task2)
            print(f'\n残念! 正解は{self.ans_str}でした。')
            print(f'\n{self.DECO}\n')
            self.write_log()
            await self.retry()


if __name__ == '__main__':
    quiz = Quiz(digit=3)
    asyncio.run(quiz.main())

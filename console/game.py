"""
ゲームのメイン処理をします
"""
import asyncio

from console.sound import play
from console.message import show_message_with_sound
from utils.keyboard_utils import input_boolean
from logic.game_logic import QuizLogic

# 使用する音声ファイル
sound_files = {
    'challenge_count': 'challenge.mp3',
    'count_down': 'count.mp3',
    'correct': 'happy.mp3',
    'wrong': 'sad.mp3'
}

message_files = {
    'correct': 'correct_message.txt',
    'wrong': 'wrong_message.txt'
}


class QuizGame:
    TARGET_TIME = 3  # カウントダウンの秒数
    RED = '\033[31m'  # テキストの色（赤）
    CYAN = '\033[36m'  # テキストの色（シアン）
    END = '\033[0m'  # テキストの色（デフォルト）
    DECO = '*' * 70

    def __init__(self, digit: int, max_challenge: int) -> None:
        self.quiz = QuizLogic(digit, max_challenge)
        self.title = f'{digit}桁モード'.center(65)

    async def input_user(self) -> None:
        """ ユーザの解答の入力を求める """
        while True:
            input_str = await self.async_input("回答を入力してください: ")
            check_result = self.quiz.input_check(input_str)

            if check_result == 'ok':
                self.quiz.user_str = input_str
                break
            else:
                print(check_result)
                continue

    async def async_input(self, prompt: str) -> str:
        """非同期で入力を受け付ける

        Args:
            prompt (str): 入力時に表示するメッセージ

        Returns:
            str: 入力された文字列
        """
        print(prompt, end="", flush=True)
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, input)

    async def count_down(self):
        """ カウントダウンをする """
        print(' よーい...')
        print('\033[?25l', end='')  # カーソル消去
        for i in range(self.TARGET_TIME, 0, -1):
            print(f'\b\b {i}', end='', flush=True)
            await play(sound_files['count_down'])
        print('\bスタート！')
        print('\033[?25h', end='')  # カーソル表示

    async def retry(self):
        """再挑戦するかどうかの入力を求める"""
        if not input_boolean('もう一度挑戦しますか？'):
            self.quiz.exit = True
            return
        self.quiz.__init__(self.quiz.digit, self.quiz.max_challenge)
        await self.main()

    async def main(self):
        """ メインの関数 """
        print(f'\n{self.DECO}')
        print(self.title)
        print(f'{self.DECO}\n')
        print(f'挑戦できる回数は{self.quiz.max_challenge}回です！')

        if not input_boolean('準備は良いですか？'):
            print('また挑戦してね！')
            await asyncio.sleep(0.7)
            return

        print('それでは始めます')
        await self.count_down()
        self.quiz.create_ans()
        print(f'テスト用: {self.quiz.ans_str}')  # デバッグ用

        while self.quiz.count <= self.quiz.max_challenge:
            print(f'\n------- {self.quiz.count}回目の挑戦！！ --------\n')
            await play(sound_files['challenge_count'])
            await self.input_user()
            print(f'あなたが入力した値: {self.quiz.user_str}')

            self.quiz.append_log()

            if self.quiz.hit_count() == self.quiz.digit:
                await show_message_with_sound(
                    message_files['correct'], sound_files['correct'])
                print(f'\n{self.RED}正解です!! {self.quiz.count}回で当たりました!!{self.END}')
                self.quiz.clear = True
                self.quiz.write_log()
                await self.retry()
                if self.quiz.exit:
                    return
            else:
                print(f'{self.CYAN}hit: {self.quiz.hit_count()} | blow: {self.quiz.blow_count()}{self.END}')
                self.quiz.count += 1

        await show_message_with_sound(message_files['wrong'], sound_files['wrong'])
        print(f'\n残念! 正解は{self.quiz.ans_str}でした。')
        self.quiz.write_log()
        await self.retry()
        if self.quiz.exit:
            return


if __name__ == '__main__':
    quiz = QuizGame(digit=3, max_challenge=10)
    asyncio.run(quiz.main())

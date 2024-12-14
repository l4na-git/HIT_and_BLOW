# クイズを出題

import random
import sound
import main_menu
from keyboard import input_int, input_boolean
from time import sleep


class Quiz:
    MAX_CHALLENGE = 10  # 入力できる回数
    TARGET_TIME = 3  # カウントダウンする秒数
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
            if len(self.ans_str) == self.digit:
                break
        return self.ans_str

    # ユーザの入力に対してのチェック
    def input_check(self) -> str:
        while True:
            user_int = input_int(f'{self.user_cnt}つ目の数字を入力してください: ')
            # 入力範囲のチェック
            if user_int >= 10:  # 入力値が範囲外の時は入力しなおし
                print('エラー!! 0～9の範囲で入力してください')
                continue
            # 数字が重複していないかチェック
            elif self.user_str.count(str(user_int)) != 0:
                print('エラー!! 同じ数字は使用できません')
                continue
            # ユーザの入力を文字列に変換
            else:
                self.user_str_piece = str(user_int)
                break
        return self.user_str_piece

    # ユーザの解答の入力
    def input_user(self) -> None:
        for _ in range(self.digit):
            self.input_check()
            self.user_cnt += 1  # 入力回数のカウントアップ
            self.user_str += self.user_str_piece  # 入力した文字列の結合

    # hitの回数をカウント
    def hit_count(self) -> int:
        self.hit = 0  # 数値と桁位置の両方が同じ
        for answer, user in zip(self.ans_str, self.user_str):
            if answer == user:
                self.hit += 1  # hitの回数をカウントアップ
        return self.hit

    # blowの回数をカウント
    def blow_count(self) -> int:
        self.blow = 0  # 数値のみ同じ
        # blowの判定
        for digit in self.user_str:
            if digit in self.ans_str:
                self.blow += 1  # blowの回数をカウントアップ
        self.blow -= self.hit  # hitの回数分を引く
        return self.blow

    # カウントダウン
    def count_down(self):
        print(' よーい...')
        print('\033[?25l', end='')  # カーソル消去
        for i in range(self.TARGET_TIME, 0, -1):
            print(f'\b\b {i}', end='', flush=True)  # 即表示
            sleep(1)  # 1秒間スリープ
        print('\bスタート！')
        print('\033[?25h', end='')  # カーソル表示

    # 判定
    def main(self):
        print(f'\n{self.DECO}')
        print(self.title)
        print(f'{self.DECO}\n')
        print(f'挑戦できる回数は{self.MAX_CHALLENGE}回です！')
        if not input_boolean('準備は良いですか？'):
            print('また挑戦してね！\n')
            main_menu.execute()
        print('それでは始めます')
        self.count_down()
        self.create_ans()
        print(f'テスト用: {self.ans_str}')  # 使用する際はコメントアウト
        while self.count <= self.MAX_CHALLENGE:
            print(f'\n------- {self.count}回目の挑戦！！ --------\n')
            self.input_user()
            print(f'あなたが入力した値: {self.user_str}')
            self.hit = self.hit_count()
            self.blow = self.blow_count()

            if self.hit == self.digit:
                print(f'{self.RED}正解!! {self.count}回で当たりました!!{self.END}')
                sound.play_correct()
                print(f'\n{self.DECO}\n')
                break
            else:
                print(f'{self.CYAN}hit: {self.hit} | blow: {self.blow}{self.END}')
                self.count += 1
                self.user_str = ""
                self.user_cnt = 1
        else:
            # 最大回数を超えた場合の処理
            print(f'残念! 正解は{self.ans_str}でした。')
            sound.play_wrong
            print(f'\n{self.DECO}\n')


if __name__ == '__main__':
    quiz = Quiz(digit=3)
    quiz.main()

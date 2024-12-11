# クイズを出題

import random
from keyboard import input_int


class Quiz:
    MAX_CHALLENGE = 20  # 入力できる回数
    RED = '\033[31m'  # テキストの色（赤）
    CYAN = '\033[36m'  # テキストの色（シアン）
    END = '\033[0m'  # テキストの色（デフォルト）

    def __init__(self, digit: int) -> None:
        self.digit = digit  # 桁数
        self.ans_str = ""  # あてる数字
        self.user_str = ""  # ユーザの解答
        self.count = 1  # カウント回数の初期化
        self.user_cnt = 1  # 入力する桁数(1=百の位)

    # 正解の生成
    def create_ans(self) -> None:
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
        self.user_str_piece = ""
        while True:
            user_int = input_int(f'{self.count}回目 {self.user_cnt}つ目の数字を入力してください: ')
            # 入力範囲のチェック
            if user_int >= 10:  # 入力値が範囲外の時は入力しなおし
                print('エラー!! 0～9の範囲で入力してください')
                continue
            elif self.user_str.count(str(user_int)) != 0:
                print('エラー!! 同じ数字は使用できません')
                continue
            else:
                # ユーザの入力を3桁の文字列に変換
                self.user_str_piece = str(user_int)
                break
        return self.user_str_piece

    # ユーザの解答の入力
    def input_user(self) -> None:
        for _ in range(self.digit):
            self.input_check()
            self.user_cnt += 1
            self.user_str += self.user_str_piece

    # hitの回数をカウント
    def hit_count(self) -> int:
        self.hit = 0  # 数値と桁位置の両方が同じ
        for answer, user in zip(self.ans_str, self.user_str):
            if answer == user:
                self.hit += 1
        return self.hit

    # blowの回数をカウント
    def blow_count(self) -> int:
        self.blow = 0  # 数値のみ同じ
        # blowの判定
        for digit in self.user_str:
            if digit in self.ans_str:
                self.blow += 1
        self.blow -= self.hit  # hit分を引く
        return self.blow

    # 判定
    def main(self):
        print(f'*** {self.digit}桁モード ***')
        self.create_ans()
        print(f'テスト用: {self.ans_str}')  # 使用する際はコメントアウト
        while self.count <= self.MAX_CHALLENGE:
            self.input_user()
            print(f'あなたが入力した値: {self.user_str}')
            self.hit = self.hit_count()
            self.blow = self.blow_count()

            if self.hit == self.digit:
                print(f'{self.RED}正解!! {self.count}回で当たりました!!{self.END}')
                break
            else:
                print(f'{self.CYAN}hit: {self.hit} | blow: {self.blow}{self.END}')
                self.count += 1
                self.user_str = ""
                self.user_cnt = 1
        else:
            # 最大回数を超えた場合の処理
            print(f'残念! 正解は{self.ans_str}でした。')


if __name__ == '__main__':
    quiz = Quiz(digit=3)
    quiz.main()

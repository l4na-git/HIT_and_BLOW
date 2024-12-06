# クイズを出題

import random
from keybord import input_int


class Quiz:
    def __init__(self, digit, max_num) -> None:
        self.digit = digit  # 桁数
        self.max_num = max_num  # 入力可能な最大値
        self.max_charenge = 20  # 入力できる回数
        self.ans_str = f'{random.randint(0, self.max_num):0{digit}}'  # 当てる数値
        self.count = 1  # カウント回数の初期化
        self.color_red = '\033[31m'  # テキストの色（赤）
        self.color_cyan = '\033[36m'  # テキストの色（シアン）
        self.color_end = '\033[0m'  # テキストの色（デフォルト）

    # ユーザの解答の入力
    def input_user(self):
        while True:
            user_int = input_int(f'{self.count}回目 数値を入力してください: ')
            # 入力範囲のチェック
            if user_int < 0 or user_int > self.max_num:  # 入力値が範囲外の時は入力しなおし
                print(f'エラー!! {'0' * self.digit}～{self.max_num}の範囲で入力してください')
                continue
            else:
                # ユーザの入力を3桁の文字列に変換
                self.user_str = f'{user_int:0{self.digit}}'
                break

    # hitの回数をカウント
    def hit_count(self):
        self.hit = 0  # 数値と桁位置の両方が同じ
        for i, (answer, user) in enumerate(zip(self.ans_str, self.user_str)):
            if answer == user:
                self.hit += 1
        return self.hit

    # blowの回数をカウント
    def blow_count(self):
        self.blow = 0  # 数値のみ同じ
        # blowの判定
        for digit in self.user_str:
            if digit in self.ans_str:
                self.blow += 1
        self.blow -= self.hit  # hit分を引く
        return self.blow

    # 判定
    def quiz(self):
        while self.count <= self.max_charenge:
            self.user = self.input_user()
            self.hit = self.hit_count()
            self.blow = self.blow_count()

            if self.hit == self.digit:
                print(f'{self.color_red}正解!! {self.count}回で当たりました!!{self.color_end}')
                break
            else:
                print(f'{self.color_cyan}hit: {self.hit} | blow: {self.blow}{self.color_end}')
                self.count += 1
        else:
            # 最大回数を超えた場合の処理
            print(f'残念! 正解は{self.ans_str}でした。')


if __name__ == '__main__':
    quiz = Quiz(digit=3, max_num=999)
    ans = quiz.ans_str
    print(f'テスト用: 正解は{ans}')
    quiz.quiz()

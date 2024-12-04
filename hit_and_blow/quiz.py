# 問題

import random


class Quiz:
    def __init__(self, digit, max_num) -> None:
        self.digit = digit
        self.max_num = max_num  # 入力可能な最大値
        self.max_charenge = 20  # 入力できる回数
        self.ans_str = f'{random.randint(0, self.max_num):0{digit}}'  # 当てる数値
        self.count = 1  # カウント回数の初期化

    # 処理
    def quiz(self):
        while self.count <= self.max_charenge:
            # 入力
            try:
                print(f'{self.count}回目 数値を入力してください: ', end='')
                user_int = int(input())
            except ValueError:
                print('エラー!! 数値を入力してください')
                continue

            # 入力範囲のチェック
            if user_int < 0 or user_int > self.max_num:  # 入力値が範囲外の時は入力しなおし
                print(f'エラー!! {'0' * self.digit}～{self.max_num}の範囲で入力してください')
                continue

            # hitとblowの判定
            hit = 0  # 数値と桁位置の両方が同じ
            blow = 0  # 数値のみ同じ

            # ユーザの入力を3桁の文字列に変換
            user_str = f'{user_int:0{self.digit}}'

            # hitの判定
            for i, (answer, user) in enumerate(zip(self.ans_str, user_str)):
                if answer == user:
                    hit += 1
            # blowの判定
            for digit in user_str:
                if digit in self.ans_str:
                    blow += 1
            blow -= hit  # hit分を引く

            if hit == self.digit:
                print(f'\033[31m正解!! {self.count}回で当たりました!!\033[0m')
                break
            else:
                print(f'\033[34mhit: {hit} | blow: {blow}\033[0m')
                self.count += 1
        else:
            # 最大回数を超えた場合の処理
            print(f'残念! 正解は{self.ans_str}でした。')


if __name__ == '__main__':
    quiz1 = Quiz(digit=3, max_num=999)
    digit = quiz1.digit
    ans = quiz1.ans_str
    print(digit)
    print(f'テスト用: 正解は{ans}')
    quiz1.quiz()

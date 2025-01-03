# ゲームの説明
from keyboard_utils import input_is_q


# 定数の定義
DECO = '*' * 70
DECO_CUT = '-' * 70
TITLE = '                            遊び方'
HOW_TO = """
1. コンピュータがランダムな数字を生成します。
    例: 3桁の数字 (000～999) または 4桁の数字 (0000～9999)
2. その数字を予想して入力してください。
    [注意!!] 同じ数字は使用できません。
3. 予想がどの程度あっているかが表示されます。
    Hit → 数字も場所も同じ
    Blow → 数字は同じだが場所は違う
4. これを繰り返します。
5. 結果が表示されます。
"""


def print_info():
    """ ゲームの遊び方を表示する関数 """
    print(f'\n{DECO}')
    print(TITLE)
    print(DECO)
    print(HOW_TO)
    print(f'{DECO_CUT}\n')


def main():
    """ メインの関数 """
    print_info()
    input_is_q()  # ユーザがqを押すまで待機
    print(f'\n{DECO}\n')


if __name__ == '__main__':
    main()

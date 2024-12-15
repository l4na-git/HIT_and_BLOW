# ゲームの説明
from keyboard import input_is_q

DECO = '*' * 70
TITLE = '                            遊び方'
HOW_TO = """
1. コンピュータがランダムな数字を生成します。
    例: 3桁の数字 (000～999) または 4桁の数字 (0000～9999)
2. その数字を予想して入力してください。
    [注意！]同じ数字は使用できません。
3. 予想がどの程度あっているかが表示されます。
    Hit → 数字も場所も同じ
    Blow → 数字は同じだが場所は違う
4. これを繰り返します。
5. 結果が表示されます。
"""


# メイン関数
def main():
    print(f'\n{DECO}')
    print(f'{TITLE}')
    print(f'{DECO}')
    print(HOW_TO)
    input_is_q()
    print(f'\n{DECO}\n')


if __name__ == '__main__':
    main()

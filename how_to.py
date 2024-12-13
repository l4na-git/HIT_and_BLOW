# ゲームの説明

def how_to():
    info = """
**********************************************************************
                                遊び方
**********************************************************************

1. コンピュータがランダムな数字を生成します。
    例: 3桁の数字 (000～999) または 4桁の数字 (0000～9999)
2. その数字を予想して入力してください。
3. 予想がどの程度あっているかが表示されます。
    Hit → 数字も場所も同じ
    Blow → 数字は同じだが場所は違う
4. これを繰り返します。
5. 結果が表示されます。

**********************************************************************
"""
    print(info)


if __name__ == '__main__':
    how_to()

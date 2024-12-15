# キーボードから入力された値に対しての処理


# キーボードから整数を入力して返す
def input_int(prompt) -> int:
    while True:
        num = input(prompt)
        if num.isdigit():  # 整数に変換できるかどうか
            break
        else:
            print('[エラー!!] 整数で入力してください')

    return int(num)


# キーボードからyまたはnを入力して返す
# True:yが入力された場合 False:nが入力された場合
def input_boolean(prompt):
    while True:
        str = input(f'{prompt} (y/n): ')
        if str.lower() == 'y' or str.lower() == 'ｙ':
            return True
        elif str.lower() == 'n' or str.lower() == 'ｎ':
            return False

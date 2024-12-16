# キーボードから入力された値に対しての処理


# キーボードから整数を入力して返す
def input_int(prompt: str) -> int:
    while True:
        num = input(prompt)
        if num.isdigit():
            break
        else:
            print('[エラー!!] 整数で入力してください')

    return int(num)


# キーボードからyまたはnを入力して返す
# True:yが入力された場合 False:nが入力された場合
def input_boolean(prompt: str) -> bool:
    while True:
        str = input(f'{prompt} (y/n): ')
        if str.lower() == 'y' or str.lower() == 'ｙ':
            return True
        elif str.lower() == 'n' or str.lower() == 'ｎ':
            return False


# キーボードからQを入力して返す
# True:Qが入力された場合
def input_is_q() -> bool:
    while True:
        str = input('戻るには"Q"を押してください: ')
        if (str.lower() == 'q' or str.lower() == 'Q' or
                str.lower() == 'ｑ' or str.lower() == 'Ｑ'):
            return True
        else:
            print('[エラー!!] 指定されたキーを入力してください')

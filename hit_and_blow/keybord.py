# キーボードから入力された値に対しての処理


# キーボードから整数を入力して返す
def input_int(prompt) -> int:
    while True:
        num = input(prompt)
        if num.isdigit():  # 整数に変換できるかどうか
            break
        else:
            print('エラー!! 整数で入力してください')

    return int(num)

# キーボードから入力された値に対しての処理

# キーボードから整数を入力して返す
# 整数以外が入力された場合は再入力させる
def input_int(prompt: str) -> int:
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            break
        else:
            print('[エラー!!] 整数で入力してください')

    return int(user_input)


# キーボードからyまたはnを入力して返す
# True:yが入力された場合 False:nが入力された場合
def input_boolean(prompt: str) -> bool:
    y_inputs = ['y', 'ｙ']
    n_inputs = ['n', 'ｎ']
    while True:
        user_input = input(f'{prompt} (y/n): ').lower()
        if user_input in y_inputs:
            return True
        elif user_input in n_inputs:
            return False
        print('[エラー!!] "y" または "n" を入力してください')


# キーボードからQを入力して返す
# True:Qが入力された場合
def input_is_q() -> bool:
    q_inputs = ['q', 'ｑ']
    while True:
        user_input = input('戻るには"Q"を押してください: ').lower()
        if user_input in q_inputs:
            return True
        else:
            print('[エラー!!] 指定されたキーを入力してください')


# キーボードから音量を入力して返す
def input_volume(prompt):
    while True:
        input_volume = input_int(prompt)
        if input_volume > 100:
            print('数字は100以下で入力してください')
            continue
        return input_volume

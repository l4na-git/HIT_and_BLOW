# キーボードから入力された値に対しての処理

def input_int(prompt: str) -> int:
    """ キーボードから整数を入力して返す """
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            break
        else:
            print('[エラー!!] 整数で入力してください')

    return int(user_input)


def input_boolean(prompt: str) -> bool:
    """ キーボードからyまたはnを入力して返す """
    y_inputs = ['y', 'ｙ']
    n_inputs = ['n', 'ｎ']
    while True:
        user_input = input(f'{prompt} (y/n): ').lower()
        if user_input in y_inputs:
            return True
        elif user_input in n_inputs:
            return False
        print('[エラー!!] "y" または "n" を入力してください')


def input_is_q() -> bool:
    """ キーボードからQを入力して返す関数 """
    q_inputs = ['q', 'ｑ']
    while True:
        user_input = input('戻るには"Q"を押してください: ').lower()
        if user_input in q_inputs:
            return True
        else:
            print('[エラー!!] 指定されたキーを入力してください')


def input_volume(prompt) -> int:
    """ キーボードから音量を入力して返す関数 """
    while True:
        input_volume = input_int(prompt)
        if input_volume > 100:
            print('数字は100以下で入力してください')
            continue
        return input_volume

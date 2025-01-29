"""
キーボードから入力された値に対しての処理をします
"""


def input_int(prompt: str) -> int:
    """キーボードから整数を入力して返す

    Args:
        prompt (str): 入力時に表示するメッセージ

    Returns:
        int: 入力された整数
    """
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print('[エラー!!] 整数で入力してください')


def input_isalnum_ascii(prompt: str) -> str:
    """キーボードから英数字(ASCII)を入力して返す

    Args:
        prompt (str): 入力時に表示するメッセージ

    Returns:
        str: 入力された英数字
    """
    while True:
        user_input = input(prompt).strip()
        if user_input.isalnum() and user_input.isascii():
            return user_input
        else:
            print('[エラー!!] 英数字で入力してください')


def input_boolean(prompt: str) -> bool:
    """キーボードからyまたはnを入力して返す

    Args:
        prompt (str): 入力時に表示するメッセージ

    Returns:
        bool: 入力された値がyの場合はTrue、nの場合はFalse
    """
    y_inputs = ['y', 'ｙ']
    n_inputs = ['n', 'ｎ']
    while True:
        user_input = input(f'{prompt} (y/n): ').lower()
        if user_input in y_inputs:
            return True
        elif user_input in n_inputs:
            return False
        print('[エラー!!] "y" または "n" を入力してください')


def input_exit_prompt(prompt: str) -> bool:
    """キーボードからQを入力して返す

    Args:
        prompt (str): 入力時に表示するメッセージ

    Returns:
        bool: 入力された値がQの場合はTrue
    """
    q_inputs = ['q', 'ｑ']
    while True:
        user_input = input(prompt).lower()
        if user_input in q_inputs:
            return True
        else:
            print('[エラー!!] 指定されたキーを入力してください')


def input_volume(prompt: str) -> int:
    """キーボードから音量を入力して返す

    Args:
        prompt (str): 入力時に表示するメッセージ

    Returns:
        int: 入力された音量
    """
    while True:
        input_volume = input_int(prompt)
        if input_volume > 100:
            print('数字は100以下で入力してください')
            continue
        return input_volume

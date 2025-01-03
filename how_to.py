# ゲームの説明
from keyboard_utils import input_is_q
from file_utils import read_all_file


# 定数の定義
DECO = '*' * 70
DECO_CUT = '-' * 70
TITLE = '                            遊び方'


def print_how_to():
    """ ゲームの遊び方を表示する関数 """
    line_data = read_all_file(r'\conf\how_to.txt')
    for line in line_data:
        print(line, end='')
    print()


def print_info():
    """ タイトルとゲームの遊び方を表示する関数 """
    print(f'\n{DECO}')
    print(TITLE)
    print(DECO)
    print_how_to()
    print(f'{DECO_CUT}\n')


def main():
    """ メインの関数 """
    print_info()
    input_is_q()  # ユーザがqを押すまで待機
    print(f'\n{DECO}\n')


if __name__ == '__main__':
    main()

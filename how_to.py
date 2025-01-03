# ゲームの説明
from keyboard_utils import input_is_q
from file_utils import read_all_file
from time import sleep


# 定数の定義
DECO = '*' * 70
DECO_CUT = '-' * 70
TITLE = '                            遊び方'
SLEEP_TIME_ONE = 0.1
SLEEP_TIME_LINE = 0.4


def print_how_to():
    """ ゲームの遊び方を表示する関数 """
    line_data = read_all_file(r'\conf\how_to.txt')
    for line in line_data:
        sleep(SLEEP_TIME_LINE)
        for _, text in enumerate(line):
            print(text, end='', flush=True)
            sleep(SLEEP_TIME_ONE)
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

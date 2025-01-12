# ゲームの説明
from utils.keyboard_utils import input_is_q
from utils.file_utils import read_all_file
from console.sound import print_with_sound
from time import sleep
import os


# 定数の定義
DECO = '*' * 70
DECO_CUT = '-' * 70
TITLE = '                            遊び方'
SLEEP_TIME = 0.3
CONF_FILE_PATH = os.path.join(
    os.path.dirname(__file__), '../config', 'how_to.txt')


def print_how_to():
    """ ゲームの遊び方を表示する関数 """
    line_data = read_all_file(CONF_FILE_PATH)
    print('\033[?25l', end='')  # カーソル消去
    for line in line_data:
        sleep(SLEEP_TIME)
        print_with_sound(line)
        print()
    print('\033[?25h', end='')  # カーソル表示


def main():
    """ メインの関数 """
    print(f'\n{DECO}')
    print(TITLE)
    print(DECO)
    print_how_to()
    print(f'{DECO_CUT}\n')
    input_is_q()  # ユーザがqを押すまで待機
    print(f'\n{DECO}\n')


if __name__ == '__main__':
    main()

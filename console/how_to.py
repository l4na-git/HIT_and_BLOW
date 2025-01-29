"""
ゲームの遊び方を表示する
"""
from time import sleep
from pathlib import Path

from utils.file_utils import read_file
from utils.keyboard_utils import input_exit_prompt
from console.sound import print_with_sound


# 定数の定義
DECO = '*' * 70
DECO_CUT = '-' * 70
TITLE = '                            遊び方'
SLEEP_TIME = 0.3
CONF_FILE_PATH = Path('config/how_to.txt').resolve()


def show_how_to():
    """ゲームの遊び方を表示する"""
    line_data = read_file(CONF_FILE_PATH)
    hide_cursor()
    for line in line_data:
        sleep(SLEEP_TIME)
        print_with_sound(line)
    show_cursor()


def hide_cursor() -> None:
    """カーソルを非表示にする"""
    print('\033[?25l', end='')


def show_cursor() -> None:
    """カーソルを再表示する"""
    print('\033[?25h', end='')


def main():
    """タイトル、ゲームの遊び方、終了方法を表示する"""
    print(f'\n{DECO}')
    print(TITLE)
    print(DECO)
    print()
    show_how_to()
    print()
    print(f'{DECO_CUT}\n')
    input_exit_prompt('戻るには"Q"を押してください: ')
    print(f'\n{DECO}\n')


if __name__ == '__main__':
    main()

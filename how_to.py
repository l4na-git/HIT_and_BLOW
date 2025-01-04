# ゲームの説明
from keyboard_utils import input_is_q
from file_utils import read_all_file
from sound import play_keyboard
from time import sleep
import asyncio
import pygame


# 定数の定義
DECO = '*' * 70
DECO_CUT = '-' * 70
TITLE = '                            遊び方'
SLEEP_TIME_ONE = 0.1
SLEEP_TIME_LINE = 0.4


async def print_how_to(event: asyncio.Event):
    """ ゲームの遊び方を表示する関数 """
    line_data = read_all_file(r'\conf\how_to.txt')
    print('\033[?25l', end='')  # カーソル消去
    for line in line_data:
        sleep(SLEEP_TIME_LINE)
        for _, text in enumerate(line):
            print(text, end='', flush=True)
            await asyncio.sleep(SLEEP_TIME_ONE)
        print()
    print('\033[?25h', end='')  # カーソル表示
    event.set()


async def print_wait_play(event: asyncio.Event):
    """ 表示が終わるまで音を鳴らし続ける関数 """
    while not event.is_set():
        await play_keyboard()
    pygame.mixer.music.stop()  # 音声を即終了させる


async def print_info():
    """ タイトルとゲームの遊び方を表示する関数 """
    print(f'\n{DECO}')
    print(TITLE)
    print(DECO)
    event = asyncio.Event()
    await asyncio.gather(print_how_to(event), print_wait_play(event))
    print(f'{DECO_CUT}\n')


async def main():
    """ メインの関数 """
    await print_info()
    input_is_q()  # ユーザがqを押すまで待機
    print(f'\n{DECO}\n')


if __name__ == '__main__':
    asyncio.run(main())

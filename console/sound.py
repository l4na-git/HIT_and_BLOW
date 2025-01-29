"""
音量に関する処理を行います
"""
import sys
import os
import asyncio
from time import sleep
from pathlib import Path

import pygame

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import utils.keyboard_utils as keyboard
from utils.file_utils import change_volume, read_json_file

# 定数の定義
CONF_FILE_PATH = Path('config/setting.json').resolve()

DEFAULT_VOLUME = 0.3
DECO = '*' * 70
TITLE = '音量の設定'
SLEEP_TIME = 0.7
WEIGHT_TIME = 0.05
DELAY = 0.1


async def play(filename: str) -> None:
    """音を再生する

    Args:
        filename (str): 再生する音声ファイル名
    """
    pygame.mixer.init()
    data_list = read_json_file(CONF_FILE_PATH)
    volume = data_list['sound']
    pygame.mixer.music.set_volume(volume)
    sound_file = Path('audio/' + filename).resolve()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        await asyncio.sleep(WEIGHT_TIME)


def volume() -> None:
    """ 音量の調整をする関数 """
    print(f'\n{DECO}')
    print(TITLE.center(65))
    print(f'{DECO}\n')
    print_with_sound('音量を設定できます(0～100)')
    print_with_sound('[注意！] パソコンでミュートになっている場合は音がなりません。\n')

    pygame.mixer.init()
    data_list = read_json_file(CONF_FILE_PATH)
    volume = data_list['sound'] * 100
    print_with_sound(f'現在の音量は{volume:.0f}%です')
    sleep(SLEEP_TIME)

    set_volume = keyboard.input_volume('音量を入力: ')
    change_volume(CONF_FILE_PATH, set_volume / 100)
    print_with_sound(f'\n音量を{set_volume}%に設定しました')
    sleep(SLEEP_TIME)
    print(f'\n{DECO}\n')


def print_with_sound(prompt: str) -> None:
    """一文字ずつ表示しながら音を再生する

    Args:
        prompt (str): 表示する文字列
    """
    PATH = Path('audio/keyboard.mp3').resolve()
    pygame.mixer.init()
    data_list = read_json_file(CONF_FILE_PATH)
    volume = data_list['sound']
    pygame.mixer.music.set_volume(volume)

    pygame.mixer.music.load(PATH)
    pygame.mixer.music.play(loops=-1)

    for char in prompt:
        sys.stdout.write(char)
        sys.stdout.flush()
        sleep(DELAY)

    pygame.mixer.music.stop()
    print()


if __name__ == "__main__":
    change_volume(CONF_FILE_PATH, 0.3)
    volume()

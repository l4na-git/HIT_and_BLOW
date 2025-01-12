# 音量に関するもの
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import utils.keyboard_utils as keyboard
from utils.file_utils import search_file, change_volume, read_log
import pygame
import os
import asyncio
from time import sleep


# 定数の定義
CONF_FILE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                r'..\config\setting.json'))

DEFAULT_VOLUME = 0.3
DECO = '*' * 70
TITLE = '                           音量の設定'
SLEEP_TIME = 0.7


def create_file_path(filename: str) -> str:
    """ ファイルパスを作成する関数 """
    return os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        r'..\audio\\' + filename))


async def play(filename):
    """ 音を再生する関数 """
    pygame.mixer.init()
    data_list = read_log(CONF_FILE_PATH)
    volume = data_list['sound']
    pygame.mixer.music.set_volume(volume)  # 音量を設定
    sound_file = create_file_path(filename)
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    # print("音声を再生中...")
    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.05)
        # pass
    # print("再生終了")


def volume():
    """ 音量の調整をする関数 """
    print(f'\n{DECO}')
    print(TITLE)
    print(f'{DECO}\n')
    print('音量を設定できます(0～100)')
    sleep(SLEEP_TIME)
    print('[注意！] パソコンでミュートになっている場合は音がなりません。\n')
    sleep(SLEEP_TIME)
    pygame.mixer.init()
    data_list = read_log(CONF_FILE_PATH)
    volume = data_list['sound'] * 100
    print(f'現在の音量は{volume:.0f}%です')
    sleep(SLEEP_TIME)
    set_volume = keyboard.input_volume('音量を入力: ')
    volume = str(set_volume / 100)
    search_file(CONF_FILE_PATH)
    change_volume(CONF_FILE_PATH, set_volume / 100)
    print(f'\n音量を{set_volume}%に設定しました')
    sleep(SLEEP_TIME)
    print(f'\n{DECO}\n')


def print_with_sound(prompt: str) -> None:
    """ 一文字ずつ表示しながら音を再生する """
    # 初期化
    DELAY = 0.1
    PATH = create_file_path("keyboard.mp3")
    pygame.mixer.init()
    data_list = read_log(CONF_FILE_PATH)
    volume = data_list['sound']
    pygame.mixer.music.set_volume(volume)

    # 音楽ファイルの読み込みと再生（ループ再生）
    pygame.mixer.music.load(PATH)
    pygame.mixer.music.play(loops=-1)  # 無限ループで再生

    # 文字を1文字ずつ表示
    for char in prompt:
        sys.stdout.write(char)  # 文字を表示
        sys.stdout.flush()       # 出力をフラッシュ（即座に表示）
        sleep(DELAY)        # 文字が表示される間隔（デフォルトで0.1秒）

    # 文字の出力が終わったら音楽を停止
    pygame.mixer.music.stop()


if __name__ == "__main__":
    change_volume(CONF_FILE_PATH, 0.3)
    volume()
    # delete_volume_file()

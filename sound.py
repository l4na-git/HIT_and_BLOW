# 音量に関するもの
import keyboard_utils as keyboard
from file_utils import search_file, write_file, delete_file
import pygame
import os
import asyncio


# 定数の定義
ERROR_PRINT = 'ファイルの読み込み中にエラーが発生しました。'
dir = os.path.dirname(__file__)
CONF_FILE_PATH = dir + r'\conf\sound.txt'
DEFAULT_VOLUME = 0.3
DECO = '*' * 70
TITLE = '                           音量の設定'


# 共通
async def play(filename):
    search_file(filename)
    pygame.mixer.init()
    with open(CONF_FILE_PATH, 'r') as f:
        try:
            volume = float(f.readline())
        except OSError:
            print(ERROR_PRINT)
            pass
    pygame.mixer.music.set_volume(volume)  # 音量を設定
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    # print("音声を再生中...")
    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.05)
        # pass
    # print("再生終了")


async def play_correct():
    """ 正解のときに呼び出す関数 """
    await play(r"audio\happy.mp3")


async def play_wrong():
    """ 不正解のときに呼び出す関数 """
    await play(r"audio\sad.mp3")


async def play_count():
    """ カウントダウンをするときに呼び出す関数 """
    await play(r"audio\count.mp3")


async def play_quiz():
    """ 何回目の挑戦を表示するときに呼び出す関数 """
    await play(r"audio\challenge.mp3")


def volume():
    """ 音量の調整をする関数 """
    print(f'\n{DECO}')
    print(TITLE)
    print(f'{DECO}\n')
    print('音量を設定できます(0～100)')
    print('[注意！] パソコンでミュートになっている場合は音がなりません。\n')
    pygame.mixer.init()
    with open(CONF_FILE_PATH, 'r') as f:
        try:
            volume = float(f.readline()) * 100
            print(f'現在の音量は{volume:.0f}%です')
        except OSError:
            print(ERROR_PRINT)
            pass
    set_volume = keyboard.input_volume('音量を入力: ')
    volume = str(set_volume / 100)
    search_file(CONF_FILE_PATH)
    write_file(f'{volume}', CONF_FILE_PATH)
    print(f'\n音量を{set_volume}%に設定しました')
    print(f'\n{DECO}\n')


def set_file():
    """ プログラム実行時に呼び出す関数 """
    return write_file(f'{DEFAULT_VOLUME}', CONF_FILE_PATH)


def delete_volume_file():
    """ ファイルの削除をする関数 """
    delete_file(CONF_FILE_PATH)


if __name__ == "__main__":
    # 音声ファイルのパス
    set_file()
    volume()
    asyncio.run(play_correct())
    # delete_volume_file()

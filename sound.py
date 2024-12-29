# 音を鳴らす
import keyboard_utils as keyboard
from file_utils import search_file, write_volume_file
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

# def read_volume_file():

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


# 正解のとき
async def play_correct():
    await play(r"audio\collect.mp3")


# 不正解のとき
async def play_wrong():
    await play(r"audio\zannen.mp3")


# カウントダウンのとき
async def play_count():
    await play(r"audio\time.mp3")


# 何回目の挑戦を表示するとき
async def play_quiz():
    await play(r"audio\kettei.mp3")


# 音量の調整
def volume():
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
    write_volume_file(f'{volume}', CONF_FILE_PATH, ERROR_PRINT)
    print(f'\n音量を{set_volume}%に設定しました')
    print(f'\n{DECO}\n')


# プログラム実行時に呼び出す
def set_file():
    return write_volume_file(f'{DEFAULT_VOLUME}', CONF_FILE_PATH, ERROR_PRINT)


# ファイルの削除
def delete_volume_file():
    if os.path.exists(CONF_FILE_PATH):
        os.remove(CONF_FILE_PATH)
        # print('ファイルを削除しました')
    else:
        print('ファイルが見つかりません')


if __name__ == "__main__":
    # 音声ファイルのパス
    # play(r"audio\hometai.mp3")
    # play(r"audio\zannen.mp3")
    set_file()
    volume()
    asyncio.run(play_correct())
    # delete_volume_file()

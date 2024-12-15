# 音を鳴らす
import keyboard
import pygame
import os


# OSErrorのときに表示する文章
ERROR_PRINT = 'ファイルの読み込み中にエラーが発生しました。'
# 設定ファイルのパス
CONF_FILE_PATH = r'conf\sound.txt'


# ファイルがあるかどうかを確認
def search_file(filename):
    if not os.path.exists(filename):
        print(f"ファイルが見つかりません: {filename}")
        return False


# 共通
def play(filename):
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
    print("音声を再生中...")
    while pygame.mixer.music.get_busy():
        pass
    print("再生終了")


# 正解のとき
def play_correct():
    play(r"audio\hometai.mp3")


# 不正解のとき
def play_wrong():
    play(r"audio\zannen.mp3")


# 音量の調整
def volume():
    DECO = '*' * 70
    TITLE = '                           音量の設定'
    print(f'\n{DECO}')
    print(TITLE)
    print(f'{DECO}\n')
    print('音量を設定してください(0～100)')
    print('[注意！] パソコンでミュートになっている場合は音がなりません。')
    pygame.mixer.init()
    with open(CONF_FILE_PATH, 'r') as f:
        try:
            volume = float(f.readline()) * 100
            print(f'現在の音量は{volume:.0f}%です')
        except OSError:
            print(ERROR_PRINT)
            pass
    while True:
        input_volume = keyboard.input_int('音量を入力: ')
        if input_volume > 100:
            print('数字は100以下で入力してください')
            continue
        break
    volume = str(input_volume / 100)
    search_file(CONF_FILE_PATH)
    with open(CONF_FILE_PATH, 'w') as f:
        try:
            f.write(f'{volume}')
        except OSError:
            print(ERROR_PRINT)
            pass
    print(f'音量を{input_volume}%に設定しました')
    print(f'\n{DECO}\n')


# 設定ファイルの作成
def create_volume_file():
    with open(CONF_FILE_PATH, 'w') as f:
        try:
            f.write('0.3')  # デフォルトの音量
        except OSError:
            print(ERROR_PRINT)
            pass


# ファイルの削除
def delete_volume_file():
    if os.path.exists(CONF_FILE_PATH):
        os.remove(CONF_FILE_PATH)
        print('ファイルを削除しました')
    else:
        print('ファイルが見つかりません')


if __name__ == "__main__":
    # 音声ファイルのパス
    # play(r"audio\hometai.mp3")
    # play(r"audio\zannen.mp3")
    create_volume_file()
    volume()
    play_correct()
    # delete_volume_file()

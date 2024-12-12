# 音を鳴らす
import keyboard
import os
import pygame


# 共通
def play(filename):
    if not os.path.exists(filename):
        print(f"ファイルが見つかりません: {filename}")
        return
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    # print("音声を再生中...")
    while pygame.mixer.music.get_busy():
        pass
    # print("再生終了")


# 正解のとき
def play_correct():
    play(r"audio\hometai.mp3")


# 不正解のとき
def play_wrong():
    play(r"audio\zannen.mp3")


# 音量の調整
def volume():
    print('音量を設定してください(0～100)')
    pygame.mixer.init()
    # print(f'現在の音量は{}です')
    input_volume = keyboard.input_int('音量を入力: ')
    volume = input_volume / 100
    pygame.mixer.music.set_volume(volume)
    print(f'音量を{input_volume}に設定しました')
    # play(r"audio\hometai.mp3")


if __name__ == "__main__":
    # 音声ファイルのパス
    # play(r"audio\hometai.mp3")
    # play(r"audio\zannen.mp3")
    volume()

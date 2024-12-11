# 音を鳴らす
import os
import pygame


# 正解のとき
def play_correct(filename):
    if not os.path.exists(filename):
        print(f"ファイルが見つかりません: {filename}")
        return
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    print("音声を再生中...")
    while pygame.mixer.music.get_busy():
        pass
    print("再生終了")


if __name__ == "__main__":
    # 音声ファイルのパス
    play_correct(r"audio\hometai.mp3")

# これ使いたい

import pygame
import sys


def create_screen(pygame):
    """ 画像を使用してスクリーンを作成 """
    back_img = pygame.image.load('images/root_back.png')  # 背景画像の読み込み
    back_img = pygame.transform.scale(back_img, (947, 535))  # 背景画像のサイズを変更
    rect_back = back_img.get_rect()  # 背景画像のサイズを取得

    screen = pygame.display.set_mode((rect_back.width, rect_back.height))  # 画面を作成

    return screen, back_img, rect_back


def main():
    """ メインの関数 """
    pygame.init()  # 初期化

    screen, back_img, rect_back = create_screen(pygame)

    pygame.display.set_caption("Hit & Blow")  # タイトルを作成

    running = True
    while running:
        screen.fill((255, 255, 255))
        screen.blit(back_img, rect_back)  # 背景画像の描画

        pygame.display.update()  # 描画処理を実行

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # 閉じるボタンが押されたとき
                running = False
                pygame.quit()  # pygameのウィンドウを閉じる
                sys.exit()  # システム終了


if __name__ == "__main__":
    main()

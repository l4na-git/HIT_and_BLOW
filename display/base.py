# 画面描画のクラス
import pygame
import sys


class DisplayBase():
    WIDTH = 947  # 画面の幅
    HEIGHT = 535  # 画面の高さ
    TITLE = 'Hit and Blow'  # タイトル

    def __init__(self, back_img_name: str):
        self.back_img_name = 'images/' + back_img_name

    def create_screen(self, pygame):
        """ 画像を使用してスクリーンを作成 """
        back_img = pygame.image.load(self.back_img_name)  # 背景画像の読み込み
        back_img = pygame.transform.scale(back_img, (self.WIDTH, self.HEIGHT))  # 背景画像のサイズを変更
        rect_back = back_img.get_rect()  # 背景画像のサイズを取得

        screen = pygame.display.set_mode((rect_back.width, rect_back.height))  # 画面を作成

        return screen, back_img, rect_back

    def event_loop(self, screen, back_img, rect_back):
        """ イベントのループ処理 """
        running = True
        while running:
            screen.fill((255, 255, 255))
            screen.blit(back_img, rect_back)  # 背景画像の描画

            pygame.display.update()  # 描画処理を実行

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 閉じるボタンが押されたとき
                    running = False
                    pygame.quit()  # ウィンドウを閉じる
                    sys.exit()

    def main(self):
        """ メインの関数 """
        pygame.init()  # 初期化

        screen, back_img, rect_back = self.create_screen(pygame)

        pygame.display.set_caption(self.TITLE)  # タイトルを作成

        self.event_loop(screen, back_img, rect_back)


if __name__ == "__main__":
    display = DisplayBase('root_back.png')
    display.main()

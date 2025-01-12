# メニュー表示

from console.quiz import Quiz
from console.how_to import main as how_to_main
from console import user_menu
from console.sound import volume
from utils.keyboard_utils import input_int
from utils.user_utils import get_username
from utils import log_utils
from utils import file_utils
import asyncio

# 装飾とタイトル
DECO = '=' * 70
TITLE = '                            Hit&Blow'

# メニュー番号
MENU_HOW_TO = 1  # 遊び方
VOLUME_SETTING = 2  # 音量の設定
USER_MENU = 3  # ユーザ管理
SHOW_LOG = 4  # ログの表示
MENU_3_DIGIT = 5  # 3桁モード
MENU_4_DIGIT = 6  # 4桁モード
MENU_EXIT = 9  # 終了


async def execute():
    """ メインの関数 """
    while True:
        # メニューを表示
        print_menu()

        # メニュー番号の入力
        num = input_int('メニュー番号を入力してください: ')

        # メニュー番号の機能を実行
        await execute_menu(num)


def print_username():
    """ ユーザ名を表示する関数 """
    username = get_username()
    print(f'こんにちは! {username}さん!!\n')


def print_menu():
    """ メニューの表示をする関数 """
    print(DECO)
    print(TITLE)
    print(f'{DECO}\n')
    print_username()
    print(f'{MENU_HOW_TO}. 遊び方')
    print(f'{VOLUME_SETTING}. 音量の設定')
    print(f'{USER_MENU}. ユーザ管理')
    print(f'{SHOW_LOG}. ログを表示')
    print(f'{MENU_3_DIGIT}. 3桁モード')
    print(f'{MENU_4_DIGIT}. 4桁モード')
    print(f'{MENU_EXIT}. 終了')
    print(f'\n{DECO}\n')


async def execute_menu(menu_no):
    """ メニュー番号の機能を実行する """
    if menu_no == MENU_HOW_TO:
        how_to_main()
    elif menu_no == VOLUME_SETTING:
        volume()
    elif menu_no == USER_MENU:
        await user_menu.execute()
    elif menu_no == SHOW_LOG:
        log_utils.print_log(file_utils.read_log('log_data/guest.json'))
        print('~' * 70)
    elif menu_no == MENU_3_DIGIT:
        quiz_mode3 = Quiz(digit=3, max_challenge=10)
        await quiz_mode3.main()
    elif menu_no == MENU_4_DIGIT:
        quiz_mode4 = Quiz(digit=4, max_challenge=15)
        await quiz_mode4.main()
    elif menu_no == MENU_EXIT:
        print('遊んでくれてありがとう!またね！')
        exit()
    else:
        print('[エラー!!] もう一度入力してください')


if __name__ == '__main__':
    asyncio.run(execute())

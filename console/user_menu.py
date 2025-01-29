"""
ユーザ管理のメニューを表示します
"""
import asyncio

from utils.keyboard_utils import input_int
from utils.user_utils import create_user, delete_user, show_user, change_user
from console.sound import print_with_sound

# 装飾とタイトル
DECO = '*' * 70
TITLE = 'ユーザ管理'

# メニュー番号
CREATE_USER = 1  # ユーザ作成
SHOW_USER = 2  # ユーザ一覧
CHANGE_USER = 3  # ユーザ変更
DELETE_USER = 4  # ユーザ削除
EXIT = 9  # 終了

SLEEP_TIME = 0.7  # メニュー表示後の待機時間


async def main():
    """ メインの関数 """
    while True:
        show_menu()
        num = input_int('メニュー番号を入力してください: ')
        if await execute_menu(num) is False:
            break
        await asyncio.sleep(SLEEP_TIME)


def show_menu():
    """ ユーザメニュー """
    print(DECO)
    print(TITLE.center(65))
    print(f'{DECO}\n')
    print_with_sound('ユーザに関する設定ができます!\n')
    print(f'{CREATE_USER}. ユーザ作成')
    print(f'{SHOW_USER}. ユーザ一覧')
    print(f'{CHANGE_USER}. ユーザ変更')
    print(f'{DELETE_USER}. ユーザ削除')
    print(f'{EXIT}. 終了')
    print(f'\n{DECO}\n')


async def execute_menu(menu_no: int):
    """ メニュー番号の機能を実行する

    Args:
        menu_no (int): ユーザが選択したメニュー番号

    Returns:
        bool: ユーザが終了を選択したらFalse
    """
    if menu_no == CREATE_USER:
        create_user()
    elif menu_no == SHOW_USER:
        show_user()
    elif menu_no == CHANGE_USER:
        change_user()
    elif menu_no == DELETE_USER:
        delete_user()
    elif menu_no == EXIT:
        return False
    else:
        print_with_sound('[エラー!!] もう一度入力してください')


if __name__ == '__main__':
    main()

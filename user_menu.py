# ユーザを管理
from utils.keyboard_utils import input_int
from utils.user_utils import create_user, delete_user, show_user, change_user
import os

# 装飾とタイトル
DECO = '*' * 70
TITLE = '                            ユーザ管理'
CREATE_TITLE = '                            ユーザ作成'
DELETE_TITLE = '                            ユーザ削除'

# メニュー番号
CREATE_USER = 1  # ユーザ作成
SHOW_USER = 2  # ユーザ一覧
CHANGE_USER = 3  # ユーザ変更
DELETE_USER = 4  # ユーザ削除
EXIT = 9  # 終了

PATH = os.path.dirname(__file__) + r'\log_data\\'


def execute():
    """ メインの関数 """
    while True:
        # ユーザメニューを表示
        print_menu()

        # メニュー番号の入力
        num = input_int('メニュー番号を入力してください: ')

        # メニュー番号の機能を実行
        execute_menu(num)


def print_menu():
    """ ユーザメニュー """
    print(DECO)
    print(TITLE)
    print(f'{DECO}\n')
    print(f'{CREATE_USER}. ユーザ作成')
    print(f'{SHOW_USER}. ユーザ一覧')
    print(f'{CHANGE_USER}. ユーザ変更')
    print(f'{DELETE_USER}. ユーザ削除')
    print(f'{EXIT}. 終了')
    print(f'\n{DECO}\n')


def execute_menu(menu_no):
    """ メニュー番号の機能を実行する """
    if menu_no == CREATE_USER:
        create_user()
    elif menu_no == SHOW_USER:
        show_user()
    elif menu_no == CHANGE_USER:
        change_user()
    elif menu_no == DELETE_USER:
        delete_user()
    elif menu_no == EXIT:
        exit()
    else:
        print('[エラー!!] もう一度入力してください')


if __name__ == '__main__':
    execute()

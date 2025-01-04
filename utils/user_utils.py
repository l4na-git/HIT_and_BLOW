# ユーザ管理の関連
from utils.keyboard_utils import input_isalnum_ascii, input_boolean
from utils.file_utils import write_file, search_file, delete_file, read_log, change_log
from pathlib import Path
import glob

DECO = '*' * 70
CREATE_TITLE = '                            ユーザ作成'
DELETE_TITLE = '                            ユーザ削除'
SHOW_TITLE = '                            ユーザ一覧'
CHANGE_TITLE = '                            ユーザ変更'

LOG_PATH = Path('log_data/')
NOW_USE_PATH = Path('conf/now_use.json')


def back_to_menu():
    """ メニューに戻る """
    import user_menu
    user_menu.execute()


def create_user():
    """ ユーザ作成 """
    print(DECO)
    print(CREATE_TITLE)
    print(f'{DECO}\n')
    name = input_isalnum_ascii('作成したいユーザの名前を入力してください(英数字のみ): ')
    filename = f'{name}.json'
    create_path = LOG_PATH / filename
    if search_file(create_path.resolve()):
        print('[エラー!!] 既に存在するユーザです')
        return back_to_menu()
    write_file(filename, create_path)
    print(f'こんにちは、{name}さん')
    print(f'\n{DECO}\n')


def show_user():
    """ ユーザ一覧を表示 """
    print(DECO)
    print(SHOW_TITLE)
    print(f'{DECO}\n')
    files = glob.glob(f'{LOG_PATH.resolve()}/*.json')
    count = 0
    for file in files:
        count += 1
        name = Path(file).stem
        print(f'{count}. {name}さん')
    print(f'\nユーザは{count}人です')
    print(f'\n{DECO}\n')


def change_user():
    """ ユーザ変更 """
    print(DECO)
    print(CHANGE_TITLE)
    print(f'{DECO}\n')
    data = read_log(NOW_USE_PATH)
    username = data['username']
    print(f'現在のユーザ: {username}')
    change_username = input_isalnum_ascii('変更したいユーザの名前を入力してください(英数字のみ): ')
    change_log(NOW_USE_PATH, change_username)
    print(f'\n{username}に変更しました!')
    print(f'\n{DECO}\n')


def delete_user():
    """ ユーザ削除 """
    print(DECO)
    print(DELETE_TITLE)
    print(f'{DECO}\n')
    name = input_isalnum_ascii('削除したいユーザの名前を入力してください(英数字のみ): ')
    filename = f'{name}.json'
    create_path = LOG_PATH / filename
    if not search_file(create_path):
        print('[エラー!!] 存在しないユーザです')
        return back_to_menu()
    data = read_log(create_path)
    count = len(data)
    print(f'\n{name}さんの記録: {count}件')
    if input_boolean('\n削除してもよろしいですか？'):
        delete_file(create_path)
        print(f'\n{name}さんのデータを削除しました')
    else:
        print('\n削除をキャンセルしました')
    print(f'\n{DECO}\n')

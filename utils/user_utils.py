# ユーザ管理の関連
from utils.keyboard_utils import input_isalnum_ascii, input_boolean
from utils.file_utils import write_file, search_file, delete_file, read_log
from pathlib import Path

DECO = '*' * 70
CREATE_TITLE = '                            ユーザ作成'
DELETE_TITLE = '                            ユーザ削除'

PATH = Path('log_data\\')


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
    create_path = PATH / filename
    if search_file(create_path):
        print('[エラー!!] 既に存在するユーザです')
        return back_to_menu()
    write_file(filename, create_path)
    print(f'こんにちは、{name}さん')
    print(f'\n{DECO}\n')


def delete_user():
    """ ユーザ削除 """
    print(DECO)
    print(DELETE_TITLE)
    print(f'{DECO}\n')
    name = input_isalnum_ascii('削除したいユーザの名前を入力してください(英数字のみ): ')
    filename = f'{name}.json'
    create_path = PATH / filename
    if not search_file(create_path):
        print('[エラー!!] 存在しないユーザです')
        return back_to_menu()
    data = read_log(filename)
    count = len(data)
    print(f'\n{name}さんの記録: {count}件')
    if input_boolean('\n削除してもよろしいですか？'):
        delete_file(create_path)
        print(f'\n{name}さんのデータを削除しました')
    else:
        print('\n削除をキャンセルしました')
    print(f'\n{DECO}\n')

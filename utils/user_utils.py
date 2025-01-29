"""
ユーザ管理に関する処理をします
"""
import glob
from pathlib import Path

from utils.keyboard_utils import input_isalnum_ascii, input_boolean
from utils.file_utils import (
    create_or_reset_file, search_file, delete_file,
    read_json_file, change_username
)
from console.sound import print_with_sound

# 定数の定義
DECO = '*' * 70
TITLES = {
    "create": "ユーザ作成",
    "delete": "ユーザ削除",
    "show": "ユーザ一覧",
    "change": "ユーザ変更",
}

LOG_PATH = Path('log_data/')
NOW_USE_PATH = Path('config/setting.json')


def show_title(title_key: str):
    """タイトルを表示する

    Args:
        title_key (str): 表示するTITLESのキー
    """
    print(DECO)
    print(f'{TITLES[title_key]}'.center(65))
    print(f'{DECO}\n')


def create_user():
    """ ユーザ作成 """
    show_title('create')
    print_with_sound('ユーザを作成します\n')
    name = input_isalnum_ascii('作成したいユーザの名前を入力してください(英数字のみ): ')
    path = LOG_PATH / f'{name}.json'
    if search_file(path.resolve()):
        print_with_sound('[エラー!!] 既に存在するユーザです')
        return
    create_or_reset_file(path)
    print_with_sound(f'こんにちは、{name}さん')
    print(f'\n{DECO}\n')


def show_user():
    """ ユーザ一覧を表示 """
    show_title('show')
    print_with_sound('ユーザの一覧を表示します\n')
    files = glob.glob(f'{LOG_PATH.resolve()}/*.json')
    for index, file in enumerate(files, 1):
        print_with_sound(f'{index}. {Path(file).stem}さん')
    print_with_sound(f'\nユーザは{index}人です')
    print(f'\n{DECO}\n')


def change_user() -> None:
    """ ユーザ変更 """
    show_title('change')
    print_with_sound('ゲームに挑戦するユーザを変更します\n')
    username = get_username()
    print_with_sound(f'現在のユーザ: {username}')
    input_username = input_isalnum_ascii('変更したいユーザの名前を入力してください(英数字のみ): ')
    path = LOG_PATH / f'{input_username}.json'
    if search_file(path.resolve()):
        change_username(NOW_USE_PATH, input_username)
        print_with_sound(f'\n{input_username}に変更しました!')
    else:
        print_with_sound('[エラー!!] 存在しないユーザです')
    print(f'\n{DECO}\n')


def delete_user() -> None:
    """ ユーザ削除 """
    show_title('delete')
    print_with_sound('ユーザを削除します\n')
    name = input_isalnum_ascii('削除したいユーザの名前を入力してください(英数字のみ): ')
    path = LOG_PATH / f'{name}.json'
    if not search_file(path):
        print_with_sound('[エラー!!] 存在しないユーザです')
        return
    data = read_json_file(path)
    print_with_sound(f'\n{name}さんの記録: {len(data)}件')
    if input_boolean('\n削除してもよろしいですか？'):
        delete_file(path)
        print_with_sound(f'\n{name}さんのデータを削除しました')
    else:
        print_with_sound('\n削除をキャンセルしました')
    print(f'\n{DECO}\n')


def get_username():
    """ 現在のユーザ名を取得 """
    data = read_json_file(NOW_USE_PATH)
    return data['username']

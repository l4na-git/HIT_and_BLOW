"""
ログに関する処理をします
"""
from time import sleep
from pathlib import Path

import utils.file_utils as file_utils
from console.sound import print_with_sound
from utils.user_utils import get_username


# 定数の定義
INDENT_SPACE = " " * 2
LINE_LENGTH = 30
DECO = '*' * 70
SLEEP_TIME = 1


def show_log():
    """ ログを表示する関数 """
    nowuser = get_username()
    path = Path('log_data/' + nowuser + '.json').resolve()

    data = file_utils.read_json_file(path)
    if data == {}:
        return
    for index, i in enumerate(data[-5:], 1):
        print(f"{index}: ")
        print(f"日時: {i['datetime']}")
        print(f"答え: {i['answer']}")
        print(f"クリア: {'yes' if i['clear'] else 'no'}")
        print(f"入力回数: {len(i['log'])}")
        print("-" * 20)
        for j in i["log"]:
            print(
                f"{INDENT_SPACE}入力: {j['input']}, ヒット: {j['hit']}, ブロー: {j['blow']}")
            if j != i["log"][-1]:
                print(f"{INDENT_SPACE}" + "~" * LINE_LENGTH)
        print("=" * LINE_LENGTH)
        sleep(SLEEP_TIME)
    print(f'\n{index}件表示しました')


def main():
    """ タイトルとログを表示する """
    nowuser = get_username()
    print(DECO)
    print(f'{nowuser}さんのログ'.center(65))
    print(f'{DECO}\n')
    print_with_sound('最新の5回分を表示します\n')
    show_log()
    sleep(SLEEP_TIME)
    print(f'\n{DECO}\n')

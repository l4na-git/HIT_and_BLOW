# ファイルの操作に関するもの
import os
import json


def search_file(filename: str) -> bool:
    """ ファイルがあるかどうかを確認する関数 """
    if not os.path.exists(filename):
        # print(f"ファイルが見つかりません: {filename}")
        return False
    return True


def write_file(num: float, file_path: str) -> None:
    """ 設定ファイルを作成する関数 """
    with open(file_path, 'w') as f:
        try:
            f.write(num)
        except OSError as e:
            print('ファイルの読み込み中にエラーが発生しました。')
            print(e)
            pass


def read_file(file_path: str):
    """ ファイルの読み込みをする関数 """
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            return f.readline()
        except OSError as e:
            print('ファイルの読み込み中にエラーが発生しました。')
            print(e)
            pass


def read_all_file(file_path: str) -> list:
    """ ファイルの読み込みをする関数 """
    list_data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            for line in f:
                list_data.append(line.strip())
            return list_data
        except OSError as e:
            print('ファイルの読み込み中にエラーが発生しました。')
            print(e)
            return []


def read_log():
    """ 記録の読み込みをする関数 """
    with open("log_data/guest.json", 'r') as f:
        return json.load(f)


def add_log(data):
    """ 記録の追加をする関数 """
    with open("log_data/guest.json", 'r+') as f:
        try:
            log_data = json.load(f)
        except json.decoder.JSONDecodeError:
            log_data = []
        log_data.append(data)
        f.seek(0)
        json.dump(log_data, f, indent=4)
        f.truncate()


def delete_file(file_path: str) -> None:
    """ ファイルの削除をする関数 """
    if os.path.exists(file_path):
        os.remove(file_path)
        # print('ファイルを削除しました')
    else:
        print('ファイルが見つかりません')

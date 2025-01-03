# ファイルの操作に関するもの
import os
import json


def search_file(filename: str) -> bool:
    """ ファイルがあるかどうかを確認する関数 """
    if not os.path.exists(filename):
        print(f"ファイルが見つかりません: {filename}")
        return False


def write_volume_file(num: float, CONF_FILE_PATH: str, ERROR_PRINT: str
                      ) -> None:
    """ 設定ファイルを作成する関数 """
    with open(CONF_FILE_PATH, 'w') as f:
        try:
            f.write(num)
        except OSError:
            print(ERROR_PRINT)
            pass


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

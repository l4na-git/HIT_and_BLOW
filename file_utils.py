# ファイルの操作に関するもの
import os
import json

# ファイルがあるかどうかを確認
def search_file(filename: str) -> bool:
    if not os.path.exists(filename):
        print(f"ファイルが見つかりません: {filename}")
        return False


# 設定ファイルの作成
def write_volume_file(num: float, CONF_FILE_PATH: str, ERROR_PRINT: str):
    with open(CONF_FILE_PATH, 'w') as f:
        try:
            f.write(num)
        except OSError:
            print(ERROR_PRINT)
            pass



def read_log():
    with open("log_data/test.json", 'r') as f:
        return json.load(f)

def add_log(data):
    with open("log_data/test.json", 'r+') as f:
        try:
            log_data = json.load(f)
        except json.decoder.JSONDecodeError:
            log_data = []
        log_data.append(data)
        f.seek(0)
        json.dump(log_data, f, indent=4)
        f.truncate()

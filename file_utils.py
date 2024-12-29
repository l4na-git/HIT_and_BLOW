# ファイルの操作に関するもの
import os


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

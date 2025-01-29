"""
ファイルの操作に関する処理をします
"""
import os
import json
from typing import List


def search_file(filename: str) -> bool:
    """ファイルが存在するかを確認する

    Args:
        filename (str): 確認するファイル名

    Returns:
        bool: ファイルが存在する場合はTrue、存在しない場合はFalse
    """
    return os.path.exists(filename)


def create_or_reset_file(filepath: str) -> None:
    """ファイルを作成、またはリセットをする

    Args:
        filepath (str): 作成、またはリセットするファイルのパス
    """
    try:
        open(filepath, 'w').close()
    except OSError as e:
        print('ファイルの作成またはリセット中にエラーが発生しました。')
        print(e)


def read_file(filepath: str) -> List[str]:
    """ファイルの内容を読み込む

    Args:
        filepath (str): 読み込むファイルのパス

    Returns:
        List[str]: ファイルの内容を文字列のリストとして返す
    """
    try:
        list_data = []
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                list_data.append(line.rstrip())
        return list_data
    except OSError as e:
        print('ファイルの読み込み中にエラーが発生しました。')
        print(e)
        return []


def read_json_file(filepath: str) -> dict:
    """JSONファイルの内容を読み込む

    Args:
        filepath (str): 読み込むファイルのパス

    Returns:
        dict: パースされたファイルの内容、失敗した場合は空の辞書を返す
    """
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except json.decoder.JSONDecodeError:
        print('データはありません')
        return {}


def update_json_file(filepath: str, data: dict) -> None:
    """JSONファイルにデータを追加する

    Args:
        filepath (str): データの追加をする対象のファイルパス
        data (dict): 追加するデータ
    """
    try:
        with open(filepath, 'r+') as f:
            log_data = json.load(f)
            log_data.append(data)
            f.seek(0)
            json.dump(log_data, f, indent=4)
            f.truncate()
    except json.decoder.JSONDecodeError:
        log_data = []


def change_username(file_path: str, data: str):
    """ プレイするユーザの変更をする関数 """
    with open(file_path, 'r+') as f:
        try:
            log_data = json.load(f)
        except json.decoder.JSONDecodeError:
            log_data = []
        log_data['username'] = data
        f.seek(0)
        json.dump(log_data, f, indent=4)
        f.truncate()


def change_volume(file_path: str, data: float):
    """ 音量の変更をする関数 """
    with open(file_path, 'r+') as f:
        try:
            log_data = json.load(f)
        except json.decoder.JSONDecodeError:
            log_data = []
        log_data['sound'] = data
        f.seek(0)
        json.dump(log_data, f, indent=4)
        f.truncate()


def delete_file(filepath: str) -> None:
    """ファイルの削除をする

    Args:
        filepath (str): 削除するファイルのパス
    """
    if os.path.exists(filepath):
        os.remove(filepath)
    else:
        print('ファイルが見つかりません')

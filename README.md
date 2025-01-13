# HIT_and_BLOW

HIT&BLOWをPythonで作成したものです。

## 概要

- HIT&BLOWは数字を当てるゲームです。
- 3桁と4桁のモードがあります。
- CUIかGUIか実行する方法を選択できます。

## インストール方法と実行

以下の手順でリポジトリをローカル環境にインストール、実行してください。

### 1. リポジトリをクローン
```bash
git clone https://github.com/tagra-git/hit_and_blow.git
cd hit_and_blow
```
### 2. 依存関係をインストール
```bash
pip install pygame
```
### 3. 実行
- GUIで実行されます。
```bash
python hitandblow.py -g
python hitandblow.py --gui
```
- CUIで実行されます。
```bash
python hitandblow.py -c
python hitandblow.py --cui
```
- ヘルプが表示されます。
```bash
python hitandblow.py -h
python hitandblow.py --help
```
※オプションが指定されていない場合はCUIで実行されます。
## ファイル構成
```
.
├── README.md
├── audio
│   ├── challenge.mp3               # 挑戦回数を表示する際に再生する音源
│   ├── count.mp3                   # カウントダウンする際に再生する音源
│   ├── happy.mp3                   # 正解した際に再生する音源
│   ├── keyboard.mp3                # 文字を表示する際に再生する音源
│   └── sad.mp3                     # 不正解した際に再生する音源
├── config
│   ├── correct_message.txt         # 正解した際に表示するテキスト
│   ├── help_message.txt            # ヘルプオプションが使用された際に表示するテキスト
│   ├── how_to.txt                  # 遊び方を記述するテキスト
│   ├── setting.json                # ユーザ、音量を保存するファイル
│   └── wrong_message.txt           # 不正解した際に表示するテキスト
├── console
│   ├── how_to.py                   # 遊び方を表示
│   ├── main_menu.py                # メインメニューを表示
│   ├── message.py                  # 結果に応じてメッセージを表示
│   ├── quiz.py                     # hit&blowの処理
│   ├── sound.py                    # 音に関する処理
│   └── user_menu.py                # ユーザメニューを表示
├── display
│   └── game.py                     # ゲーム画面を描画
├── hitandblow.py                   # オプションに関する処理
├── log_data                        # それぞれのユーザのログを保存
│   └── guest.json
├── requirements.txt                # 依存関係を記述
└── utils
    ├── file_utils.py               # ファイル操作に関する処理
    ├── keyboard_utils.py           # 入力された値に対する処理
    ├── log_utils.py                # ログファイルに関する処理
    └── user_utils.py               # ユーザ管理に関する処理

```

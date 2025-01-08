# HIT_and_BLOW

HIT&BLOWをPythonで作成したものです。

## 概要

- HIT&BLOWは数字を当てるゲームです。
- Pythonで作成しています。
- 3桁と4桁のモードがあります。

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
```
- CUIで実行されます。
```bash
python hitandblow.py -c
```

## ファイル構成
```
.
│  .gitignore
│  hitandblow.py
│  how_to.py
│  index.txt  # 遊び方の説明
│  main_menu.py  # メニュー表示
│  message.py  # 正解、不正解に対してのアニメーション
│  quiz.py  # ゲームの処理
│  requirements.txt  # 依存関係
│  sound.py  # 音を鳴らすための処理
│  user_menu.py  # ユーザ管理メニュー
├─audio  # 音源を保存
├─conf
│      how_to.txt  # 遊び方の説明
│      now_use.json  # ゲーム起動中に使用
├─display
│      base.py  # 基底クラスを定義
│      info.py  # 遊び方の画面
│      main.py  # 起動時の画面
│      mgenplus-1p-regular.ttf
│      play.py  # ゲームする画面
│      sound.py  # 音量調整する画面
├─images  # GUI起動時に使用する画像
├─log_data  # 遊んだ記録を保存
└─utils
      file_utils.py  # ファイル入出力に関する処理
      keyboard_utils.py  # キーボードから入力された値の処理
      log_utils.py  # ログを表示
      user_utils.py  # ユーザ管理に関する処理

```

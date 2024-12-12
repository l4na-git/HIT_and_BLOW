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
```bash
python main_menu.py
```
メニューが表示されます。

## ファイル構成
```
.
├──audio           # 音源を保存
├──how_to.py       # 遊び方の説明
├──keyboard.py     # キーボードから入力された値の処理
├──main_menu.py    # メニュー表示
├──quiz.py         # ゲームの処理
└──sound.py        # 音を鳴らすための処理
```

# 用途と特徴
- 単語集作成補助ツール。
- CATツールに単語集をアップロードする下準備に最適なプログラム。
- `ta01.py`を実行すると自然言語 (英語) の文章から単語を吸い出して原形にし、なおかつ重複を削除した単語集(csv形式)ができあがる。

# 使い方
1. `source.txt`に単語を吸い出したいテキストを貼り付ける。
2. Anaconda Promptで`$ python ta01.py`と入力しエンター。
3. `source.csv`の生成完了。
4. あとはエクセル上で日本語訳をつけてCATツールにアップロード。

以下ファイルの説明。
## ta01.py
プログラムのメインとなるファイル。

## source.txt
このファイルに単語を吸い出したい文章を貼り付ける。
現在サンプルとしてWilliam Shakespeareの["A Midsummer Night's Dream"](http://shakespeare.mit.edu/midsummer/index.html)、Act 1, Scene 1を採用。

## source.csv
`ta01.py`実行後に生成されるファイル。中身はアルファベット順に重複なく英単語が並ぶ。

# 開発環境
- Python 3.6.5 |Anaconda, Inc.| (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bi
t (AMD64)] on win32
- Windows7

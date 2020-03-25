# Pythonを利用したツイートサンプル
## 概要
取得したTwitter APIのアカウントで「Pythonに投稿！」とつぶやくサンプルです。
Pythonは3系を想定しています。

## 利用方法
### 事前準備
1. Twitter APIの取得
APIの取得方法は、以下を参考にしてください。
https://siaris.hatenablog.jp/entry/2020/03/25/204925

1. tweepyモジュールをインストール
    ```
    pip install tweepy
    ```

### 利用方法
1. Twitter APIの各種キーを代入
    ```
    # 取得した各種キーを代入
    CK="<Consumer Key>"
    CS="<Consumer Secret>"
    AT="<Access Token>"
    AS="<Access Token Secret>"
    ```

1. 実行
    ```
    python tweetMessage.py
    ```


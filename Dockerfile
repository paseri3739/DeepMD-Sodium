# ベースとなるDockerイメージを指定。この場合はPython 3.8を指定
FROM python:3.11.4

# イメージ内に作業ディレクトリを作成
WORKDIR /usr/src/app

# 必要なパッケージをイメージにコピー
COPY requirements.txt ./

# パッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# スクリプトをイメージにコピー
COPY . .

# スクリプトを実行するコマンド
CMD [ "python", "./your_script.py" ]

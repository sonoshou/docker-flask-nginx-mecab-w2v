# ベースイメージ
FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y mecab \
    && apt-get install -y libmecab-dev \
    && apt-get install -y mecab-ipadic-utf8\
    && apt-get install -y swig\
    && apt-get install -y git\
    && apt-get install -y make\
    && apt-get install -y curl\
    && apt-get install -y xz-utils\
    && apt-get install -y file\
    && apt-get install -y sudo\
    && apt-get install -y wget

# mecab-ipadic-neologdのインストール
WORKDIR /var/www
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git\
    && cd mecab-ipadic-neologd\
    && bin/install-mecab-ipadic-neologd -n -y

RUN apt-get update
RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN python3.6 -m pip install pip --upgrade

# word2vecのダウンロード
WORKDIR /usr/lib
RUN git clone --depth 1 https://bitbucket.org/sonoshou/w2v-model-light.git

# 依存Pythonライブラリ一覧コピー
WORKDIR /var/www
COPY requirements.txt ./

# 依存Pythonライブラリインストール
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /var/www/src

CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]

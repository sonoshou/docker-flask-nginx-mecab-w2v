# 概要

- docker上にflaskとnginxを構築する。
- ウェブブラウザ上でmecabとword2vecのテストができる。

## 起動

```
# make run
```

## 停止

```
# make stop
```

## サンプル

### mecabのテスト

```
http://localhost/mecab?q=ピコ太郎はテストをします。
```

```
ピコ太郎 は テスト を し ます 。
```

- （mecab-ipadic-neologdのため、新語に対応している。）

### word2vecのテスト

```
http://localhost/w2v?q=テスト
```

```
[('試験', 0.7903265357017517), ('トレーニング', 0.6843209862709045), ('追試', 0.6640247702598572), ('練習', 0.6420447826385498), ('適性検査', 0.6370010375976562), ('シェイクダウン', 0.6339285373687744), ('チェック', 0.6325801610946655), ('実験', 0.6300682425498962), ('トライアル', 0.6293531060218811), ('検査', 0.6283568143844604)]
```

- 類義語のテストです。

## 前提

- docker及びdocker-composeのインストール

## 構成

```
.
├── Makefile
├── README.md
├── docker-compose.yml
├── flask
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── src
│   │   ├── app.py
│   │   ├── config.yml
│   │   └── sample.py
│   └── uwsgi.ini
└── nginx
    ├── Dockerfile
    └── nginx.conf
```

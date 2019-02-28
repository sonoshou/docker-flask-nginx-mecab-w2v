#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request
from gensim.models import word2vec as GensimWord2Vec
import MeCab
import yaml, os
from sample import Sample

app = Flask(__name__)
sample = Sample()

@app.route('/')
def hello():
    return "Hello"

@app.route('/mecab')
def _mecab():
    q = request.args.get('q')
    return sample.mecab(q)

@app.route('/w2v')
def _w2v():
    q = request.args.get('q')
    return sample.w2v(q)

if __name__ == '__main__':
    app.run()

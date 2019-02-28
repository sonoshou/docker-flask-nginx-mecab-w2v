#!/usr/bin/python
# -*- coding: utf-8 -*-

from gensim.models import word2vec as GensimWord2Vec
import MeCab, yaml, os, io, sys

class Sample:
    def __init__(self):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

        # 設定ファイルの読み込み
        with open(os.path.dirname(os.path.abspath(__file__)) + '/config.yml', 'r', encoding='utf-8') as yml:
            self.config = yaml.load(yml)

        # モデルの読み込み
        self.model = GensimWord2Vec.Word2Vec.load(self.config['path']['w2v_model'])
        self.tagger = MeCab.Tagger("-Owakati -d{0}".format(self.config['path']['mecab']))

    def mecab(self, q):
        print(q)
        print(self.tagger.parse(q))
        return str(self.tagger.parse(q))

    def w2v(self, q):
        print(q)
        print(self.model.wv.most_similar(positive=[q]))
        return str(self.model.wv.most_similar(positive=[q]))

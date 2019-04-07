#coding:utf-8

"""
参考
http://qiita.com/ynakayama/items/2cc0b1d3cf1a2da612e4
"""

# Flask などの必要なライブラリをインポートする
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient, DESCENDING
import numpy as np
import sys

# 自身の名称を app という名前でインスタンス化する
app = Flask(__name__)

client = MongoClient()
db = client['MusicBrainz']
collection = db['artist']

# ここからウェブアプリケーション用のルーティングを記述
# index にアクセスしたときの処理
@app.route('/')
def index():
    title = "100本ノック 69"
    # index.html をレンダリングする
    return render_template('index.html',
                           title=title,
                           total_count=0)

# /post にアクセスしたときの処理
@app.route('/post', methods=['GET', 'POST'])
def post():
    title = "検索結果"
    if request.method == 'POST':
        # リクエストフォームから「名前」を取得して
        name = request.form['name']
        area = request.form['area']
        tag = request.form['tag']

        clue = []
        if len(name) > 0:
            #アーティスト名と別名の両方で検索
            clue.append({'$or' : [{'name' : name}, {'aliases.name' : name}]})
        if len(area) > 0:
            clue.append({'area' : area})
        if len(tag):
            clue.append({'tags.value' : tag})

        total_count = 0
        result_list = []
        if len(clue) > 0:
            #レーティングでソートすると高得点の票が1票だけみたいなのが上位になっておもしろくない
            #なのでレーティングの投票数でソート
            tmp = collection.find({'$and' : clue}).sort("rating.count", DESCENDING)
            total_count = tmp.count()
            result_list = tmp[:10]

        # index.html をレンダリングする
        return render_template('index.html',
        						name=name,
                               area=area,
                               tag=tag,
                               title=title,
                               result_list=result_list,
                               total_count=total_count)
    else:
        # エラーなどでリダイレクトしたい場合はこんな感じで
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
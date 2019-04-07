コメント
・70
基本的にはやるだけ
データの文字コードがUTF-8ではないことに気をつけよう(WINDOWS 1252)
(http://qiita.com/segavvy/items/0e91fe02088b875a386a)

・71
ストップリストは既存のものを使用するなり、自分で作成するなり好きにすれば良い
ただ、既存のものだと素性として効きそうな否定語が含まれていることが多く、
個人的に気に入らなかったので、自分で作成した
頻度の高い単語をストップワードとして用いると良いらしい
(http://kenichia.hatenablog.com/entry/2016/02/22/111027)

・72
素性(feature, 特徴量)
本当は行列演算しやすいようにベクトル化しておくべきな気もするが、
ここは指示に従って最低限のことをやればいい

ステミング
単語から語幹を取り出す処理。ex. 「投げる」-> 「投げ」
ステミング処理は単語の正規化の方法の一種。
他の単語の正規化の方法としてはレンマ化(見出し語化)が挙げられる。

参考:
https://qiita.com/Hironsan/items/2466fe0f344115aff177
http://kenichia.hatenablog.com/entry/2016/02/22/111027
http://d.hatena.ne.jp/jetbead/20131109/1383968030

・73
理論さえ追えれば、あとは目的関数の最適化をするだけ
手法は色々あるので、好きなものを選べば良い
https://www.slideshare.net/tkm2261/ss-42149384
http://postd.cc/optimizing-gradient-descent/
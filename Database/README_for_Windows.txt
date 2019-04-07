・KVS(Key-Value-Store)の導入
  
  1.Redisのインストール
    Redisのインストーラーをここから入手(https://github.com/MSOpenTech/redis/releases)
    使用メモリの最大値はデフォルトの100MBだと足りないかもしれないので多めに設定しておくべし
    (むしろ最大値を設定しないくらいのほうが良いかも?)
    環境変数などの設定はお好みで

  2.redis-pyのインストール
    pip install redisでインストールできるはず
    だめならソースから(https://github.com/andymccurdy/redis-py)

  3.使い方
  	3.1. redis-serverでサーバー起動(別ターミナルで)
         redis-server [設定ファイル(インストールしたRedisのフォルダからパクる)]
  	     参考(http://qiita.com/yoh-nak/items/69c26e7d627e2b5a95e2)
  	     
  	3.2. redis-cliでクライアントの起動 or redis-pyの使用
    3.3. redis-cliでshutdown(これをするとディスクに保存される)


・MongoDB
  
  1. MongoDBおよびpymongoのインストール
     MongoDB(https://www.mongodb.com/download-center?jmp=homepage#community)はここからインストール
     pymongoはpip install pymongoでインストールできるはず

  2. 下準備
     データとログの保存するためのディレクトリを作成しておく
     設定ファイルを作っておくと捗る

  3. 使い方
     3.1. mongodでサーバーを起動(別ターミナルで)
          下2つのどちらかで
     	  mongod --dbpath [データ用ディレクトリ] --logpath [データ用ディレクトリ]
     	  mongod --config [設定ファイル]

     3.2. mongoでサーバーに接続 or pymongoを利用

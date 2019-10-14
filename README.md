[![License](http://img.shields.io/badge/license-mit-blue.svg?style=flat)](https://github.com/0x0u/dmm/blob/master/LICENSE.txt)

[![Build Status](https://travis-ci.org/0x0u/dmm_search3.svg?branch=master)](https://travis-ci.org/0x0u/dmm_search3)

https://pypi.org/project/dmm-search3/

# dmm_search3
DMM APIをPythonで扱うライブラリです。
[DMM Webサービス](https://affiliate.dmm.com/api/)をPythonで扱うためのライブラリです。[コチラ](https://affiliate.dmm.com/api/regist_guide/)DMMアフィリエイトのアカウントを作成して、API IDとアフィリエイトIDを取得して使います。

## Install
pipでインストールします。
```
$ pip3 install dmm_search3
```

## Usage
#### モジュールのインポート
```Python
from dmm import DMM
```

#### 取得したAPI IDとアフィリエイトIDをセット
```Python
api_id = 'your_api_id'
affiliate_id = 'your_affiliate_id'
```

#### インスタンスの作成
```Python
api = DMM(api_id=api_id, affiliate_id=affiliate_id)
```

#### 各検索メソッド
```Python
#商品検索
item_search = api.item_search(site='FANZA', hits=1, keyword='バレンタイン')

#フロア一覧
floor_list = api.floor_list()

#女優検索
actress_search = api.actress_search()

#ジャンル検索
genre_search = api.genre_search(floor_id=91)

#メーカー検索
maker_search = api.maker_search(floor_id=91)

#シリーズ検索
series_search = api.series_search(floor_id=91)

#作者検索
author = api.author_search(floor_id=72)
```

各メソッドの引数は以下のリファレンスを参照してください。

API リファレンス: https://affiliate.dmm.com/api/v3/itemlist.html

#### サンプル動画ダウンロードメソッド
```Python
DMM.sample_download(cid='blor0018', fname='sample')
```
サンプル動画をダウンロードするメソッドです。クラスメソッドなのでインスタンス化する必要はありません。第一引数（cid）には商品検索メソッドから得たcontent_idや商品ページから取得できる品番を入れ、第二引数（fname）には必須ではないですが任意のファイル名を入れます。第二引数を省略した場合はcidがファイル名となります。

#### Example
商品検索メソッドを使って検索キーワードに関する９つのタイトルを出力する例です。

```Python
items = api.item_search(site='DMM.com', keyword='バレンタイン', hits=9)
for i in items['result']['items']:
    print(i.get('title'))

# => バレンタイン・ゲーム（単話）   
#    落合くんの半減（単話）
#    オトメ錬金術（単話）
#    アクションピザッツ 2016年4月号
#    コミックホットミルク 2016年03月号
#    comicアンスリウム Vol.35
#    すぺしゃるでこれーしょん（単話）
#    とっぴんぐえんじぇるず（単話）
#    チョコはおまけで（単話）
```

サンプル動画ダウンロードメソッドの使用例
商品検索検索メソッドからcontent_idを抜き出して、サンプル動画ダウンロードメソッドに渡す例です。
```Python
items = api.item_search(site='FANZA', keyword='バレンタイン', hits=10)
for i in  items['result']['items']:
    cid = i.get('content_id')
    title = i.get('title')
    status = DMM.sample_download(cid=cid)
    print(cid, title, status)
``

## License
MIT    
https://github.com/0x0u/dmm_search3/blob/master/LICENSE.txt

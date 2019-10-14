# dmm_search3

[![License](http://img.shields.io/badge/license-mit-blue.svg?style=flat)](https://github.com/0x0u/dmm/blob/master/LICENSE.txt)

[![Build Status](https://travis-ci.org/0x0u/dmm_search3.svg?branch=master)](https://travis-ci.org/0x0u/dmm_search3)


https://pypi.org/project/dmm-search3/

## dmm_search3 is 何
[DMM Webサービス](https://affiliate.dmm.com/api/)をPythonで扱うためのライブラリです。[コチラ](https://affiliate.dmm.com/api/regist_guide/)からアカウントを作成して、API IDとアフィリエイトIDを取得しておく必要があります。

## インストール
pipでインストールします。
```
$ pip3 install dmm_search3
```

## 使い方
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
dmm = DMM(api_id=api_id, affiliate_id=affiliate_id)
```

#### 検索(search)メソッド
```Python
dmm.search('ItemList', keyword='六本木', hits=5, offset=10, sort='review')
```

検索メソッドの第一引数は、ItemList(商品検索)、FloorList(フロア検索)、ActressSearch(女優検索)、GenreSearch(ジャンル検索)、MakerSearch(メーカー検索)、SeriesSearch(シリーズ検索)、AuthorSearch(作者検索)のいずれかを指定します。第二引数以降は[APIリファレンス](https://affiliate.dmm.com/api/v3/itemlist.html)のリクエストパラメータを指定します。可変長引数で受け取るので、`keyword='バレンタイン'`のように明示的にキーワードと値を指定します。

#### 検索メソッドの使用例
```Python
items = dmm.search('ItemList', keyword='バレンタイン', hits=9)
for i in items['items']:
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

レスポンスに関しても[APIリファレンス](https://affiliate.dmm.com/api/v3/itemlist.html)のレスポンスフィールドを参照してください。


#### サンプル動画ダウンロード(video_download)メソッド
```Python
DMM.video_download(cid='1vandr00069', fname='sample')
```
サンプル動画をダウンロードするメソッドです。これはクラスメソッドなのでインスタンス化する必要はありません。第一引数に動画のcontent_idを、第二引数にはファイル名を入れます。第二引数を入れた場合は、ファイル名.mp4というファイル名でダウンロードされます。第二引数を省略した場合はcontent_idがファイル名となります。

#### サンプル動画ダウンロードメソッドの使用例
searchメソッドからcontent_idを抜き出して、video_downloadメソッドに渡す例です。
```Python
items = dmm.search('ItemList', keyword='六本木', hits=9)
for i in items['items']:
    cid = i.get('content_id')
    DMM.video_download(cid)
```

## APIリファレンス
検索メソッド第一引数(物理名を指定します)

|論理名|物理名|APIリファレンス|
|:--:|:--:|:--:|
|商品検索|ItemList|https://affiliate.dmm.com/api/v3/itemlist.html
|フロア検索|FloorList|https://affiliate.dmm.com/api/v3/floorlist.html
|女優検索|ActressSearch|https://affiliate.dmm.com/api/v3/actresssearch.html
|ジャンル検索|GenreSearch|https://affiliate.dmm.com/api/v3/genresearch.html
|メーカー検索|MakerSearch|https://affiliate.dmm.com/api/v3/makersearch.html
|シリーズ検索|SeriesSearch|https://affiliate.dmm.com/api/v3/seriessearch.html
|作者検索|AuthorSearch|https://affiliate.dmm.com/api/v3/authorsearch.html

検索メソッド第二引数以降

|論理名|物理名|値のサンプル|概要|
|:--|:--|:--|:--|
|サイト|site|FANZA|一般（DMM.com）かアダルト（FANZA）か|
|サービス|service|digital|フロアAPIから取得できるサービスコードを指定|
|フロア|floor|videoa|フロアAPIから取得できるフロアコードを指定|
|取得件数|hits|20|初期値：20 最大：100|
|検索開始位置|offset|1|初期値：1 最大：50000|
|ソート順|sort|rank|初期値：rank<br>人気：rank<br>価格が高い：pric<br>価格が安い順：-price<br>新着：date<br>評価：review|
|キーワード|keyword|上原亜衣|UTF-8で指定|
|商品ID|cid|15dss00145|商品に振られているcontent_id
|絞りこみ項目|article|actress|女優：actress<br>作者：author<br>ジャンル：genre<br>シリーズ：series<br>メーカー：maker
|絞り込みID|article_id|1011199|上記絞り込み項目のID(各検索APIから取得可能)|
|発売日絞り込み|gte_date|2016-04-01T00:00:00|このパラメータで指定した日付以降に発売された商品を絞り込むことができます。ISO8601形式でフォーマットした日付を指定してください。(ただし、タイムゾーンは指定できません)
|在庫絞り込み|mono_stock|mono|初期値：絞り込みなし<br>在庫あり：stock<br>予約受付中：reserve<br>DMM通販のみ：mono<br>マーケットプレイスのみ：dmp<br>※通販サービスのみ指定可能
|出力形式|output|json|json / xml|
|コールバック|callback|callback|出力形式jsonで指定した場合に、このパラメータでコールバック関数名を指定すると、JSONP形式で出力されます

[APIリファレンス](https://affiliate.dmm.com/api/v3/itemlist.html)からの一部抜粋、改変済みの表となっています。必須パラメーターである`api_id`、`affiliate_id`はインスタンス作成時、`site`はデフォルトで'FANZA'に設定してあります。

## License
MIT    
https://github.com/0x0u/dmm_search3/blob/master/LICENSE.txt

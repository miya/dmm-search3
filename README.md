# dmm_search3
[![License](http://img.shields.io/badge/license-mit-blue.svg?style=flat)](https://github.com/0x0u/dmm/blob/master/LICENSE.txt)
[![Build Status](https://travis-ci.org/0x0u/dmm_search3.svg?branch=master)](https://travis-ci.org/0x0u/dmm_search3)
[![Requirements Status](https://requires.io/github/0x0u/dmm_search3/requirements.svg?branch=master)](https://requires.io/github/0x0u/dmm_search3/requirements/?branch=master)   

[DMM Webサービス](https://affiliate.dmm.com/api/)をPythonで扱うためのライブラリです。[コチラ](https://affiliate.dmm.com/api/regist_guide/)からアカウントを作成して、API IDとアフィリエイトIDを取得しておく必要があります。

## Install
pipでインストールします。
```
$ pip3 install dmm_search3
```

## Usage
モジュールのインポート
```Python
from dmm import DMM
```

取得したAPI IDとアフィリエイトIDをセット
```Python
api_id = 'your_api_id'
affiliate_id = 'your_affiliate_id'
```

インスタンスの作成
```Python
dmm = DMM(api_id=api_id, affiliate_id=affiliate_id)
```

検索メソッド(search)
```Python
dmm.search('物理名', keyword引数='')
```

searchメソッドの第一引数

|論理名|物理名|
|:--:|:--:|
|商品検索|ItemList|
|フロア検索|FloorList|
|女優検索|ActressSearch|
|ジャンル検索|GenreSearch|
|メーカー検索|MakerSearch|
|シリーズ検索|SeriesSearch|
|作者検索|AuthorSearch|

検索メソッドの第一引数は上記のいずれかの物理名を指定します。第二引数以降はキーワード引数で([APIリファレンス](https://affiliate.dmm.com/api/v3/itemlist.html))のリクエストパラメータを指定します。引数に値を渡す場合は明示的にキーワードを指定しないとエラーが発生します。  

```Python
dmm.search('ItemsList', keyword='バレンタイン', hits=5, offset=10, sort='review')
```

商品検索リクエストパラメーター引用

|論理名|物理名|必須|値のサンプル|概要|
|:--:|:--:|:--:|:--:|:--:|
|APIID|api_id|○||登録時に割り振られたID|
|アフィリエイトID|affiliate_id|○|affiliate-990|登録時に割り振られた990|
|サイト|site|○|FANZA|一般（DMM.com）かアダルト（FANZA）か|
|サービス|service||digital|フロアAPIから取得できるサービスコードを指定|
|フロア|floor||videoa|フロアAPIから取得できるフロアコードを指定|
|取得件数|hits||20|初期値：20 最大：100|
|検索開始位置|offset||1|初期値：1 最大：50000|
|ソート順|sort||rank|初期値：rank人気：rank価格が高い：pric価格が安い順：-price新着：date評価：review|
|キーワード|keyword||上原亜衣|UTF-8で指定|
|商品ID|cid||15dss00145|商品に振られているcontent_id
|絞りこみ項目|article||actress|女優：actress 作者：author ジャンル：genre シリーズ：series メーカー：maker
|絞り込みID|article_id||1011199|上記絞り込み項目のID(各検索APIから取得可能)|
|発売日絞り込み|gte_date||2016-04-01T00:00:00|このパラメータで指定した日付以降に発売された商品を絞り込むことができます。ISO8601形式でフォーマットした日付を指定してください。(ただし、タイムゾーンは指定できません)
|在庫絞り込み|mono_stock||mono|初期値：絞り込みなし 在庫あり：stock 予約受付中：reserve DMM通販のみ：mono マーケットプレイスのみ：dmp ※通販サービスのみ指定可能
|出力形式|output||json|json / xml|
|コールバック|callback||callback|出力形式jsonで指定した場合に、このパラメータでコールバック関数名を指定すると、JSONP形式で出力されます

商品検索の例
```Python
items = dmm.search('ItemList', keyword='バレンタイン' , hits=9, )
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

商品検索のレスポンスフィールド引用

|フィールド|説明|例|
|:--:|:--:|:--:|
|request|||
|　└ parameter|リクエストパラメータ||
|　　├ name|パラメーター名|site|
|　　└ value|値|FANZA|
|result|||
|　├ status|ステータスコード|200|
|　├ result_count|取得件数|20|
|　├ total_count|全体件数|150627|
|　├ first_position|検索開始位置|1|
|　├ items|商品情報||
|　├ service_code|サービスコード|digital|
|　├ service_name|サービス名|動画|
|　├ floor_code|フロアコード|videoa|
|　├ floor_name|フロア名|ビデオ|
|　├ category_name|カテゴリ名|ビデオ(動画)|
|　├ content_id|商品ID|15dss00145|
|　├ product_id|品番|15dss00145|
|　├ title|タイトル|GET！！素人ナンパ Best100！！街角女子ベスト100人 8時間
|　├ volume|収録時間 or ページ数|350|
|　├ number|巻数|3|
|　├ review|レビュー平均点||
|　　├ count|レビュー数|8|
|　　└ average|レビュー平均点|3.13|
|　├ URL|商品ページURL|http://www.dmm.co.jp/digital/videoa/-/detail/=/cid=15dss00145/
|　├ affiliateURL|アフィリエイトリンクURL|http://www.dmm.co.jp/digital/videoa/-/detail/=/cid=15dss00145/affiliate-990
|　├ URLsp|スマホ向け商品ページURL|http://www.dmm.co.jp/digital/videoa/-/detail/=/cid=15dss00145/
|　├ affiliateURLsp|スマホ向けアフィリエイトリンクURL|http://www.dmm.co.jp/digital/videoa/-/detail/=/cid=15dss00145/affiliate-990
|　├ imageURL|画像URL||
|　　├ list|リストページ用|http://pics.dmm.co.jp/digital/video/15dss00145/15dss00145pt.jpg
|　　├ small|末端用（小）|http://pics.dmm.co.jp/digital/video/15dss00145/15dss00145ps.jpg
|　　└ large|末端用（大）|http://pics.dmm.co.jp/digital/video/15dss00145/15dss00145pl.jpg
|　├ tachiyomi|||
|　　├ URL|立ち読みページURL|http://book.dmm.co.jp/tachiyomi/?product_id=b468acown00017&item_id=b468acown00017&shop=digital_book
|　　└ affilaiteURL|立ち読みアフィリエイトリンクURL|http://book.dmm.co.jp/tachiyomi/?product_id=b468acown00017&item_id=b468acown00017&shop=digital_book/affiliate-990
|　├ sampleImageURL|サンプル画像URL||
|　　├ sample_s|サンプル（小）リスト||
|　　　 └ image|サンプル画像（小）|http://pics.dmm.co.jp/digital/video/15dss00145/15dss00145-1.jpg
|　├ sampleMovieURL|サンプル動画URL||
|　　├ size_476_306|476×306|http://www.dmm.co.jp/litevideo/-/part/=/cid=15dss145/size=476_306/
|　　├ size_560_360|560×360|http://www.dmm.co.jp/litevideo/-/part/=/cid=15dss145/size=560_360/
|　　├ size_644_414|644×414|http://www.dmm.co.jp/litevideo/-/part/=/cid=15dss145/size=644_414/
|　　├ size_720_480|720×480|http://www.dmm.co.jp/litevideo/-/part/=/cid=15dss145/size=720_480/
|　　├ pc_flag|PC対応しているか|1
|　　└ sp_flag|スマホ対応しているか|1
|　├ prices|価格||
|　　├ price|金額|300～|
|　　├ list_price|定価||
|　　└ deliveries|配信リスト||
|　　　└ delivery|配信||
|　　　　├ type|配信タイプ|stream
|　　　　└ price|配信価格|300
|　├ date|発売日、配信開始日、貸出開始日|2012/8/3 10:00
|　├ iteminfo|商品詳細||
|　　├ genre|ジャンル||
|　　　├ name|ジャンル名|ベスト・総集編
|　　　└ id|ジャンルID|6003
|　　├ series|シリーズ||
|　　　├ name|シリーズ名|ETシリーズ
|　　　└ id|シリーズID|1006
|　　├ maker|メーカー||
|　　　├ name|メーカー名|桃太郎映像出版
|　　　└ id|メーカーID|40016
|　　├ actor|出演者（一般作品のみ）||
|　　　├ name|出演者名||
|　　　└ id|出演者ID||
|　　├actress|女優（アダルト作品のみ）||
|　　　├ name|女優名|小澤マリア
|　　　└ id|女優ID|15187
|　　├ director|監督||
|　　　├ name|監督名||
|　　　└ id|監督ID||
|　　├ author|作家、原作者、著者||
|　　　├ name|作家、原作者、著者名||
|　　　└ id|作家、原作者、著者ID||
|　　├ label|レーベル||
|　　　└ id|レーベルID|76
|　├ jancode|JANコード||
|　├ maker_product|メーカー品番||
|　├ isbn|ISBN||
|　└ stock|在庫状況||
|　　　└ id|作家、原作者、著者ID|241046
|　　├ label|レーベル||
|　　　├ name|レーベル名|ワーナー・ホーム・ビデオ
|　　　└ id|レーベルID|60016|
|　　├ type|タイプ||
|　　　├ name|タイプ名||
|　　　└ id|タイプID||
|　　├ color|カラー||
|　　　├ name|カラー名||
|　　　└ id|カラーID||
|　　└ size|サイズ||
|　　　├ name|サイズ名||
|　　　└ id|サイズID||
|　├ bandaiinfo|バンダイch情報||
|　　└ titlecode|作品コード||
|　├ cdinfo|CD情報||
|　　└ kind|アルバム、シングル||
|　├ jancode|JANコード|4988135965905|
|　├ maker_product|メーカー品番|10003-54653|
|　├ isbn|ISBN||
|　└ stock	在庫状況|reserve|||

## License
MIT    
https://github.com/0x0u/dmm_search3/blob/master/LICENSE.txt

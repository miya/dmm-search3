# dmm_search3

[![License](http://img.shields.io/badge/license-mit-blue.svg?style=flat)](https://github.com/0x0u/dmm/blob/master/LICENSE.txt)
[![Build Status](https://travis-ci.org/0x0u/dmm_search3.svg?branch=master)](https://travis-ci.org/0x0u/dmm_search3)
[![Requirements Status](https://requires.io/github/0x0u/dmm_search3/requirements.svg?branch=master)](https://requires.io/github/0x0u/dmm_search3/requirements/?branch=master)  

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

検索メソッドの第一引数は、ItemList(商品検索)、FloorList(フロア検索)、ActressSearch(女優検索)、GenreSearch(ジャンル検索)、MakerSearch(メーカー検索)、SeriesSearch(シリーズ検索)、AuthorSearch(作者検索)のいずれかを指定します。第二引数以降は[APIリファレンス](https://affiliate.dmm.com/api/v3/itemlist.html)のリクエストパラメータを指定します。可変長引数で受け取るので、`keyword='バレンタイン'`のように明示的にキーワードと値を指定します。必須パラメーターである`api_id`、`affiliate_id`はインスタンス作成時、`site`はデフォルトで'FANZA'に設定してあります。

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
DMM.sample_download(cid='1vandr00069', fname='sample')
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
## License
MIT    
https://github.com/0x0u/dmm_search3/blob/master/LICENSE.txt

# dmm_search3

[![License](http://img.shields.io/badge/license-mit-blue.svg?style=flat)](https://github.com/miya/dmm_search3/blob/master/LICENSE.txt)
![](https://github.com/miya/dmm_search3/workflows/workflow/badge.svg)

DMM Web API Version 3.0 Wrapper for Python3

## Requirements
Please get it [here](https://affiliate.dmm.com/api/guide/).

* api_id
* affiliate_id

## Install  
```
$ pip3 install dmm_search3
```

## Initialize
```python
# モジュールのインポート
import dmm

# API ID と アフィリエイトIDをセット
api_id = "your_api_id"
affiliate_id = "your_affiliate_id"

# インスタンスの作成
api = dmm.API(api_id=api_id, affiliate_id=affiliate_id)
```

## Feature
```python
#商品検索
item_search = api.item_search(site="FANZA", hits=1, keyword="バレンタイン")

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
author_search = api.author_search(floor_id=91)

# サンプル動画ドウンロード
dmm.sample_download(cid="abgktk_0012", fname="sample", size="big")
```

## Sample
Please refer [here](https://github.com/miya/dmm_search3/blob/master/test.py).

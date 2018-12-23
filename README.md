# dmm_search3
[![License](http://img.shields.io/badge/license-mit-blue.svg?style=flat)](https://github.com/0x0u/dmm/blob/master/LICENSE.txt)
[![Build Status](https://travis-ci.org/0x0u/dmm_search3.svg?branch=master)](https://travis-ci.org/0x0u/dmm_search3)
[![Requirements Status](https://requires.io/github/0x0u/dmm_search3/requirements.svg?branch=master)](https://requires.io/github/0x0u/dmm_search3/requirements/?branch=master)   

[DMM Webサービス](https://affiliate.dmm.com/api/)をPythonで扱うためのライブラリです。[コチラ](https://affiliate.dmm.com/api/regist_guide/)からアカウントを作成して、API IDとアフィリエイトIDを取得しておく必要があります。

## Install
pipでインストールします。
```
pip3 install dmm_search3

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

商品検索メソッド
```Python
item = dmm.item_search(keyword='バレンタイン')
for i in item:
   print(i)
```

メソッドは商品(item)、女優(actress)、ジャンル(genre)、メーカー
(maker)、シリーズ(series)、作者(author)検索があります。

```Python
dmm.<対象>_search(引数)
```

引数は([APIリファレンス](https://affiliate.dmm.com/api/v3/itemlist.html))のリクエストパラメータを指定します。原則としてhits(データの取得件数)、offset(検索開始位置)、output(出力形式)はそれぞれ最大値である100、最小値である1、jsonでデフォルト引数として指定しています。

引数に値を渡す場合は明示的にキーワードを指定します。  

```Python
dmm.item_search(keyword='バレンタイン', hits=5, offset=10, sort='review')
```

## License
MIT    
https://github.com/0x0u/dmm_search3/blob/master/LICENSE.txt

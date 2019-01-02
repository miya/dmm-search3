#Travis CIの定期ビルド時に実行されるテスト用スクリプトです

import os
from dmm import DMM

# api_idとアフィリエイトIDをセット
api_id = os.environ.get('api_id')
affiliate_id = os.environ.get('affiliate_id')


#インスタンスを作成
dmm = DMM(api_id=api_id, affiliate_id=affiliate_id)

#検索メソッド

#商品検索API
item = dmm.search('ItemList', keyword='明日花キララ')

#フロアAPI
floor = dmm.search('floorList')

#女優検索API
actress = dmm.search('ActressSearch', keyword='明日花キララ')

#ジャンル検索API
genre = dmm.search('GenreSearch', keyword='明日花キララ')

#メーカー検索API
maker = dmm.search('MakerSearch', initial='あ')

#シリーズ検索API
series = dmm.search('SeriesSearch', initial='あ')

#作者検索API
author = dmm.search('AuthorSearch', initial='あ')


#サンプル動画ダウンロードメソッド
DMM.sample_download('ssni378')

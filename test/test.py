#Travis CIの定期ビルド時に実行されるテスト用スクリプトです

import os
from dmm import DMM

# api_idとアフィリエイトIDをセット
api_id = os.environ.get('api_id')
affiliate_id = os.environ.get('affiliate_id')

# インスタンスを作成
api = DMM(api_id=api_id, affiliate_id=affiliate_id)

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

#サンプル動画ドウンロード
dl_st = DMM.sample_download(cid='blor0018', fname='sample')
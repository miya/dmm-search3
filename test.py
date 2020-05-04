import os
import dmm

"""
api_idとaffiliate_idを取得してください: https://affiliate.dmm.com/api/regist_guide
api_id = "YOUR_API_ID"
affiliate_id = "YOUR_AFFILIATE_ID"
"""

api_id = os.environ.get("API_ID")
affiliate_id = os.environ.get("AFFILIATE_ID")

"""検索メソッド
各メソッドのパラメーター及びレスポンスは以下のURLを参照してください
商品検索: https://affiliate.dmm.com/api/v3/itemlist.html
フロア: https://affiliate.dmm.com/api/v3/floorlist.html
女優検索: https://affiliate.dmm.com/api/v3/actresssearch.html
ジャンル検索: https://affiliate.dmm.com/api/v3/genresearch.html
メーカー検索: https://affiliate.dmm.com/api/v3/makersearch.html
シリーズ検索: https://affiliate.dmm.com/api/v3/seriessearch.html
作者検索: https://affiliate.dmm.com/api/v3/authorsearch.html
"""

# インスタンスを作成
api = dmm.API(api_id=api_id, affiliate_id=affiliate_id)

# 商品検索
item_search = api.item_search(site="FANZA", hits=1, keyword="バレンタイン")

# フロア一覧
floor_list = api.floor_list()

# 女優検索
actress_search = api.actress_search()

# ジャンル検索
genre_search = api.genre_search(floor_id=91)

# メーカー検索
maker_search = api.maker_search(floor_id=91)

# シリーズ検索
series_search = api.series_search(floor_id=91)

# 作者検索
author = api.author_search(floor_id=72)

# 商品検索メソッドからcontent_idを抜き出し、サンプル動画をダウンロードする
items = api.item_search(site="FANZA", hits=10)
for i in items["result"]["items"]:
    cid = i.get("content_id")
    title = i.get("title")
    status = dmm.sample_download(content_id=cid)
    print(title, status)

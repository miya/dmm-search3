"""
The MIT License (MIT)

Copyright (c) dmm_search3.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import re
import requests
import youtube_dl
from bs4 import BeautifulSoup


class DMM:

    def __init__(self, api_id=None, affiliate_id=None):
        self.api_url = "https://api.dmm.com/affiliate/v3"
        self.api_id = api_id
        self.affiliate_id = affiliate_id

    def request(self, endpoint, kwargs):
        url = self.api_url + endpoint

        query = {
            "api_id": self.api_id,
            "affiliate_id": self.affiliate_id,
            "output": "json"
        }

        query.update(kwargs)

        return requests.get(url, params=query).json()

    def item_search(self, **kwargs):
        """商品検索

        Required parameters
        ---------
        site: str
            "FANZA" or "DMM.com"    

        Returns
        ---------
        dict
            商品情報がJSONで返ります。

        Docs
        ---------
        https://affiliate.dmm.com/api/v3/itemlist.html   
        """
        endpoint = "/ItemList"
        return self.request(endpoint, kwargs)

    def floor_list(self, **kwargs):
        """フロア一覧

        Returns
        ---------
        dict
            フロア一覧がJSONで返ります。

        Docs
        ---------
        https://affiliate.dmm.com/api/v3/floorlist.html
        """
        endpoint = "/FloorList"
        return self.request(endpoint, kwargs)

    def actress_search(self, **kwargs):
        """女優検索

        Returns
        ---------
        dict
            女優の情報がJSONで返ります。

        Docs
        ---------
        https://affiliate.dmm.com/api/v3/actresssearch.html
        """
        endpoint = "/ActressSearch"
        return self.request(endpoint, kwargs)

    def genre_search(self, **kwargs):
        """ジャンル検索

        Required parameters
        ---------
        floor_id: int
            フロア一覧から取得できるfloor_id 例: 91(VRch)
        
        Returns
        ---------
        dict
            ジャンル一覧がJSONで返ります。

        Docs
        ---------
        https://affiliate.dmm.com/api/v3/genresearch.html
        """
        endpoint = "/GenreSearch"
        return self.request(endpoint, kwargs)

    def maker_search(self, **kwargs):
        """メーカー検索

        Required parameters
        ---------
        floor_id: int
            フロア一覧から取得できるfloor_id 例: 91(VRch)

        Returns
        ---------
        dict
            メーカー一覧がJSONで返ります。 

        Docs
        ---------
        https://affiliate.dmm.com/api/v3/makersearch.html

        """
        endpoint = "/MakerSearch"
        return self.request(endpoint, kwargs)

    def series_search(self, **kwargs):
        """シリーズ検索

        Required parameters
        ---------
        floor_id: int
            フロア一覧から取得できるfloor_id 例: 91(VRch)
        
        Returns
        ---------
        dict
            シリーズ一覧がJSONで返ります。

        Docs
        ---------
        https://affiliate.dmm.com/api/v3/seriessearch.html
        """
        endpoint = "/SeriesSearch"
        return self.request(endpoint, kwargs)

    def author_search(self, **kwargs):
        """作者検索

        Required parameters
        ---------
        floor_id: int
            フロア一覧から取得できるfloor_id 例: 91(VRch) 

        Docs
        ---------
        https://affiliate.dmm.com/api/v3/authorsearch.html
        """
        endpoint = "AuthorSearch"
        return self.request(endpoint, kwargs)

    @classmethod
    def sample_download(cls, cid, fname=None, size="small"):
        """サンプル動画ダウンロード

        Required parameters
        ---------
        cid: str
            商品検索APIのcontent_id、商品ページから取得できる品番 例: blor00128

        Parameters
        ---------
        fname: str
            ファイル名

        size: str
            ダウンロードする動画の大きさを指定します。small(320x180) or big(720x404)

        Returns
        ---------
        dict
            requestsのステータスコードと動画ダウンロードの成否が返ります。
        """

        video_search_url = "https://www.dmm.co.jp/litevideo/-/detail/=/cid=" + cid
        r = requests.get(video_search_url)
        s = r.status_code

        if s == 200:
            soup = BeautifulSoup(r.text, "lxml")
            find_src = soup.find("iframe", allow="autoplay").get("src")
            tcid = re.findall("cid=(.*)/mtype", find_src)[0]

            if size == "small":  # 320 × 180
                video_url = "http://cc3001.dmm.co.jp/litevideo/freepv/{}/{}/{}/{}_sm_w.mp4".format(tcid[:1], tcid[:3], tcid, tcid)
            elif size == "big":  # 720 × 404
                video_url = "http://cc3001.dmm.co.jp/litevideo/freepv/{}/{}/{}/{}_dmb_w.mp4".format(tcid[:1], tcid[:3], tcid, tcid)

            r = requests.get(video_url)
            s = r.status_code

            if s == 200:
                if fname is None:
                    fname = cid

                ydl_opts = {
                    "outtmpl": fname + ".mp4",
                    "quiet": True,
                    "no_warnings": True
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([video_url])

                status = {"status": s, "message": "Download successful"}

            else:
                status = {"status": s, "message": "Download failed"}
        else:
            status = {"status": s, "message": "Not found"}

        return status

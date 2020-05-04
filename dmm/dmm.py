import re
import requests
import youtube_dl
from bs4 import BeautifulSoup


class API:

    def __init__(self, api_id=None, affiliate_id=None):
        self.api_url = "https://api.dmm.com/affiliate/v3"
        self.api_id = api_id
        self.affiliate_id = affiliate_id

    def _request(self, endpoint, kwargs):
        url = self.api_url + endpoint

        query = {
            "api_id": self.api_id,
            "affiliate_id": self.affiliate_id,
            "output": "json"
        }

        query.update(kwargs)

        return requests.get(url, params=query).json()

    def item_search(self, **kwargs):
        """
        商品検索

        Required parameters
        ---------
        site: str
            "FANZA" or "DMM.com"

        Returns
        ---------
        商品情報: dict

        Docs
        ---------
        https://affiliate.dmm.com/api/v3/itemlist.html   
        """
        endpoint = "/ItemList"
        return self._request(endpoint, kwargs)

    def floor_list(self, **kwargs):
        """
        フロア一覧

        Returns
        ---------
        フロア一覧: dict

        Docs
        ---------
        https://affiliate.dmm.com/api/v3/floorlist.html
        """
        endpoint = "/FloorList"
        return self._request(endpoint, kwargs)

    def actress_search(self, **kwargs):
        """
        女優検索

        Returns
        ---------
        女優情報: dict

        Docs
        ---------
        https://affiliate.dmm.com/api/v3/actresssearch.html
        """
        endpoint = "/ActressSearch"
        return self._request(endpoint, kwargs)

    def genre_search(self, **kwargs):
        """
        ジャンル検索

        Required parameters
        ---------
        floor_id: int
            フロア一覧から取得できるfloor_id 例: 91(VRch)
        
        Returns
        ---------
        ジャンル一覧: dict

        Docs
        ---------
        https://affiliate.dmm.com/api/v3/genresearch.html
        """
        endpoint = "/GenreSearch"
        return self._request(endpoint, kwargs)

    def maker_search(self, **kwargs):
        """
        メーカー検索

        Required parameters
        ---------
        floor_id: int
            フロア一覧から取得できるfloor_id 例: 91(VRch)

        Returns
        ---------
        メーカー一覧: dict

        Docs
        ---------
        https://affiliate.dmm.com/api/v3/makersearch.html

        """
        endpoint = "/MakerSearch"
        return self._request(endpoint, kwargs)

    def series_search(self, **kwargs):
        """
        シリーズ検索

        Required parameters
        ---------
        floor_id: int
            フロア一覧から取得できるfloor_id 例: 91(VRch)
        
        Returns
        ---------
        シリーズ一覧: dict

        Docs
        ---------
        https://affiliate.dmm.com/api/v3/seriessearch.html
        """
        endpoint = "/SeriesSearch"
        return self._request(endpoint, kwargs)

    def author_search(self, **kwargs):
        """
        作者検索

        Required parameters
        ---------
        floor_id: int
            フロア一覧から取得できるfloor_id 例: 91(VRch)

        Returns
        ---------
        作者一覧: dict

        Docs
        ---------
        https://affiliate.dmm.com/api/v3/authorsearch.html
        """
        endpoint = "AuthorSearch"
        return self._request(endpoint, kwargs)


def sample_download(content_id, file_name=None, size="small", download=True, **kwargs):
    """
    サンプル動画ダウンロード

    Parameters
    ----------
    content_id: str
        商品検索APIなどで取得できるcontent_id

    file_name: str
        保存する際のファイル名

    size: str
        動画のサイズ small: 320 × 180 or big: 720 × 404

    download: bool
        動画のダウンロードを行うか

    Returns
    -------
    requestsのステータスコード, ステータスメッセージ, サンプル動画のURL: dict
    """
    video_search_url = "https://www.dmm.co.jp/litevideo/-/detail/=/cid=" + content_id
    r = requests.get(video_search_url)
    s = r.status_code

    if s == 200:
        soup = BeautifulSoup(r.text, "lxml")
        find_src = soup.find("iframe", allow="autoplay").get("src")
        tcid = re.findall("cid=(.*)/mtype", find_src)[0]

        # 320 × 180
        small_video_url = "http://cc3001.dmm.co.jp/litevideo/freepv/{}/{}/{}/{}_sm_w.mp4".format(tcid[:1], tcid[:3], tcid, tcid)

        # 720 × 404
        big_video_url = "http://cc3001.dmm.co.jp/litevideo/freepv/{}/{}/{}/{}_dmb_w.mp4".format(tcid[:1], tcid[:3], tcid, tcid)

        if size == "small":
            video_url = small_video_url
        elif size == "big":
            video_url = big_video_url
        else:
            video_url = small_video_url

        r = requests.get(video_url)
        s = r.status_code

        if not download:
            if s == 200:
                status = {"status_code": s, "message": "This URL is valid", "download_url": video_url}
            else:
                status = {"status_code": s, "message": "This URL is invalid", "download_url": video_url}
            return status

        if s == 200:
            if file_name is None:
                file_name = content_id

            ydl_opts = {
                "outtmpl": file_name + ".mp4",
                "quiet": True,
                "no_warnings": True
            }
            ydl_opts.update(kwargs)

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])

            status = {"status_code": s, "message": "Download successful", "download_url": video_url}

        else:
            status = {"status_code": s, "message": "Download failed", "download_url": video_url}
    else:
        status = {"status_code": s, "message": "The video doesn't exist.", "download_url": ""}

    return status

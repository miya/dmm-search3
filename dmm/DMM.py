'''
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
'''

import re
import requests
import youtube_dl
from bs4 import BeautifulSoup

class DMM():
    '''初期化
    インスタンス変数にapi_idとaffiliate_idを代入
    '''
    def __init__(self, api_id, affiliate_id):
        self.api_id = api_id
        self.affiliate_id = affiliate_id

    '''検索メソッド
    第一引数でItemList、FloorList、ActressSearch、GenreSearch、MakerSearch、SeriesSearch、AuthorSearchのいずれかを指定
    第二引数以降はキーワード引数でDMM Web APIリファレンスのリクエストパラメーターを指定。
    urlに第一引数、第二引数移行をqueryに追加する。
    requestsでパラメーターにqueryを指定してgetリクエスト。
    '''
    def search(self, req, **key):
        url = 'https://api.dmm.com/affiliate/v3/{}?&site=FANZA'.format(req)
        query = {'api_id':self.api_id, 'affiliate_id':self.affiliate_id}
        query.update(key)
        data = requests.get(url, params=query).json()
        return data['result']

    '''サンプルダウンローダーメソッド
    content_idからサンプル動画をダウンロードするクラスメソッド。
    第一引数にcontent_idを指定、
    第二引数はファイル名を指定。第二引数を省略した場合はcontent_idがそのままファイル名になる。
    '''
    @classmethod
    def video_download(cls, cid, fname=None):
        url = 'https://www.dmm.co.jp/litevideo/-/detail/=/cid={}'.format(cid)
        req = requests.get(url)
        status = req.status_code
        if status == 200:
            soup = BeautifulSoup(req.text, 'html.parser')
            f = soup.find('iframe', allow="autoplay").get('src')
            r = re.search(r'cid=(.*)/mtype', f)
            if r != None:
                rcid = r.group(1)
            else:
                return 404
            # 320 × 180
            url2 = 'http://cc3001.dmm.co.jp/litevideo/freepv/{}/{}/{}/{}_sm_w.mp4'.format(rcid[:1], rcid[:3], rcid, rcid)
            # 720 × 404
            # url2 = 'http://cc3001.dmm.co.jp/litevideo/freepv/{}/{}/{}/{}_dmb_w.mp4'.format(rcid[:1], rcid[:3], rcid, rcid)
            req2 = requests.get(url2)
            status2 = req2.status_code
            if status2 == 200:
                if fname == None:
                    fname = cid
                ydl_opts = {
                    'outtmpl':fname + '.mp4',
                    'quiet':True
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url2])
                return status2
            else:
                return status2
        else:
            return status
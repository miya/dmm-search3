'''
The MIT License (MIT)

Copyright (c) 2015 bpyamasinn.

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

import requests

class DMM():
    def __init__(self, api_id, affiliate_id):
        self.api_id = api_id
        self.affiliate_id = affiliate_id

    def item_search(self, site='FANZA', service=None, floor=None, hits=100, offset=1, sort=None, keyword=None, cid=None, article=None, article_id=None, gte_date=None, lte_date=None, mono_stock=None, output=None, callback=None):
        url = 'https://api.dmm.com/affiliate/v3/ItemList?api_id=[APIID]&affiliate_id=[アフィリエイトID]&site=FANZA&service=digital&floor=videoa&hits=10&sort=date&keyword=%e4%b8%8a%e5%8e%9f%e4%ba%9c%e8%a1%a3&output=json'
        query = {
          'api_id':self.api_id,
          'affiliate_id':self.affiliate_id,
          'site':site,
          'service':service,
          'floor':floor,
          'hits':hits,
          'offset':offset,
          'sort':sort,
          'keyword':keyword,
          'cid':cid,
          'article':article,
          'article_id':article_id,
          'gte_date':gte_date,
          'lte_date':lte_date,
          'mono_stock':mono_stock,
          'output':output,
          'callback':callback
        }
        result = requests.get(url, params=query).json()['result']
        text = 'status: {}\nresult_count: {}\ntotal_count: {}\nfirst_position: {}\n'.format(result.get('status'), result.get('result_count'), result.get('total_count'), result.get('first_position'))
        print(text)
        return result['items']

    def floor_search(self, output=None, callback=None):
        url = 'https://api.dmm.com/affiliate/v3/FloorList?api_id=[APIID]&affiliate_id=[アフィリエイトID]&output=json&callback=example'
        query = {
          'api_id':self.api_id,
          'affiliate_id':self.affiliate_id,
          'output':output,
          'callback':callback
        }
        data = requests.get(url, params=query).json()
        return data

    def actress_search(self, site='FANZA', service=None, floor=None, hits=100, offset=1, sort=None, keyword=None, cid=None, article=None, article_id=None, gte_date=None, lte_date=None, mono_stock=None, output=None, callback=None):
        url = 'https://api.dmm.com/affiliate/v3/ActressSearch?api_id=[APIID]&affiliate_id=[アフィリエイトID]&keyword=%e3%81%82%e3%81%95%e3%81%bf&gte_bust=90&lte_waist=60&sort=-bust&hits=10&offset=10&output=json'
        query = {
          'api_id':self.api_id,
          'affiliate_id':self.affiliate_id,
          'site':site,
          'service':service,
          'floor':floor,
          'hits':hits,
          'offset':offset,
          'sort':sort,
          'keyword':keyword,
          'cid':cid,
          'article':article,
          'article_id':article_id,
          'gte_date':gte_date,
          'lte_date':lte_date,
          'mono_stock':mono_stock,
          'output':output,
          'callback':callback
        }
        result = requests.get(url, params=query).json()['result']
        text = 'status: {}\nresult_count: {}\ntotal_count: {}\nfirst_position: {}\n'.format(result.get('status'), result.get('result_count'), result.get('total_count'), result.get('first_position'))
        print(text)
        return result['actress']

    def genre_search(self, floor_id=None, initial=None, hits=100, offset=1, output=None, callback=None):
        url = 'https://api.dmm.com/affiliate/v3/GenreSearch?api_id=[APIID]&affiliate_id=[アフィリエイトID]&initial=%e3%81%8d&floor_id=25&hits=10&offset=10&output=json'
        query = {
        'api_id':self.api_id,
        'affiliate_id':self.affiliate_id,
        'floor_id':floor_id,
        'initial':initial,
        'hits':hits,
        'offset':offset,
        'output':output,
        'callback':callback
        }
        result = requests.get(url, params=query).json()['result']
        text = 'status: {}\nresult_count: {}\ntotal_count: {}\nfirst_position: {}\n'.format(result.get('status'), result.get('result_count'), result.get('total_count'), result.get('first_position'))
        print(text)
        return result['genre']

    def maker_search(self, floor_id=None, initial=None, hits=100, offset=1, output=None, callback=None):
        url = 'https://api.dmm.com/affiliate/v3/MakerSearch?api_id=[APIID]&affiliate_id=[アフィリエイトID]&floor_id=43&hits=10&offset=100&output=json'
        query = {
        'api_id':self.api_id,
        'affiliate_id':self.affiliate_id,
        'floor_id':floor_id,
        'initial':initial,
        'hits':hits,
        'offset':offset,
        'output':output,
        'callback':callback
        }
        result = requests.get(url, params=query).json()['result']
        text = 'status: {}\nresult_count: {}\ntotal_count: {}\nfirst_position: {}\n'.format(result.get('status'), result.get('result_count'), result.get('total_count'), result.get('first_position'))
        print(text)
        return result['maker']

    def series_search(self, floor_id=None, initial=None, hits=100, offset=1, output=None, callback=None):
        url = 'https://api.dmm.com/affiliate/v3/SeriesSearch?api_id=[APIID]&affiliate_id=[アフィリエイトID]&initial=%e3%81%8a&floor_id=27&hits=10&output=json'
        query = {
        'api_id':self.api_id,
        'affiliate_id':self.affiliate_id,
        'floor_id':floor_id,
        'initial':initial,
        'hits':hits,
        'offset':offset,
        'output':output,
        'callback':callback
        }
        result = requests.get(url, params=query).json()['result']
        text = 'status: {}\nresult_count: {}\ntotal_count: {}\nfirst_position: {}\n'.format(result.get('status'), result.get('result_count'), result.get('total_count'), result.get('first_position'))
        print(text)
        return result['series']

    def author_search(self, floor_id=None, initial=None, hits=100, offset=1, output=None, callback=None):
        url = 'https://api.dmm.com/affiliate/v3/AuthorSearch?api_id=[APIID]&affiliate_id=[アフィリエイトID]&iniital=%e3%81%86&floor_id=27&hits=10&output=json'
        query = {
        'api_id':self.api_id,
        'affiliate_id':self.affiliate_id,
        'floor_id':floor_id,
        'initial':initial,
        'hits':hits,
        'offset':offset,
        'output':output,
        'callback':callback
        }
        result = requests.get(url, params=query).json()['result']
        text = 'status: {}\nresult_count: {}\ntotal_count: {}\nfirst_position: {}\n'.format(result.get('status'), result.get('result_count'), result.get('total_count'), result.get('first_position'))
        print(text)
        return result['author']

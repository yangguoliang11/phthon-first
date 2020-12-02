# -*- encoding: utf-8 -*-
"""
@File    : wechat_spider.py
@Time    : 2020/7/1 9:02 上午
@Author  :
@Software: PyCharm
"""

import json
import time
import requests
import re
import random


class Spider(object):
    def __init__(self, req_host):
        self.req_host = req_host

    def getPublicList(self):
        url = self.req_host + "/python/getPublicList"
        res = requests.get(url=url).json()
        print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
        print("getPublicList res获取到的是:",res)
        if res.get("code") == "0000":
            return True, res.get("result")
        return False, res.get("msg")

    def getParameter(self, publicId):
        url = self.req_host + "/python/getParameter?publicNumberId=" + str(publicId)
        res = requests.get(url=url).json()
        print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
        print("getParameter res获取到的是:",res)
        if res.get("code") == "0000":
            return True, res.get("result")
        return False, res.get("msg")

    def get_content(self, publicName, publicId):
        status, res = self.getParameter(publicId)
        if not status:
            time.sleep(2)
        else:
            appmsg_token = res.get("clientToken")
            cookie = res.get("mpCookie")
            b_cookie = res.get("clientCookie")
            # 公众号主页
            url = 'https://mp.weixin.qq.com'
            header = {
                "HOST": "mp.weixin.qq.com",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36"
            }
            cookies = {"Cookie": cookie}
            response = requests.get(url=url, cookies=cookies)
            token = re.findall(r'token=(\d+)', str(response.url))[0]
            # 搜索微信公众号的接口地址
            search_url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?'
            query_id = {
                'action': 'search_biz',
                'token': token,
                'lang': 'zh_CN',
                'f': 'json',
                'ajax': '1',
                'random': random.random(),
                'query': publicName,
                'begin': '0',
                'count': '5'
            }
            search_response = requests.get(search_url, cookies=cookies, headers=header, params=query_id)
            # 取搜索结果中的第一个公众号
            lists = search_response.json().get('list')[0]
            # 获取这个公众号的fakeid，后面爬取公众号文章需要此字段
            fakeid = lists.get('fakeid')

            # 微信公众号文章接口地址
            appmsg_url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?'
            query_id_data = {
                'token': token,
                'lang': 'zh_CN',
                'f': 'json',
                'ajax': '1',
                'random': random.random(),
                'action': 'list_ex',
                'begin': '0',
                'count': '5',
                'query': '',
                'fakeid': fakeid,
                'type': '9'
            }
            # 打开搜索的微信公众号文章列表页
            appmsg_response = requests.get(appmsg_url, cookies=cookies, headers=header, params=query_id_data)
            max_num = appmsg_response.json().get('app_msg_cnt')
            print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
            print('文章总数:', max_num)
            # 每页至少有5条，获取文章总的页数，爬取时需要分页爬
            num = int(int(max_num) / 5)
            # num = 10
            # 起始页begin参数，往后每页加5
            begin = 0
            while num + 1 > 0:
                query_id_data = {
                    'token': token,
                    'lang': 'zh_CN',
                    'f': 'json',
                    'ajax': '1',
                    'random': random.random(),
                    'action': 'list_ex',
                    'begin': '{}'.format(str(begin)),
                    'count': '5',
                    'query': '',
                    'fakeid': fakeid,
                    'type': '9'
                }
                print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
                print('正在翻页：--------------获取篇数:', begin)

                query_fakeid_response = requests.get(appmsg_url, cookies=cookies, headers=header, params=query_id_data)
                fakeid_list = query_fakeid_response.json().get('app_msg_list')
                print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
                print('收集到的fakeid_list:', fakeid_list)
                doc_list = list()
                for item in fakeid_list:
                    content_link = item.get('link')
                    content_title = item.get('title')
                    create_time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(item.get('create_time')))
                    appmsgid = item.get('appmsgid')
                    itemidx = item.get('itemidx')
                    read_num, like_num, old_like_num = self.get_read_num(content_link, b_cookie, appmsg_token)
                    doc = dict()
                    doc["like_num"] = like_num
                    doc["title"] = content_title
                    doc["create_time"] = create_time
                    doc["appmsgid"] = appmsgid
                    doc["itemidx"] = itemidx
                    doc["read_num"] = read_num
                    doc["url"] = content_link
                    doc["old_like_num"] = old_like_num
                    doc_list.append(doc)
                self.savePythonData(publicId, doc_list)

                num -= 1
                begin = int(begin)
                begin += 5
                # 经测试一分钟之内爬取20条以上会被封大概5分钟
                time.sleep(30)
            return

    def get_read_num(self, url, cookie, appmsg_token):
        headers = {
            "Cookie": cookie,
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) MicroMessenger/6.8.0(0x16080000) MacWechat/2.4.1(0x12040110) Chrome/39.0.2171.95 Safari/537.36 NetType/WIFI WindowsWechat MicroMessenger/6.8.0(0x16080000) MacWechat/2.4.1(0x12040110) Chrome/39.0.2171.95 Safari/537.36 NetType/WIFI WindowsWechat MicroMessenger/6.8.0(0x16080000) MacWechat/2.4.1(0x12040110) Chrome/39.0.2171.95 Safari/537.36 NetType/WIFI WindowsWechat"
        }
        your__biz = url.split("&")[0].split("__biz=")[1]
        article_mid = url.split("&")[1].split("=")[1]
        article_sn = url.split("&")[3].split("=")[1]
        article_idx = url.split("&")[2].split("=")[1]
        data = {
            "is_only_read": "1",
            "is_temp_url": "0",
            "appmsg_type": "9",
        }
        origin_url = "http://mp.weixin.qq.com/mp/getappmsgext?"
        appmsgext_url = origin_url + "__biz={}&mid={}&sn={}&idx={}&appmsg_token={}&x5=1".format(your__biz, article_mid, article_sn, article_idx, appmsg_token)
        content = requests.post(appmsgext_url, headers=headers, data=data).json()
        print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
        print('收集到的content:', content)
        if not content.get("appmsgstat"):
            read_num = 0
            like_num = 0
            old_like_num = 0
        else:
            read_num = content["appmsgstat"]["read_num"]
            like_num = content["appmsgstat"]["like_num"]
            old_like_num = content["appmsgstat"]["old_like_num"]
        return read_num, like_num, old_like_num

    def savePythonData(self, publicId, formData):
        url = self.req_host + "/python/savePythonData"
        data = dict()
        data["publicId"] = publicId
        data["jsonArray"] = json.dumps(formData)
        print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
        print('收集到的data:', data)
        res = requests.post(url=url, data=data)
        return res

    def start_spider(self):
        status, res_list = self.getPublicList()
        if not status or len(res_list) == 0:
            time.sleep(2)
        else:
            for res in res_list:
                publicId = res.get("publicId")
                publicName = res.get("publicName")
                print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
                print('publicName:', publicName)
                self.get_content(publicName, publicId)


def main(host):
    try:
        spider = Spider(host)
        spider.start_spider()
    except Exception as err:
        print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
        print("error is : %s" % err)


if __name__ == '__main__':
    #host = "http://zhongk-admin.jvtdtest.top/admin"
    host = "https://zhongk-admin.yunpaas.cn/admin"
    main(host)

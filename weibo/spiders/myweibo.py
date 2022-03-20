import random
import scrapy
import json

import weibo.items
from weibo.timer import TimeFormatTransform
from weibo.geo import getgeo
import paramiko
import time
class MyweiboSpider(scrapy.Spider):
    name = 'myweibo'
    allowed_domains = ['m.weibo.cn']
    page=1
    count=0
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname='114.104.210.66', port=20402, username='root', password='nU8tW3tT2uN3')

    cookies=[{

                "_T_WM": "68333456070",
                "M_WEIBOCN_PARAMS": "luicode=20000174&uicode=20000174",
                "MLOGIN": "1",
                "SUB": "_2A25PMGGZDeRhGeFJ71QX9CvIzzuIHXVs2w_RrDV6PUJbkdANLRHXkW1Nf8flhCqiJJKxTxdSFyGzkJtHkeIdKHjo",
                "WEIBOCN_FROM": "1110006030",
                "XSRF-TOKEN": "7bc8d0"
},
        {


                    "_T_WM": "62055704070",
                    "loginScene": "102003",
                    "M_WEIBOCN_PARAMS": "luicode=20000174&uicode=20000174",
                    "MLOGIN": "1",
                    "SUB": "_2A25PM2V1DeRhGeBI4lAU8y_Ezz6IHXVs3As9rDV6PUJbkdCOLWrhkW1NRn2D3UDINlR8injHkeD83eHYvYGUalfx",
                    "WEIBOCN_FROM": "1110006030",
                    "XSRF-TOKEN": "ce3b22"

        },


        {
                    "_T_WM": "49438419208",
                    "loginScene": "102003",
                    "M_WEIBOCN_PARAMS": "lfid=102803&luicode=20000174&uicode=20000174",
                    "MLOGIN": "1",
                    "SUB": "_2A25PM2Z9DeRhGeFJ71QX9CvIzzuIHXVs3Ao1rDV6PUJbkdAKLW6mkW1Nf8flhGIGO3GekwolB1yno27Siz8C4-0E",
                    "WEIBOCN_FROM": "1110006030",
                    "XSRF-TOKEN": "ed3dc3"
        }
        ,
        {

                "_T_WM": "35541879483",
                "loginScene": "102003",
                "M_WEIBOCN_PARAMS": "luicode=20000174&uicode=20000174",
                "MLOGIN": "1",
                "SUB": "_2A25PMGGZDeRhGeFJ71QX9CvIzzuIHXVs2w_RrDV6PUJbkdANLRHXkW1Nf8flhCqiJJKxTxdSFyGzkJtHkeIdKHjo",
                "WEIBOCN_FROM": "1110006030",
                "XSRF-TOKEN": "72473a"

        }
    ]
    headers = [
        {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1'},
        {
            'User-Agent': 'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1'},
        {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3'},
        {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3'},
        {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3'},
        {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'},
        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'}
    ]
    start_urls = ['https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D60%26q%3D%23%E5%90%89%E6%9E%97%E5%86%9C%E4%B8%9A%E7%A7%91%E6%8A%80%E5%AD%A6%E9%99%A2%E7%96%AB%E6%83%85%23%26t%3D10&extparam=%23%E5%90%89%E6%9E%97%E5%86%9C%E4%B8%9A%E7%A7%91%E6%8A%80%E5%AD%A6%E9%99%A2%E7%96%AB%E6%83%85%23&luicode=10000011&lfid=100103type%3D38%26q%3D%E5%90%89%E6%9E%97%E5%86%9C%E4%B8%9A%E7%A7%91%E6%8A%80%E5%AD%A6%E9%99%A2%E7%96%AB%E6%83%85%26t%3D0&page_type=searchall']
    def changeip(self):
        print('到点了，定时换号ip')
        stdin, stdout, stderr = self.client.exec_command('pppoe-stop')
        stdin, stdout, stderr = self.client.exec_command('pppoe-start')
        time.sleep(15)

    def parse(self, response):
        self.page = self.page + 1
        body = json.loads(response.text,strict=False)
        data = body.get('data')
        title=data.get('cardlistInfo').get('title_top').strip('-').strip('#')
        header = random.choice(self.headers)
        cookie = random.choice(self.cookies)
        if not 'msg' in body:
            cards = data.get('cards')
            for i in cards:
                mblog = None
                if 'card_group' in i and i.get('card_group') != None:
                    card_group = i.get('card_group')
                    if 'mblog' in card_group:
                        mblog = card_group[0].get('mblog')
                elif 'mblog' in i and i.get('mblog') != None:
                    mblog = i.get('mblog')
                if mblog != None:
                    id = mblog.get('id')
                    username = mblog.get('user').get('screen_name')
                    user_id = mblog.get('user').get('id')
                    time = TimeFormatTransform(mblog.get('created_at'))
                    # text = mblog.get('text')
                    # with open('page/' + response.meta.get("key") + '.txt', 'a', encoding='utf-8') as f:
                    #     f.write('\t' + ' 用户名: ' + username + ' 用户id: ' + str(
                    #         user_id) + ' 评论时间' + time + ' 评论内容: ' + text + '\n' * 2)
                    comment_url = 'https://m.weibo.cn/comments/hotflow?id=' + str(id) + '&mid=' + str(
                        id) + '&max_id_type=0'
                    yield scrapy.Request(url=comment_url, headers=header, cookies=cookie, callback=self.comment_parse,
                                         meta={'url': comment_url, 'key':title})
            url = self.start_urls[0] + '&page=' + str(self.page)
            yield scrapy.Request(url=url, headers=header, cookies=cookie, callback=self.parse)
        else:
            self.crawler.engine.close_spider(self,"到底了!")
    def comment_parse(self, response):
        body = json.loads(response.text,strict=False)
        item=weibo.items.WeiboItem()
        header = random.choice(self.headers)
        cookie = random.choice(self.cookies)
        stdin, stdout, stderr = self.client.exec_command(
            'ifconfig  ppp0 | awk \'{print $2}\'|awk "NR==2"')
        result = stdout.read().decode('utf-8')
        ip = {'http': result + ':8888'}
        if body.get('ok') == 1:
            datas = body.get('data')
            data = datas.get('data')
            max_id = datas.get('max_id')
            url = response.meta.get('url') + '&max_id=' + str(max_id)
            for t in data:
                self.count=self.count+1
                if self.count % 1500==0:
                    self.changeip()
                else:
                    user = t.get('user')
                    time = TimeFormatTransform(t.get('created_at'))
                    if t.get('text')!='转发微博':
                        text = t.get('text')
                    else:
                        self.count=self.count-1
                        continue
                    userid = user.get('id')
                    username = user.get('screen_name')
                    geourl = 'https://weibo.com/ajax/profile/info?uid=' + str(userid)
                    userlocation=getgeo(headers=self.headers,cookies=self.cookies,id=userid,ip=ip)
                    item['USERNAME']=username
                    item['USERID']=str(userid)
                    item['LOCATION']= userlocation
                    item['TIME'] = time
                    item['TEXT'] = text
                    yield item
            yield scrapy.Request(url=url, headers=header, cookies=cookie, callback=self.comment_parse, meta=response.meta)















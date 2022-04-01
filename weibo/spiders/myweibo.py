import random
import scrapy
import json


from pydispatch import dispatcher
from scrapy import signals
from scrapy.signalmanager import SignalManager
import weibo.items
from weibo.timer import TimeFormatTransform
from weibo.geo import getgeo
from weibo.ipgeo import getipgeo
from weibo.middlewares import ip_pools
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
    start_urls=['']
    def __init__(self):
        with open('starturls.txt','r') as f:
            self.start_urls[0]=f.read().replace('search?containerid=231522type%3D1%26t%3D10','api/container/getIndex?containerid=231522type%3D60')
        SignalManager(dispatcher.Any).connect(
            self.close, signal=signals.spider_closed)

        # 退出函数
    ip_pools=[]
    cookies=[

        {

                "_T_WM": "28752832714",
                "loginScene": "102003",
                "M_WEIBOCN_PARAMS": "lfid=102803&luicode=20000174&uicode=20000174",
                "MLOGIN": "1",
                "SUB": "_2A25PQqY-DeRhGeBI4lAU8y_Ezz6IHXVszMp2rDV6PUJbkdAKLRbMkW1NRn2D3UGs5MLqArRSP56GDkA7B2sPTC5C",
                "WEIBOCN_FROM": "1110006030",
                "XSRF-TOKEN": "4f68ae"

        }
        ,
        {
                "_T_WM": "37249435170",
                "loginScene": "102003",
                "M_WEIBOCN_PARAMS": "lfid=102803&luicode=20000174&uicode=20000174",
                "MLOGIN": "1",
                "SUB": "_2A25PQqa7DeRhGeFJ71QX9CvIzzuIHXVszMrzrDV6PUJbkdANLUTskW1Nf8flhF68C0DkliHzAPyYsze1ae6KXeqZ",
                "WEIBOCN_FROM": "1110006030",
                "XSRF-TOKEN": "c4cb9c"

        },
        {
                "_T_WM": "48231368342",
                "loginScene": "102003",
                "M_WEIBOCN_PARAMS": "lfid=102803&luicode=20000174&uicode=20000174",
                "MLOGIN": "1",
                "SUB": "_2A25PQqiwDeRhGeBI4lAU8y_Ezz6IHXVszMj4rDV6PUJbkdB-LWPbkW1NRn2D3VfSTZ0xZjZsUJBkvMTzLuURR8OM",
                "WEIBOCN_FROM": "1110006030",
                "XSRF-TOKEN": "ee7a36"

        },
        {
                "_T_WM": "81983068356",
                "loginScene": "102003",
                "M_WEIBOCN_PARAMS": "oid=4752052762970858&lfid=102803&luicode=20000174&uicode=20000174",
                "MLOGIN": "1",
                "SUB": "_2A25PQqnYDeRhGeFJ71QX9CvIzzuIHXVszDeQrDV6PUJbkdB-LRXDkW1Nf8flhDUnRiY8Bny8UcpIVgZ3VSGY2jCx",
                "WEIBOCN_FROM": "1110006030",
                "XSRF-TOKEN": "262def"

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
   # start_urls=['https://m.weibo.cn/search?containerid=231522type%3D1%26t%3D10%26q%3D%23%E4%B8%9C%E8%88%AA%E5%9D%A0%E6%AF%81%E8%88%AA%E7%8F%AD%E4%B8%8A%E5%85%B1132%E4%BA%BA%23&extparam=%23%E4%B8%9C%E8%88%AA%E5%9D%A0%E6%AF%81%E8%88%AA%E7%8F%AD%E4%B8%8A%E5%85%B1132%E4%BA%BA%23&luicode=10000011&lfid=100103type%3D38%26q%3D%E4%B8%9C%E8%88%AA%26t%3D0']
   # url=['https://m.weibo.cn/api/container/getIndex?containerid=231522type%3D60%26q%3D%23%E4%B8%9C%E8%88%AA%E5%9D%A0%E6%AF%81%E8%88%AA%E7%8F%AD%E4%B8%8A%E5%85%B1132%E4%BA%BA%23%26t%3D10&extparam=%23%E4%B8%9C%E8%88%AA%E5%9D%A0%E6%AF%81%E8%88%AA%E7%8F%AD%E4%B8%8A%E5%85%B1132%E4%BA%BA%23&luicode=10000011&lfid=100103type%3D38%26q%3D%E4%B8%9C%E8%88%AA%26t%3D0&page_type=searchall']
    #start_urls[0] =start_urls[0].replace('search?containerid=231522type%3D1%26t%3D10','api/container/getIndex?containerid=231522type%3D60')
    def changeip(self):
        print('到点了，定时换号ip')
        stdin, stdout, stderr = self.client.exec_command('pppoe-stop')
        stdin, stdout, stderr = self.client.exec_command('pppoe-start')
        time.sleep(10)

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
                if self.count % 2000==0:
                    self.changeip()
                elif self.count==10000:
                    self.crawler.engine.close_spider(self,"10000条达成!")
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
                    userlocation=getgeo(headers=self.headers,cookies=self.cookies,id=userid,ip=ip)
                    useriplocation=getipgeo(headers=self.headers,cookies=self.cookies,id=userid,ip=ip)
                    item['USERNAME']=username
                    item['USERID']=str(userid)
                    item['LOCATION']= userlocation
                    item['IPREGION']=useriplocation
                    item['TIME'] = time
                    item['TEXT'] = text
                    yield item
            yield scrapy.Request(url=url, headers=header, cookies=cookie, callback=self.comment_parse, meta=response.meta)












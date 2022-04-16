#####################
## 本项目作者：黄炤程
## 完成时间：2022年4月14日下午
## 目前运行正常,本注释旨在给以后的自己看
#####################
import random
import scrapy
import json
import weibo.items
from weibo.timer import TimeFormatTransform
from weibo.geo import getgeo
from weibo.ipgeo import getipgeo
import paramiko
from weibo.replace_url import get_replaced_url
class MyweiboSpider(scrapy.Spider):
    name = 'myweibo' #设置每个爬虫的名称，具有唯一性
    allowed_domains = ['m.weibo.cn'] #限定url
    page=10
    count=0
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname='114.104.210.66', port=20402, username='root', password='nU8tW3tT2uN3')
    start_urls=[''] #爬虫开始以后最先会从start_urls里进行第一次http请求
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with open('starturls.txt','r') as f: #利用weibo文件家里的starturls.txt，每次都可以将进行爬虫的起始网页放入为一行
            #遵照参考格式，只能为微博话题下的热门话题 (https://m.weibo.cn/search?containerid=231522type%3D1%26t%3D10%26q%3D%23%E4%B8%80%E5%AE%9A%E8%A6%81%E5%9C%A8%E5%8E%A6%E9%97%A8%E7%9C%8B%E6%AC%A1%E8%8D%A7%E5%85%89%E6%B5%B7%23&extparam=%23%E4%B8%80%E5%AE%9A%E8%A6%81%E5%9C%A8%E5%8E%A6%E9%97%A8%E7%9C%8B%E6%AC%A1%E8%8D%A7%E5%85%89%E6%B5%B7%23&luicode=20000174)
            self.start_urls[0]=f.read().replace('search?containerid=231522type%3D1%26t%3D10','api/container/getIndex?containerid=231522type%3D60')
            self.start_urls[0]=self.start_urls[0]+'&page='+str(self.page)
#添加访问微博的cookie
    cookies=[

        {
                    "_T_WM": "43501422776",
                    "loginScene": "102003",
                    "M_WEIBOCN_PARAMS": "luicode=20000174&uicode=20000174",
                    "MLOGIN": "1",
                    "mweibo_short_token": "b709eae71c",
                    "SUB": "_2A25PU7sQDeRhGeBI4lAU8y_Ezz6IHXVsv8VYrDV6PUJbkdANLWzRkW1NRn2D3Zpmtuxo2fg_qymlUfVaKUiY4N8G",
                    "WEIBOCN_FROM": "1110006030",
                    "XSRF-TOKEN": "43890b"
        }
        ,
        {


                    "_T_WM": "31870840980",
                    "loginScene": "102003",
                    "M_WEIBOCN_PARAMS": "luicode=20000174&uicode=20000174",
                    "MLOGIN": "1",
                    "mweibo_short_token": "d8de6fb1a0",
                    "SUB": "_2A25PU7vmDeRhGeFJ71QX9CvIzzuIHXVsv8WurDV6PUJbkdCOLUKkkW1Nf8flhIcXXv86hpMEO2Gc7jolF9nnspf2",
                    "WEIBOCN_FROM": "1110006030",
                    "XSRF-TOKEN": "5a0feb"


        },
        {
                    "_T_WM": "30333836359",
                    "loginScene": "102003",
                    "M_WEIBOCN_PARAMS": "lfid=102803&luicode=20000174&uicode=20000174",
                    "MLOGIN": "1",
                    "mweibo_short_token": "f6b94f31d6",
                    "SUB": "_2A25PU7uhDeRhGeBI4lAU8y_Ezz6IHXVsv8XprDV6PUJbkdCOLXDRkW1NRn2D3TGJ1XxJ674yQ0aIt10ioluD75LB",
                    "WEIBOCN_FROM": "1110006030",
                    "XSRF-TOKEN": "baf746"


        },
        {

                    "_T_WM": "85275312875",
                    "loginScene": "102003",
                    "M_WEIBOCN_PARAMS": "luicode=10000011&lfid=102803&uicode=20000174",
                    "MLOGIN": "1",
                    "mweibo_short_token": "c2c0ee0228",
                    "SUB": "_2A25PU7x9DeRhGeFJ71QX9CvIzzuIHXVsv8Q1rDV6PUJbkdAKLWnHkW1Nf8flhFYHDc9fFetXqYKUthlVW-hxR1Q0",
                    "WEIBOCN_FROM": "1110006030",
                    "XSRF-TOKEN": "105d4d"
        }
    ]
#添加访问微博的header头
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

    # def changeip(self): #利用vps服务器的pppoe命令更改ip
    #     print('到点了，定时换号ip')
    #     stdin, stdout, stderr = self.client.exec_command('pppoe-stop')
    #     stdin, stdout, stderr = self.client.exec_command('pppoe-start')
    #     time.sleep(10)

    def parse(self, response):#最开始的指定网页返回包会在此函数解析
        self.start_urls[0]=self.start_urls[0].replace('&page='+str(self.page),'')#取消start_url里的第一个page
        self.page = self.page + 1 #每个网页后有个page参数代表多少页，表示人工操作中的手工翻页
        body = json.loads(response.text,strict=False) #因为读取到的是json数据所以可以用json.loads函数进行解析
        data = body.get('data') #按照该json返回数据解析
        title=data.get('cardlistInfo').get('title_top').strip('-').strip('#')
        header = random.choice(self.headers) #每次随机选用设定好的header池进行获取
        cookie = random.choice(self.cookies) #每次随机选用设定好的cookie池进行获取
        if not 'msg' in body: #爬虫结束的标志是该json里有msg，msg里的数据是"暂无数据"
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
                    user_id = mblog.get('user').get('id')
                    time = TimeFormatTransform(mblog.get('created_at'))
                    comment_url = 'https://m.weibo.cn/comments/hotflow?id=' + str(id) + '&mid=' + str(
                        id) + '&max_id_type=0' #解析微博的评论后发现，因为微博是从json返回的数据中有个id，该id用来进入评论网页
                    yield scrapy.Request(url=comment_url, headers=header, cookies=cookie, callback=self.comment_parse,
                                         meta={'url': comment_url, 'key':title,'userid':user_id})#进行微博评论的爬取
            url = self.start_urls[0] + '&page=' + str(self.page) #类似于手工操作，在热门话题下翻页
            with open('starturls.txt', 'a') as f:
                f.write('\n'+url) #该为测试使用，旨在知道爬虫断在哪一个url的page上
            yield scrapy.Request(url=url, headers=header, cookies=cookie, callback=self.parse) #类似于手工操作，在热门话题下翻页
        else:
            self.crawler.engine.close_spider(self,"到底了!") #整体退出所需要的步骤
    def comment_parse(self, response):
        global comment2comment_url
        body = json.loads(response.text,strict=False)#本步骤基本和上面的步骤一致
        item=weibo.items.WeiboItem()#引入该项目里的item数据类型，该数据类型会用于在pipeline.py里进行数据库存储
        header = random.choice(self.headers)
        cookie = random.choice(self.cookies)
        stdin, stdout, stderr = self.client.exec_command(
            'ifconfig  ppp0 | awk \'{print $2}\'|awk "NR==2"')
        result = stdout.read().decode('utf-8') #因为m.weibo.cn里暂时还没有ip属地的json所以需要一个ip用来发起一个requests在用户的主页里找到ip_location
        ip = {'http': result.strip() + ':8888'}
        print(ip)
        if body.get('ok') == 1:#获取评论翻页需要的数据
            datas = body.get('data')#评论翻页不是page形式儿时有一个maxid进行翻页
            data = datas.get('data')
            max_id = datas.get('max_id')
            url = response.meta.get('url') + '&max_id=' + str(max_id)
            for t in data:
                self.count=self.count+1 #当前计数的条数
                print("当前第" + str(self.count) + "条")
                # if self.count % 2000 == 0:#你要记住这一点，一旦转换了原来有的ip就会失效
                #     self.changeip()
                #     stdin, stdout, stderr = self.client.exec_command(
                #         'ifconfig  ppp0 | awk \'{print $2}\'|awk "NR==2"')
                #     result = stdout.read().decode('utf-8')
                #     ip = {'http': result.strip() + ':8888'}
                #     print(ip)
                if self.count==10000:
                    self.crawler.engine.close_spider(self,"10000条达成!") #爬虫会停止在10000条
                else:
                    id=t.get('id')
                    totol_nums=t.get('total_number')
                    user = t.get('user')
                    time = TimeFormatTransform(t.get('created_at')) #利用自制的time转换器
                    comment2comment_url = 'https://m.weibo.cn/comments/hotFlowChild?cid='+str(id)+'&max_id=0&max_id_type=0'
                    if totol_nums!=0:
                        yield scrapy.Request(url=comment2comment_url, headers=header, cookies=cookie,
                                         callback=self.comment2comment_parse, meta={'url': comment2comment_url})
                    if t.get('text')!='转发微博': #初步过滤内容为“转发微博”的微博
                        text = t.get('text')
                    else:
                        self.count=self.count-1#初步过滤内容为“转发微博”的微博
                        continue
                    userid = user.get('id')
                    username = user.get('screen_name')
                    userlocation=getgeo(headers=self.headers,cookies=self.cookies,id=userid,ip=ip)#进入geo.py里的getgeo函数
                    useriplocation=getipgeo(headers=self.headers,cookies=self.cookies,id=userid,ip=ip)#进入ipgeb.py里的getipgeo函数
                    item['USERNAME']=username
                    item['USERID']=str(userid)
                    item['LOCATION']= userlocation
                    item['IPREGION']=useriplocation
                    item['TIME'] = time
                    item['TEXT'] = text
                    yield item #存储所有必须的内容于item里，然后进入pipeline.py里进行处理

            if max_id!=0:
                yield scrapy.Request(url=url, headers=header, cookies=cookie, callback=self.comment_parse, meta=response.meta) #利用maxid进行翻页
    def comment2comment_parse(self,response):
        body=json.loads(response.text,strict=False)
        item = weibo.items.WeiboItem()  # 引入该项目里的item数据类型，该数据类型会用于在pipeline.py里进行数据库存储
        header = random.choice(self.headers)
        cookie = random.choice(self.cookies)
        stdin, stdout, stderr = self.client.exec_command(
            'ifconfig  ppp0 | awk \'{print $2}\'|awk "NR==2"')
        result = stdout.read().decode('utf-8')  # 因为m.weibo.cn里暂时还没有ip属地的json所以需要一个ip用来发起一个requests在用户的主页里找到ip_location
        ip = {'http': result.strip() + ':8888'}
        print(ip)
        if body.get('ok') == 1:  # 获取评论翻页需要的数据
            data = body.get('data')
            max_id = body.get('max_id')
            url = get_replaced_url(response.meta.get('url'),max_id)
            for i in data:
                self.count = self.count + 1  # 当前计数的条数
                if self.count==10000:
                    self.crawler.engine.close_spider(self,"10000条达成!") #爬虫会停止在10000条
                print("当前第" + str(self.count) + "条")
                time = TimeFormatTransform(i.get('created_at'))  # 利用自制的time转换器
                user=i.get('user')
                if i.get('text') != '转发微博':  # 初步过滤内容为“转发微博”的微博
                    text = i.get('text')
                else:
                    self.count = self.count - 1  # 初步过滤内容为“转发微博”的微博
                    continue
                userid=user.get('id')
                username=user.get('screen_name')
                userlocation = getgeo(headers=self.headers, cookies=self.cookies, id=userid, ip=ip)  # 进入geo.py里的getgeo函数
                useriplocation = getipgeo(headers=self.headers, cookies=self.cookies, id=userid,
                                          ip=ip)  # 进入ipgeb.py里的getipgeo函数
                item['USERNAME'] = username
                item['USERID'] = str(userid)
                item['LOCATION'] = userlocation
                item['IPREGION'] = useriplocation
                item['TIME'] = time
                item['TEXT'] = text
                yield item  # 存储所有必须的内容于item里，然后进入pipeline.py里进行处理
            if max_id!=0:
                yield  scrapy.Request(url=url,headers=header, cookies=cookie, callback=self.comment2comment_parse,meta=response.meta)











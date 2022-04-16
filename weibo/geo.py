import requests
import random
import json
from requests.adapters import HTTPAdapter


def getgeo(headers,cookies,id,ip):
    s = requests.session()
    # max_retries=3 重试3次
    s.mount('https://', HTTPAdapter(max_retries=3))
    r=s.request("GET",url='https://weibo.com/ajax/profile/info?uid='+str(id),headers=random.choice(headers),cookies=random.choice(cookies),proxies=ip,timeout=10)
    #headers传入的是header池，cookies也是cookie池，ip按照固定的格式{'http':"yourip:"+"yourport"}
    #r=requests.get('https://weibo.com/ajax/profile/info?uid='+str(id),headers=random.choice(headers),cookies=random.choice(cookies),proxies=ip,timeout=10)

    if r.text!=None:
        body=json.loads(r.text,strict=False)
        if body!=None:
            data = body.get('data')
            if data!=None:
                user = data.get('user')
                if user.get('location') != None:
                    return user.get('location')
                else:
                    return '暂无地区'
            else:
                return '暂无地区'
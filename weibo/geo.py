import requests
import random
import json
def getgeo(headers,cookies,id,ip):
    r=requests.get('https://weibo.com/ajax/profile/info?uid='+str(id),headers=random.choice(headers),cookies=random.choice(cookies),proxies=ip)
    if r.text!=None:
        body=json.loads(r.text,strict=False)
        data = body.get('data')
        user = data.get('user')
        return user.get('location')
    else:
        return '暂无地区'
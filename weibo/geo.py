import requests
import random
import json
def getgeo(headers,cookies,id,ip):
    r=requests.get('https://weibo.com/ajax/profile/info?uid='+str(id),headers=random.choice(headers),cookies=random.choice(cookies),proxies=ip)

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
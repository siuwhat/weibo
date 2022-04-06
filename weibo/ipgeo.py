
import requests
import random
import json


def getipgeo(headers, cookies, id, ip):
    print(ip)
    r=requests.get('https://weibo.com/ajax/profile/detail?uid='+str(id),headers=random.choice(headers),cookies=random.choice(cookies),proxies=ip)

    if r.text != None:
        body = json.loads(r.text, strict=False)
        if body!=None:
            data = body.get('data')
            if data.get('region')!=None:
                return data.get('region')
            else:
                return 'ip属地：暂无'
        else:
            return 'ip属地:暂无'
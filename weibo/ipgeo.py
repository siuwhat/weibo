# encoding=gbk
import requests
import random
import json
from requests.adapters import HTTPAdapter


def getipgeo(headers, cookies, id, ip):
    s = requests.session()
    # max_retries=3 ����3��
    s.mount('https://', HTTPAdapter(max_retries=3))
    r = s.request("GET", url='https://weibo.com/ajax/profile/detail?uid='+str(id), headers=random.choice(headers),
                  cookies=random.choice(cookies), proxies=ip, timeout=10)
    #headers�������header�أ�cookiesҲ��cookie�أ�ip���չ̶��ĸ�ʽ{'http':"yourip:"+"yourport"}
    #r=requests.get('https://weibo.com/ajax/profile/detail?uid='+str(id),headers=random.choice(headers),cookies=random.choice(cookies),proxies=ip,timeout=10)
    if r.text != None:
        body = json.loads(r.text, strict=False)
        if body!=None:
            data = body.get('data')
            if data!=None:
                ip_location=data.get('ip_location')
                if ip_location!=None and ip_location!="":
                    return ip_location
                else:
                    return 'IP���أ�����'
            else:
                return 'IP���أ�����'
        else:
            return 'IP���أ�����'
    else:
        return 'IP���أ�����'


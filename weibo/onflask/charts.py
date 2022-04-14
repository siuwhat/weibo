import json
import os.path
import sys

import requests
from flask import Blueprint,render_template,url_for
from hotspot import mybar
from mapspot import mygeo
from weibo.onflask.sentipie import mypie
from wordcloudshow import mywdcd
from sentiment import mysenti

def get_title():
    with open('../../starturls.txt','r') as f:
        url=f.read().replace('search?containerid=231522type%3D1%26t%3D10','api/container/getIndex?containerid=231522type%3D60')
        r=requests.get(url=url,)
        body = json.loads(r.text, strict=False)
        data=body.get('data')
        info=data.get('cardlistInfo')
        title=info.get('title_top')
        return title.strip('-').strip('#')


title=get_title()
chart=Blueprint('chart',__name__,url_prefix='/chart')
@chart.route('/hotspot')
def show():
    return render_template('show.html',**{'url':'/chart/hotspot_show','title':title})

@chart.route('/hotspot_show')
def hotspot_show():
    return mybar()

@chart.route('/mapspot')
def mapshow():
    return render_template('show.html',**{'url':'/chart/mapspot_show','title':title})

@chart.route('/mapspot_show')
def mapspot_show():
    return mygeo()

@chart.route('/wordcloud')
def wordcloud():
    return render_template('show.html',**{'url':'/chart/wordcloud_show','title':title})

@chart.route('/wordcloud_show')
def wordcloudshow():
    return mywdcd()

@chart.route('/sentiments')
def sentiments():
    return render_template('sentiments.html',**{'url':'/chart/senti_show','title':title})

@chart.route('/senti_show')
def sentiment_show():
    return mysenti()

@chart.route('/pie')
def pie():
    return render_template('show.html',**{'url':'/chart/pie_show','title':title})

@chart.route('/pie_show')
def pie_show():
    return mypie()
import json
import requests
from flask import Blueprint, render_template, url_for, request
from hotspot import mybar
from mapspot import mygeo
from wordcloudshow import mywdcd
from sentiment import mysenti,mysentimap


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
word=Blueprint('word',__name__,url_prefix='/word')

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
    return render_template('sentiments.html',**{'url':'/chart/wordcloud_show','title':title},href='/wordfreq')

@chart.route('/wordcloud_show')
def wordcloudshow():
    return mywdcd()

@chart.route('/sentiments')
def sentiments():
    return render_template('sentiments.html',**{'url':'/chart/senti_show','title':title},href="/allshow_sentiment",flag=1)

@chart.route('/senti_show')
def sentiment_show():
    return mysenti()

@chart.route('/sentimap')
def sentimap():
    return render_template('show.html', **{'url': '/chart/sentimap_show', 'title': title})

@chart.route('/sentimap_show')
def sentimap_show():
    return mysentimap()


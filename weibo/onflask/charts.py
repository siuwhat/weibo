from flask import Blueprint,render_template,url_for
from hotspot import mybar
from mapspot import mygeo
from wordcloudshow import mywdcd
chart=Blueprint('chart',__name__,url_prefix='/chart')
@chart.route('/hotspot')
def show():
    return render_template('show.html',**{'url':'/chart/hotspot_show'})

@chart.route('/hotspot_show')
def hotspot_show():
    return mybar()

@chart.route('/mapspot')
def mapshow():
    return render_template('show.html',**{'url':'/chart/mapspot_show'})

@chart.route('/mapspot_show')
def mapspot_show():
    return mygeo()

@chart.route('/wordcloud')
def wordcloud():
    return render_template('show.html',**{'url':'/chart/wordcloud_show'})

@chart.route('/wordcloud_show')
def wordcloudshow():
    return mywdcd()

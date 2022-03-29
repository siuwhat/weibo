from flask import Blueprint,render_template,url_for
from hotspot import mybar
chart=Blueprint('chart',__name__,url_prefix='/chart')
@chart.route('/hotspot')
def show():
    return render_template('show.html',mybar=mybar())

@chart.route('/hotspot_show')
def hotspot_show():
    return '/static/weiboreli.png'


# encoding=gbk
from datetime import datetime
from snownlp import SnowNLP
from filter import filter_str
import pymysql
from pyecharts.charts import Line,Grid
from pyecharts import options as opts
from hotspot import timer,count,thebar
import csv
from export_senti import export


def getstopstr():
    stopstr=""
    with open("static/file/txt/stopwords.txt","r",encoding="utf-8") as f:
        for i in f.readlines():
            stopstr=stopstr+i.strip()
    return stopstr

def export_senti():
    db = pymysql.connect(host='localhost', passwd='root', user='root', database='spider')
    flag = db.cursor()
    flag.execute('select * from text ;')
    res_list = flag.fetchall()
    stopwords = getstopstr()
    sentilist = []
    headers=['id','username','userid','time','location','ipregion','text','sentiment']
    with open('static/file/csv/senti.csv','w',encoding='utf-8-sig',newline='') as fs:
        f=csv.writer(fs)
        f.writerow(headers)
        for i in res_list:
            res=list(i)
            string=filter_str(res[6])
            if (string != "") and (not string in stopwords):
                sn=SnowNLP(string)
                res.append(sn.sentiments)
                sentilist.append(res)
                f.writerow(res)
    return sentilist

def get_mean_senti():
    db = pymysql.connect(host='localhost', passwd='root', user='root', database='spider')
    flag = db.cursor()
    flag.execute('show tables;')
    table_list = flag.fetchall()
    sentilist = []
    stopwords = getstopstr()
    for tablename in table_list:
        if '20' in tablename[0]:
            textlist = []
            allnumber = 0.0
            flag.execute('select text from ' + tablename[0] + ';')
            db.commit()
            res_list = flag.fetchall()
            for t in res_list:
                string = filter_str(t[0])
                if (string != "") and (not string in stopwords):
                    textlist.append(string)
            length = len(textlist)
            if length==0:
                length=length+1
            for s in textlist:
                sn = SnowNLP(s)
                allnumber = allnumber + sn.sentiments
            sentilist.append(allnumber / length)
    return sentilist

def get_timelist():
    x = [datetime.strptime(timer(k), '%Y-%m-%d').date() for k in count().keys()]
    print(x)
    return x

def export_sentiment():
    export()

def mysenti():
    export_sentiment()
    sentilist=get_mean_senti()
    x_list=get_timelist()
    bar=thebar()
    line=(Line(init_opts=opts.InitOpts(width="1200px",height="600px")).add_xaxis(xaxis_data=x_list).add_yaxis(series_name="情绪值",y_axis=sentilist,color="black",symbol_size=8,is_hover_animation=False,label_opts=opts.LabelOpts(is_show=False),is_smooth=True, linestyle_opts=opts.LineStyleOpts(width=1.5),)
          .set_global_opts(tooltip_opts=opts.TooltipOpts(trigger='axis'),
                           datazoom_opts=opts.DataZoomOpts(type_='inside'),
                           title_opts=opts.TitleOpts(title='情绪折线图',subtitle='基于SNOWNLP的情绪值分析',pos_left="center"),
                           xaxis_opts=opts.AxisOpts(type_="category"),
                           legend_opts=opts.LegendOpts(is_show=True,pos_left="7%"),
                           )
          )
    grid=Grid(init_opts=opts.InitOpts(width="1000px",height="600px")).add(bar,grid_opts=opts.GridOpts(pos_top="60%")).add(line,grid_opts=opts.GridOpts(pos_bottom="60%")).render_embed()
    return grid


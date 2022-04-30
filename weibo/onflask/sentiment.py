# encoding=gbk
from datetime import datetime,timedelta
from snownlp import SnowNLP
from filter import filter_str
import pymysql
from pyecharts.charts import Line, Map
from pyecharts import options as opts
from hotspot import timer,count
import csv
from export_senti import export
from mapspot import allregiondict

def getstopstr():
    stopstr=""
    with open("static/file/txt/stopwords.txt","r",encoding="utf-8") as f:
        for i in f.readlines():
            stopstr=stopstr+i.strip()
    return stopstr


def allsentigeo():
    db = pymysql.connect(host='localhost', passwd='root', user='root', database='spider')
    flag = db.cursor()
    flag.execute("select ipregion,text from text;")
    region_list=flag.fetchall()
    dict={}
    list=[]
    stopwords=getstopstr()
    for i in region_list:
        str=i[0]
        str=str.replace(':','：')
        reg=str.split('：')[1]
        if reg=='中国香港':
            reg="香港"
        elif reg=='中国台湾':
            reg="台湾"
        if reg in allregiondict:
            text = filter_str(i[1])
            if (text != "") and (not text in stopwords):
                sn=SnowNLP(text)
                if dict.get(reg)!=None:
                    dict[reg][0]=dict[reg][0]+sn.sentiments
                    dict[reg][1]=dict[reg][1]+1
                else:
                    dict[reg]=[sn.sentiments,1]
    for k,v in dict.items():
        newlist=[]
        newlist.append(k)
        newlist.append(v[0]/v[1])
        list.append(newlist)
    return  list


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
            flag.execute('select time,text from ' + tablename[0] + ';')#获取时间和时间内的评论
            res_list = flag.fetchall()
            timedict = {}
            for hournums in range(24):
                timedict[hournums] = []  # 设定间隔为每小时
            if len(res_list)>500:#设定大于500才予以采用的阈值
                for t in res_list:
                    hour=int(t[0].split()[1].split(':')[0])
                    string = filter_str(t[1])
                    if (string != "") and (not string in stopwords):
                        timedict[hour].append(string)
                for hournums in range(24):
                    allnumber=0.0
                    length=len(timedict[hournums])
                    for s in timedict[hournums]:
                        sn = SnowNLP(s)
                        allnumber = allnumber + sn.sentiments
                    if length!=0:
                        sentilist.append(allnumber/length)
                    else:
                        sentilist.append(length)
    return sentilist

def get_timelist():
    x = [datetime.strptime(timer(k), '%Y-%m-%d') for k in count().keys()]
    timelist=[]
    for t in x:
        ct=t
        for length in range(24):
            timelist.append(ct)
            ct=ct+timedelta(hours=1)
    return timelist

def export_sentiment():
    export()

def mysenti():
    export_sentiment()
    sentilist=get_mean_senti()
    x_list=get_timelist()
    line=(Line(init_opts=opts.InitOpts(width="1200px",height="600px")).add_xaxis(xaxis_data=x_list).add_yaxis(series_name="情绪值",y_axis=sentilist,color="black",symbol_size=8,is_hover_animation=False,label_opts=opts.LabelOpts(is_show=False),is_smooth=True, linestyle_opts=opts.LineStyleOpts(width=1.5),)
          .set_global_opts(tooltip_opts=opts.TooltipOpts(trigger='axis'),
                           datazoom_opts=opts.DataZoomOpts(type_='inside'),
                           title_opts=opts.TitleOpts(title='情绪图',subtitle='基于SNOWNLP的情绪值分析',pos_left="center"),
                           xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,axistick_opts=opts.AxisTickOpts()),
                           legend_opts=opts.LegendOpts(is_show=True,pos_left="7%"),
                           yaxis_opts=opts.AxisOpts(max_=1)
                           )
          )
    return line.render_embed()

def mysentimap():
    map = (Map(init_opts=opts.InitOpts(width="1050px", height="600px"))
           .add(series_name='地区情绪', data_pair=allsentigeo(), maptype='china', aspect_scale=0.8, )
           .set_global_opts(
        legend_opts=opts.LegendOpts(is_show=False),
        tooltip_opts=opts.TooltipOpts(axis_pointer_type="shadow", background_color="gray"),
        visualmap_opts=opts.VisualMapOpts(max_=0.7,min_=0.3),
        title_opts=opts.TitleOpts(title='情绪地图',subtitle='基于SNOWNLP的情绪值分析',pos_left="center")

    )
           .set_series_opts(label_opts=opts.LabelOpts(is_show=True, color="black"),
                            areastyle_opts=opts.AreaStyleOpts(color="gray")))
    return map.render_embed()
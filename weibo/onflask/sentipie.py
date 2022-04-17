# encoding=gbk

from snownlp import SnowNLP
from filter import filter_str
from pyecharts.charts import Pie, Liquid, Grid
from pyecharts import options as opts
import pymysql

def getstopstr():
    stopstr=""
    with open("static/file/txt/stopwords.txt","r",encoding="utf-8") as f:
        for i in f.readlines():
            stopstr=stopstr+i.strip()
    return stopstr


def get_sentiment():

    db = pymysql.connect(host='localhost', passwd='root', user='root', database='spider')
    flag = db.cursor()
    flag.execute('select text from text ;')
    res_list = flag.fetchall()
    db.commit()
    kind=4
    partlist=[]
    pos=0
    neg=0
    for i in range(kind):
        partlist.append([i])
        partlist[i].append(0)
    stopwords = getstopstr()
    for res in res_list:
        string = filter_str(res[0])
        if (string != "") and (not string in stopwords):
            sn=SnowNLP(string)
            if 0<=sn.sentiments<0.25:
                partlist[0][1]=partlist[0][1] + 1
            elif 0.25<=sn.sentiments<0.50:
                partlist[1][1]=partlist[1][1] + 1
            elif 0.50<=sn.sentiments<0.75:
                partlist[2][1]=partlist[2][1] + 1
            else:
                partlist[3][1] = partlist[3][1] + 1

    # print(partlist)
    # print(halfLiquid)
    partlist[0][0]="不满意"
    partlist[1][0]="较不满意"
    partlist[2][0]="较满意"
    partlist[3][0]="满意"
    # print(partlist)
    return partlist



def mypie():

    pie=(Pie()
         .add(series_name="",data_pair=get_sentiment(),center=["50%","50%"])
         .set_global_opts(
        legend_opts=opts.LegendOpts(pos_right="15%", orient="vertical"),
        title_opts=opts.TitleOpts(title="情绪比较饼图",subtitle="情绪值<0.5=消极,情绪值>0.5为积极",pos_left="center")
    )
         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}")).render_embed())
    return pie






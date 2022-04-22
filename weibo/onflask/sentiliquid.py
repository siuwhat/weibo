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
    pos=0
    neg=0
    stopwords = getstopstr()
    for res in res_list:
        string = filter_str(res[0])
        if (string != "") and (not string in stopwords):
            sn=SnowNLP(string)
            if 0<=sn.sentiments<0.5:
                neg=neg+1
            else:
                pos=pos+1
    pos_num=pos/(pos+neg)
    # print(partlist)
    # print(halfLiquid)
    print(pos_num)
    # partlist[3][0]="满意"
    # print(partlist)
    return pos_num



def myliquid():

    li = (
        Liquid().add('积极程度', [get_sentiment()], center=['70%', '50%']).set_global_opts(title_opts=opts.TitleOpts(title="积极程度图",pos_left="60%")).render_embed())

    return li

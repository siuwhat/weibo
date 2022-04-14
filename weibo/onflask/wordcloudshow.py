# encoding=gbk
from copy import deepcopy

import jieba
import jieba.analyse
from filter import filter_str
from pyecharts import options as opts
from pyecharts.charts import WordCloud
import pymysql
import wordcloud
def getstopstr():
    stopstr=""
    with open("static/file/txt/stopwords.txt","r",encoding="utf-8") as f:
        for i in f.readlines():
            stopstr=stopstr+i.strip()
    return stopstr
def gaoping():
    db = pymysql.connect(host='localhost', passwd='root', user='root', database='spider')
    flag = db.cursor()
    flag.execute("select text from text;")
    db.commit()
    res_list=flag.fetchall()
    dict={}
    stopwords=getstopstr()
    for i in res_list:
        l=jieba.lcut(filter_str(i[0]))
        newl=l.copy()
        str=""
        for i in newl:
            str=str+" "+i
        # print("str"+str)
        for s in l:
            if (len(s)>=2) and (not s in stopwords) and (not s.isdigit()):
                if  dict.get(s)==None:
                    dict[s]=1
                else:
                    dict[s]=dict[s]+1
                jieba.add_word(s)

    dict=sorted(dict.items(),key=lambda d:d[-1],reverse=True)
    # print(dict)
    return dict
def get_wordlist():
    db = pymysql.connect(host='localhost', passwd='root', user='root', database='spider')
    flag = db.cursor()
    flag.execute("select text from text;")
    db.commit()
    res_list = flag.fetchall()
    stopwords = getstopstr()
    newlist=[]
    for i in res_list:
        mylist = jieba.lcut(filter_str(i[0]))
        for s in mylist:
            if (len(s)>=2) and (not s in stopwords) and (not s.isdigit()):
                jieba.add_word(s)
                newlist.append(s)
    # print(newlist)
    return newlist
def mywdcd():
    return (WordCloud(init_opts=opts.InitOpts(width="1600px",height="1000px")).add(series_name="热点分析",data_pair=gaoping(),shape="cursive",word_size_range=[14,66],mask_image="static/file/png/plane.png",word_gap=5,pos_top="10%",pos_left="10px")
            .set_global_opts(
        title_opts=opts.TitleOpts(
            title="热点分析词云图", title_textstyle_opts=opts.TextStyleOpts(font_size=28),pos_top="10%"
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render_embed())
mywdcd()
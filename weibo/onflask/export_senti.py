# encoding=gbk
import csv

import pymysql
from snownlp import SnowNLP

from filter import filter_str
from sentipie import getstopstr

def export():
    db = pymysql.connect(host='localhost', passwd='root', user='root', database='spider')
    flag = db.cursor()
    flag.execute('select * from text ;')
    res_list = flag.fetchall()
    stopwords = getstopstr()
    sentilist = []
    headers=['id','username','userid','time','location','ipregion','text','sentiment']
    for i in res_list:
        res = list(i)
        string = filter_str(res[6])
        if (string != "") and (not string in stopwords):
            sn = SnowNLP(string)
            res.append(sn.sentiments)
            sentilist.append(res)
    sentilist.sort(key=lambda x:x[7],reverse=True)

    with open('static/file/csv/senti.csv','w',encoding='utf-8-sig',newline='') as fs:
        f=csv.writer(fs)
        f.writerow(headers)
        for j in sentilist:
            f.writerow(j)


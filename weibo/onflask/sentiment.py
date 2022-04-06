# encoding=gbk
from snownlp import SnowNLP
from wordcloudshow import getstopstr
from filter import filter_str
import pymysql
db = pymysql.connect(host='localhost', passwd='root', user='root', database='spider')
flag = db.cursor()
flag.execute("select text from text;")
db.commit()
res_list = flag.fetchall()

stopwords = getstopstr()
for i in res_list:
    string=filter_str(i[0])
    if string!="":
        print("原语句:" + string)
        num=SnowNLP(string)
        print("情感值"+str(num.sentiments))

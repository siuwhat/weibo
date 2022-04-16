# 再次定义你的item pipeline
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
import pymysql
import codecs
import requests
import json
class WeiboPipeline:
    def __init__(self):
        self.file=open('text.csv','a',encoding='gb18030',newline='')#写入text.csv 注意encoding不能为utf-8，要么是utf-8-sig要么是gbk,gb18030
        self.db = pymysql.connect(host='localhost', passwd='root', user='root', database='spider')
        self.flag = self.db.cursor()
        self.csvwriter=csv.writer(self.file)#获取csv的读取器
        self.csvwriter.writerow(['用户名','用户id','发布时间','用户位置','用户IP属地','用户评论'])#写入csv的头字段
    def process_item(self, item, spider):#每个item都会传递到这里
        #将item里存储的item数据写入到text.csv
        self.csvwriter.writerow([item['USERNAME'],item['USERID'],item['TIME'],item['LOCATION'],item['IPREGION'],item['TEXT']])
        date=item['TIME']
        data = '\''+str(item['USERNAME'])+'\',\'' + str(item['USERID']) + '\',\''+str(item['TIME'])+'\',\''+str(item['LOCATION'])+'\',\''+str(item['IPREGION'])+'\',\''+str(item['TEXT'].replace('\'','\"')+'\'')
       #进行创建text数据表
        self.flag.execute(
            'create table if not exists text(id int unsigned auto_increment primary key,username varchar(100) not null,userid varchar(100) not null,time varchar(100) not null,location varchar(100),ipregion varchar(100),text text not null);')
       #对text数据表进行插入操作
        self.flag.execute('insert into text(username,userid,time,location,ipregion,text)values('+data+');')
        return item
    def close_spider(self, spider):
        self.file.close()


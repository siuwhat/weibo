# Define your item pipelines here
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
        self.file=open('text.csv','a',encoding='gb18030',newline='')
        self.db = pymysql.connect(host='localhost', passwd='root', user='root', database='spider')
        self.flag = self.db.cursor()
        self.csvwriter=csv.writer(self.file)
        self.csvwriter.writerow(['用户名','用户id','发布时间','用户位置','用户IP属地','用户评论'])
    def process_item(self, item, spider):
        self.csvwriter.writerow([item['USERNAME'],item['USERID'],item['TIME'],item['LOCATION'],item['IPREGION'],item['TEXT']])
        datalist={'username':item['USERNAME'],'userid':item['USERID'],'time':item['TIME'],'location':item['LOCATION'],'ipregion':item['IPREGION'],'text':item['TEXT']}
        datajson=json.dumps(datalist)
        date=item['TIME']
        tabledate = date.split('-');
        time = ''
        for d in tabledate:
            time = time + d
        #data=item['USERNAME']+','+str(item['USERID'])+','+item['TIME']+','+item['LOCATION']+','+item['TEXT']

        data = '\''+str(item['USERNAME'])+'\',\'' + str(item['USERID']) + '\',\''+str(item['TIME'])+'\',\''+str(item['LOCATION'])+'\',\''+str(item['IPREGION'])+'\',\''+str(item['TEXT'].replace('\'','\"')+'\'')
        with open('111.html', 'a', encoding='utf-8') as f:
            f.write(data)
        # print(data)
        # print('insert into text(username,userid,time,location,text)values('+data+');')
        self.flag.execute(
            'create table if not exists text(id int unsigned auto_increment primary key,username varchar(100) not null,userid varchar(100) not null,time varchar(100) not null,location varchar(100),ipregion varchar(100),text text not null);')
        self.flag.execute('insert into text(username,userid,time,location,ipregion,text)values('+data+');')
        return item
    def close_spider(self, spider):
        self.file.close()
    # def process_item(self,item,spider):
    #     pass



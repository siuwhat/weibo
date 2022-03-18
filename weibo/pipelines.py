# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
import codecs
class WeiboPipeline:
    def __init__(self):
        self.file=open('text.csv','a',encoding='gb18030',newline='')
        self.csvwriter=csv.writer(self.file)
        self.csvwriter.writerow(['用户名','用户id','发布时间','用户位置','用户评论'])
    def process_item(self, item, spider):
        self.csvwriter.writerow([item['USERNAME'],item['USERID'],item['TIME'],item['LOCATION'],item['TEXT']])
        return item
    def close_spider(self, spider):
        self.file.close()
    # def process_item(self,item,spider):
    #     pass



import pymysql
import csv

reader=csv.reader(open('../text.csv','r',encoding='gb18030'))
text=list(reader)
for i in range(1,len(text)):
    print(text[i][2].split()[0])
    f=open('../'+text[i][2].split()[0]+'.csv','a',encoding='gb18030',newline='')
    writer=csv.writer(f)
    writer.writerow(text[i])
    f.close()

db=pymysql.connect(host='localhost',passwd='root',user='root',database='spider')
flag=db.cursor()
t=flag.execute('select * from test;')
if t!=0:
    flag.execute('truncate table test')
print(t)
import pymysql
import csv

reader=csv.reader(open('../text.csv','r',encoding='gb18030'))
db=pymysql.connect(host='localhost',passwd='root',user='root',database='spider')
flag=db.cursor()

text=list(reader)
for i in range(1,len(text)):
    date=text[i][2].split()[0]
    tabledate=date.split('-');
    time=''
    for d in tabledate:
        time=time+d
    data=''
    for j in text[i]:
        j=j.replace('\'','\"')
        data=data+',\''+str(j)+'\''
    data=data.strip(',')


    flag.execute('create table if not exists text'+ time+'(id int unsigned auto_increment primary key,username varchar(100) not null,userid varchar(100) not null,time varchar(100) not null,location varchar(100),text text not null);')
    # t = flag.execute('select * from text'+time+';')
    # if t != 0:
    #     flag.execute('truncate table text'+time+';')
    # print(t)
    print('insert into text'+time+'(username,userid,time,location,text)values('+data+');')
    flag.execute('insert into text'+time+'(username,userid,time,location,text)values('+data+');')
    f=open('../'+text[i][2].split()[0]+'.csv','a',encoding='gb18030',newline='')

    writer=csv.writer(f)
    writer.writerow(text[i])
    f.close()


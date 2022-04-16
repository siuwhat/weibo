#本代码用sql语句进行去重，仅此而已
import pymysql

db = pymysql.connect(host='localhost', passwd='root', user='root', database='spider')
flag = db.cursor()
flag.execute('show tables;')
db.commit()
table_list = flag.fetchall()
print(table_list)
for tablename in table_list:
    print(tablename[0])
    if 'text'==tablename[0]:
        flag.execute('select * from text group by userid,username,time;')
        db.commit()
        res=flag.fetchall()
        print(res)
        flag.execute('truncate table text;')
        db.commit()
        #flag.execute('create table if not exists text2(id int unsigned auto_increment primary key,username varchar(100) not null,userid varchar(100) not null ,time varchar(100) not null,location varchar(100),ipregion varchar(100),text text not null );')
        db.commit()
        for i in res:
            print(i)
            data=''
            for j in i[1:len(i)]:
                data=data+'\''+j+'\','
            data=data.rstrip(',')
            print(data)
            flag.execute('insert into text(username,userid,time,location,ipregion,text)values('+data+');')
            db.commit()
            print('insert into text(username,userid,time,location,ipregion,text)values('+data+');')

db.commit()

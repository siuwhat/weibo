import pymysql
nums=0

db = pymysql.connect(host='localhost', passwd='root', user='root', database='spider')
flag = db.cursor()
flag.execute('select count(*)from text;')
db.commit()
countnums=flag.fetchone()[0]

for id in range(1,countnums+1):
    flag.execute('select * from text where id=' + str(id) + ';')
    db.commit()
    text=flag.fetchone()
    db.commit()
    print(text)
    date=text[3].split()[0]
    if '/' in date:
        tabledate=date.split('/')
    elif '-' in date:
        tabledate=date.split('-')
    time=''

    for d in tabledate:
        time=time+d
    print(time)
    data=''

    for j in text[1:len(text)+1]:
        j=str(j)
        j = j.replace('\'', '\"')
        data=data+',\''+j+'\''
    data=data.strip(',')
    print(time,data)

    flag.execute('create table if not exists text'+ time+'(id int unsigned auto_increment primary key,username varchar(100) not null,userid varchar(100) not null ,time varchar(100) not null,location varchar(100),ipregion varchar(100),text text not null );')
    db.commit()
    print('insert into text'+time+'(username,userid,time,location,ipregion,text)values('+data+');')
    flag.execute('insert into text'+time+'(username,userid,time,location,ipregion,text)values('+data+');')
    db.commit()
    nums=nums+1



print(countnums)
print(nums)

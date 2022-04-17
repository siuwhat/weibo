import json
import time
import requests
from flask import Flask,jsonify,url_for,request,redirect,render_template
import pymysql
from charts import chart,word
flag=0
db = pymysql.connect(host='localhost', passwd='root', user='root', database='spider')
curse= db.cursor()

app = Flask(__name__)
app.register_blueprint(chart)#注册chart蓝图
app.register_blueprint(word)


def get_title():
    with open('../../starturls.txt','r') as f:
        url=f.read().replace('search?containerid=231522type%3D1%26t%3D10','api/container/getIndex?containerid=231522type%3D60')
        print(url)
        r=requests.get(url=url,)
        body = json.loads(r.text, strict=False)
        data=body.get('data')
        info=data.get('cardlistInfo')
        title=info.get('title_top')
        return title.strip('-').strip('#')

@app.route('/about',methods=['GET'])
def about():
    f = request.args.get('flag')
    print(f)
    global flag
    if f!=None:
        flag=int(f)
    flag=flag+1
    if if_exists('text'):
        if if_data_exists('text'):
            curse.execute('select * from text where id=' + str(flag) + ';')
            db.commit()
            res=curse.fetchone()
            if res:
                data={'data':res}
            else:
                time.sleep(5)
                curse.execute('select * from text where id=' + str(flag) + ';')
                res = curse.fetchone()
                data = {'data': res}
            return data
        else:
            return {'data':'-2'}
    else:
        return {'data':"-1"}
    # return render_template('index.html',**user)




@app.route('/index')
def index():  # put application's code here
    title_dict={'title':get_title()}
    return render_template("index.html",**title_dict)

def if_exists(name):
    curse.execute('show tables;')
    db.commit()
    table_list=curse.fetchall()
    db.commit()
    print(table_list)
    for tablename in table_list:
        print(tablename[0])
        if tablename[0]==name:
            return True
    else:
        return False
def if_data_exists(name):
    num=curse.execute('select * from '+name+';')
    if num!=0:
        return True
    else:
        return False

@app.route('/')
def hello():
    return render_template('hello.html')
@app.route('/chart')
def ret():
    return render_template('hello.html')
if __name__ == '__main__':
    app.run(debug=True)

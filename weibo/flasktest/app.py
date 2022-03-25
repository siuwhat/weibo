import time

from flask import Flask,jsonify,url_for,request,redirect,render_template
import pymysql
flag=0
db = pymysql.connect(host='localhost', passwd='root', user='root', database='spider')
curse= db.cursor()

app = Flask(__name__)

a = [
    {'0': '水浒传','res':''},
    {'1': '三国演义','res':''},
    {'2': '红楼梦','res':''},
    {'3': '西游记','res':''}
]
@app.route('/about',methods=['GET'])
def about():
    f = request.args.get('flag')
    print(f)
    global flag
    if f!=None:
        flag=int(f)
    flag=flag+1
    curse.execute('select * from text where id=' + str(flag) + ';')
    res=curse.fetchone()
    if res:
        data={'data':res}
    else:
        time.sleep(3)
    print(data)
    return data
    # return render_template('index.html',**user)


@app.route('/booklist')
def book_list(id):

    return jsonify(a[id][str(id)])

@app.route('/book')
def book():
    for i in range(len(a)):
        a[i]['res']=url_for('book_list',id=i)
    print(a)
    return jsonify(a)

@app.route('/login')
def login():
    id=request.args.get('id')
    if not id:
        return redirect(url_for('hello_world'))
    else:
        return jsonify(a)

@app.route('/index')
def index():  # put application's code here
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)

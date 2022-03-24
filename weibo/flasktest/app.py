from flask import Flask,jsonify,url_for,request,redirect,render_template
import pymysql
flag=1
db = pymysql.connect(host='localhost', passwd='root', user='root', database='spider')
curse= db.cursor()

app = Flask(__name__)

a = [
    {'0': '水浒传','res':''},
    {'1': '三国演义','res':''},
    {'2': '红楼梦','res':''},
    {'3': '西游记','res':''}
]
@app.route('/about')
def about():
    user={'username':'fuck'}
    curse.execute('select * from text where id=' + str(flag) + ';')
    data={'data':curse.fetchone()}
    print(data)
    return render_template('index.html',**data)

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

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello www!'


if __name__ == '__main__':
    app.run(debug=True)

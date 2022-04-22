
import pymysql
from gensim.models import word2vec
import gensim
import jieba
from filter import filter_str
def getstopstr():
    stopstr=""
    with open("static/file/txt/stopwords.txt","r",encoding="utf-8") as f:
        for i in f.readlines():
            stopstr=stopstr+i.strip()
    return stopstr
def make_model():
    stopword=getstopstr()
    db = pymysql.connect(host='localhost', passwd='root', user='root', database='spider')
    flag = db.cursor()
    flag.execute("select text from text;")
    db.commit()
    res_list = flag.fetchall()
    stopwords = getstopstr()

    with open('static/file/txt/jieba.txt','w',encoding='utf-8')as z:
        for i in res_list:
            list=jieba.lcut(filter_str(i[0]))
            newlist=[]
            for j in list:
                if not j in stopword:
                    newlist.append(j)
            if newlist!=[] and newlist[0]!='\n':
                z.write(" ".join(newlist))

    sentences=word2vec.Text8Corpus('static/file/txt/jieba.txt')
    model=gensim.models.Word2Vec(sentences,sg=0,vector_size=300,window=10,min_count=2,negative=5,sample=0.001,hs=1,workers=4)
    model.save("wdmodel.model")
    words = model.wv.key_to_index
    print(words)

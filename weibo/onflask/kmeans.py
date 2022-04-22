# encoding=gbk
from sklearn.cluster import KMeans
import gensim

from sentipie import getstopstr

stopstr=getstopstr()
def make_kmeans(clunumber):
    model=gensim.models.Word2Vec.load("wdmodel.model")
    print(model.wv.index_to_key)
    newlist=[]
    classify={}
    for i in model.wv.index_to_key:
        newlist.append(model.wv[i])
    # print(newlist)
    for n in range(clunumber):
        classify[n]=[]
    clf=KMeans(n_clusters=clunumber,init="k-means++")
    clf.fit(newlist)
    labels=clf.labels_
    print(labels)
    intlabels=[int(j) for j in labels] #由numpy.int32变成int
    for num,i in enumerate(intlabels):
        string=model.wv.index_to_key[num]
        if len(string) > 1 and not string in stopstr and not string.isdigit():
            classify[i].append(model.wv.index_to_key[num])
    with open('static/file/txt/result.txt','w',encoding='utf-8',newline='') as f:
        for a in classify.items():
            f.write("第"+str(a[0]+1)+"类: ")
            f.write(" ".join(a[1])+'\n'*5)



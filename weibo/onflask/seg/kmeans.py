import json

from sklearn.cluster import KMeans
import numpy
import gensim

model=gensim.models.Word2Vec.load("wdmodel.model")
print(model.wv.index_to_key)
newlist=[]
for i in model.wv.index_to_key:
    newlist.append(model.wv[i])
# print(newlist)

clf=KMeans(n_clusters=3,init="k-means++")
clf.fit(newlist)
labels=clf.labels_
print(labels)
intlabels=[int(j) for j in labels]

classify = {0: [], 1: [],2:[]}
num=0
for i in intlabels:
    classify[i].append(model.wv.index_to_key[num])
    num=num+1
for a in classify.items():
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(a,ensure_ascii=False))
    print(a)

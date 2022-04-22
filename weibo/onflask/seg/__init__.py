import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import gensim

def make_img():
    model=gensim.models.Word2Vec.load("wdmodel.model")
    data=[]
    for i in model.wv.index_to_key:
        data.append(model.wv[i])
    SSE =[]

    for k in range(1,10):
        model = KMeans(n_clusters=k)
        model.fit(data)
        SSE.append(model.inertia_)
    X = range(1,10)
    plt.xlabel('k')
    plt.ylabel('SSE')
    plt.plot(X,SSE,'o-')
    #plt.show()
    plt.savefig('sse.png')

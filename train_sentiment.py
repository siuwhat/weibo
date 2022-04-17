from snownlp import sentiment
with open('daoru.txt','r',encoding='utf-8') as f:
    reader=f.readlines()
    for key,item in enumerate(reader,):
        res=item.split()
        num=res[0]
        if num !="0" and num!="1" :
            print(key+1)
        if len(res)<2:
            print(key+1)
        else:
           with open('neg.txt','a',encoding='utf-8') as n:
                with open('pos.txt','a',encoding='utf-8') as p:
                    if num=="0":
                        n.write(res[1]+'\n')
                    else:
                        p.write(res[1]+'\n')
sentiment.train('neg.txt', 'pos.txt')
sentiment.save('weibo.marshal')





from snownlp import sentiment
from snownlp import SnowNLP
# with open('daoru.txt','r',encoding='utf-8') as f:
#     reader=f.readlines()
#     for key,item in enumerate(reader):
#         res=item.split()
#         num=res[0]
#         if num !="0" and num!="1":
#             print(key)
#         else:
#            with open('neg.txt','a',encoding='utf-8') as n:
#                 with open('pos.txt','a',encoding='utf-8') as p:
#                     if num=="0":
#                         n.write(res[1]+'\n')
#                     else:
#                         p.write(res[1]+'\n')

# sentiment.train('neg.txt','pos.txt')
# sentiment.save('weibo.marshal')
with open('daifenlei.txt','r',encoding='utf-8') as f:
    reader=f.readlines()
    list=[]
    for item in reader:
        mydict = {}
        text=item.strip()
        sn=SnowNLP(text)
        print("text: "+text+" senti: "+str(sn.sentiments))
        mydict['text']= text
        mydict['sentiment']=sn.sentiments
        list.append(mydict)
    print(list)
    newlist = sorted(list,key=lambda x:x['sentiment'])
    for i in newlist:
        print('text: '+i['text'])
        print(' senti:'+str(i['sentiment']))
        # for i in list:
        #     reg = i[0]
        #     mydict[reg] = i[1]




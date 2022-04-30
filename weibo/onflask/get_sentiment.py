from snownlp import SnowNLP
def getit(string:str):
    sn=SnowNLP(string)
    return sn.sentiments
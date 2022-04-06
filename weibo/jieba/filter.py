# coding=gb18030
import re
def filter_emoji(desstr, restr=''):
    # ���˳���Ӣ�ļ���������������ַ�
    res = re.compile("[^\\u4e00-\\u9fa5^a-z^A-Z^0-9]")
    return res.sub(restr, desstr)
# str='�ѹ�<span class="url-icon"><img alt=[��] src="https://h5.sinaimg.cn/m/emoticon/icon/default/d_lei-4cdf6ee412.png" style="width:1em; height:1em;" /></span>'
def filter_span_a(string):
    str=""
    flag = True
    for s in string:
        if flag:
            if s!='<':
                str=str+s
            else:
                flag=False
        else:
            if s != '>':
                continue
            else:
                flag=True
    return str
def filter_at(string):
    str = ""
    flag = True
    for s in string:
        if flag:
            if s!="@":
                str=str+s
            else:
                flag=False
        else:
            if s==":":
                flag=True
    return str

def filter_slash(string):
    return string.replace("//"," ")
def filter_str(string):
    str=string
    if "<span" in str or "<a" in str:  ##���˺���<span> �� <a>�����
        str=filter_span_a(str)
    if "@" in str:
        str=filter_at(str)
    if "//" in str:
        str=filter_slash(str)
    str=filter_emoji(str)
    return str

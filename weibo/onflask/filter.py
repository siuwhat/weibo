# coding=gb18030
import re
def filter_emoji(desstr, restr=''):
    # 过滤除中英文及数字以外的其他字符
    res = re.compile("[^\\u4e00-\\u9fa5^a-z^A-Z^0-9]")
    return res.sub(restr, desstr)
# str='难过<span class="url-icon"><img alt=[泪] src="https://h5.sinaimg.cn/m/emoticon/icon/default/d_lei-4cdf6ee412.png" style="width:1em; height:1em;" /></span>'
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
    if "<span" in str or "<a" in str:  ##过滤含有<span> 和 <a>的语句
        str=filter_span_a(str)
    if "@" in str:
        str=filter_at(str)
    if "//" in str:
        str=filter_slash(str)
    str=filter_emoji(str)
    if "回复" in str:
        str=str.replace("回复","")
    return str

print(filter_str("回复<a href=/n/我常威并不会武功>@我常威并不会武功</a>:这个全果都这样，不必黑<img alt=\"[doge]\" title=\"[doge]\" src=\"https://face.t.sinajs.cn/t4/appstyle/expression/ext/normal/a1/2018new_doge02_org.png\" /><img alt=\"[doge]\" title=\"[doge]\" src=\"https://face.t.sinajs.cn/t4/appstyle/expression/ext/normal/a1/2018new_doge02_org.png\" /><img alt=\"[doge]\" title=\"[doge]\" src=\"https://face.t.sinajs.cn/t4/appstyle/expression/ext/normal/a1/2018new_doge02_org.png\" />"))
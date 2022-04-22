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
            if s == '>':
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

def filter_hash(string):
    str = ""
    flag = True
    for s in string:
        if flag:
            if s != "#":
                str = str + s
            else:
                flag = False
        else:
            if s == "#":
                flag = True
    return str

def filter_slash(string):
    return string.replace("//"," ")
def filter_str(string):
    str=string
    if "<span" in str or "<a" in str:  ##过滤含有<span> 和 <a>的语句
        str=filter_span_a(str)
    if "#" in str:
        str=filter_hash(str)
    if "@" in str:
        str=filter_at(str)
    if "//" in str:
        str=filter_slash(str)
    str=filter_emoji(str)
    if "回复" in str:
        str=str.replace("回复","")
    return str

print(filter_str('<a  href="https://m.weibo.cn/search?containerid=231522type%3D1%26t%3D10%26q%3D%23%E9%95%BF%E6%98%A5%E5%AE%BD%E5%9F%8E+%E9%98%B2%E7%96%AB%23&extparam=%23%E9%95%BF%E6%98%A5%E5%AE%BD%E5%9F%8E+%E9%98%B2%E7%96%AB%23" data-hide=""><span class="surl-text">#长春宽城 防疫#</span></a> 离了个大谱 出不了门 抢不到菜 还没有物资支援 社区一刀切死统统封闭 老百姓在家等死吗<span class="url-icon"><img alt=[太开心] src="https://h5.sinaimg.cn/m/emoticon/icon/default/d_taikaixin-b7d86de3fd.png" style="width:1em; height:1em;" /></span>就这就这<span class="url-icon"><img alt=[太开心] src="https://h5.sinaimg.cn/m/emoticon/icon/default/d_taikaixin-b7d86de3fd.png" style="width:1em; height:1em;" /></span><span class="url-icon"><img alt=[太开心] src="https://h5.sinaimg.cn/m/emoticon/icon/default/d_taikaixin-b7d86de3fd.png" style="width:1em; height:1em;" /></span><span class="url-icon"><img alt=[太开心] src="https://h5.sinaimg.cn/m/emoticon/icon/default/d_taikaixin-b7d86de3fd.png" style="width:1em; height:1em;" /></span><span class="url-icon"><img alt=[太开心] src="https://h5.sinaimg.cn/m/emoticon/icon/default/d_taikaixin-b7d86de3fd.png" style="width:1em; height:1em;" /></span>'))
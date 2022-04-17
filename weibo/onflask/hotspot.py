# encoding=gbk
import pymysql
from pyecharts import options as opts
from pyecharts.charts import Bar
from datetime import datetime
from pyecharts.globals import ThemeType


def count():
    db = pymysql.connect(host='localhost', passwd='root', user='root', database='spider')
    flag = db.cursor()
    flag.execute('show tables;')
    table_list = flag.fetchall()
    # print(table_list)
    numlist={}
    for tablename in table_list:
        # print(tablename[0])
        if '20'in tablename[0]:
            flag.execute('select count(*) from '+tablename[0]+';')
            num=flag.fetchone()[0]
            name=tablename[0].replace('text','')
            numlist[name]=num
    # print(numlist)
    return numlist

def timer(timetext):
   year=timetext[:4]
   mon=timetext[4:6]
   day=timetext[6:len(timetext)+1]
   timelist=[year,mon,day]
   return '-'.join(timelist)

# for k,v in count().items():
#     print(timer(k))
#     str=datetime.strptime(timer(k),'%Y-%m-%d').date()
x=[datetime.strptime(timer(k),'%Y-%m-%d').date() for k in count().keys()]
y=count().values()

def mybar():
    return (Bar(init_opts=opts.InitOpts(width="1280px",height="600px",theme=ThemeType.SHINE),)
       .add_xaxis(x)
       .add_yaxis('每日评论数',list(y))
       .set_global_opts(title_opts=opts.TitleOpts(title="时域热点图",pos_left="60px",title_textstyle_opts=opts.TextStyleOpts(font_style="oblique")),
                        visualmap_opts=opts.VisualMapOpts(is_show=True,type_="color",min_=0,max_=1000,is_calculable = True,range_text=["High","Low"]),
                        legend_opts=opts.LegendOpts(is_show=False),
                        tooltip_opts=opts.TooltipOpts(trigger="axis",trigger_on="mousemove"),
                        toolbox_opts=opts.ToolboxOpts(feature=opts.ToolBoxFeatureOpts(data_zoom=None,brush=None,magic_type=opts.ToolBoxFeatureMagicTypeOpts(type_=["line","bar"]),data_view=None)),
                        datazoom_opts=opts.DataZoomOpts(range_start=0,range_end=100),
                        ).render_embed())



# print(count())
# for i in count().keys():
#     print(timer(i))




# encoding=gbk
import pymysql
from pyecharts import options as opts
from pyecharts.charts import Bar
from datetime import datetime, timedelta
from pyecharts.globals import ThemeType


def count():
    db = pymysql.connect(host='localhost', passwd='root', user='root', database='spider')
    flag = db.cursor()
    flag.execute('show tables;')
    table_list = flag.fetchall()
    # print(table_list)
    numdict={}

    for tablename in table_list:
        if '20'in tablename[0]:
            numlist = []
            for i in range(24):
                numlist.append(0)
            flag.execute('select time from '+tablename[0]+';')
            time_res_list=flag.fetchall()
            for t in time_res_list:
                hour = int(t[0].split()[1].split(':')[0])
                numlist[hour]=numlist[hour]+1
            name=tablename[0].replace('text','')
            if sum(numlist)>500:
                numdict[name]=numlist
    return numdict

def timer(timetext):
   year=timetext[:4]
   mon=timetext[4:6]
   day=timetext[6:len(timetext)+1]
   timelist=[year,mon,day]
   return '-'.join(timelist)

# for k,v in count().items():
#     print(timer(k))
#     str=datetime.strptime(timer(k),'%Y-%m-%d').date()
x=[datetime.strptime(timer(k),'%Y-%m-%d') for k in count().keys()]
x_timelist=[]
for t in x:
    ct=t
    for length in range(24):
        x_timelist.append(ct)
        ct=ct+timedelta(hours=1)
y=[j for i in count().values() for j in i]

def mybar():
    return (Bar(init_opts=opts.InitOpts(width="1280px",height="600px",theme=ThemeType.SHINE),)
       .add_xaxis(x_timelist)
       .add_yaxis('每小时评论数',list(y))
       .set_global_opts(title_opts=opts.TitleOpts(title="时间热点图",pos_left="60px",title_textstyle_opts=opts.TextStyleOpts(font_style="oblique")),
                        visualmap_opts=opts.VisualMapOpts(is_show=True,type_="color",min_=0,max_=1000,is_calculable = True,range_text=["High","Low"]),
                        legend_opts=opts.LegendOpts(is_show=False),
                        tooltip_opts=opts.TooltipOpts(trigger="axis",trigger_on="mousemove"),
                        toolbox_opts=opts.ToolboxOpts(feature=opts.ToolBoxFeatureOpts(data_zoom=None,brush=None,magic_type=opts.ToolBoxFeatureMagicTypeOpts(type_=["line","bar"]),data_view=None)),
                        datazoom_opts=opts.DataZoomOpts(range_start=0,range_end=100,type_='inside'),
                        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False, axistick_opts=opts.AxisTickOpts()),
                        ).render_embed())



# print(count())
# for i in count().keys():
#     print(timer(i))




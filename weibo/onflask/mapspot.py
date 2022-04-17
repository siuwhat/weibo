# encoding=gbk
from pyecharts import options as opts
from pyecharts.charts import Map,Grid,Bar
import pymysql
from pyecharts.globals import ThemeType

allregiondict="河北山西辽宁吉林黑龙江江苏浙江安徽福建江西山东河南湖北湖南广东海南四川贵州云南陕西甘肃青海台湾内蒙古广西西藏宁夏新疆北京天津上海重庆香港澳门"

def allgeo():
    db = pymysql.connect(host='localhost', passwd='root', user='root', database='spider')
    flag = db.cursor()
    flag.execute("select ipregion from text;")
    db.commit()
    region_list=flag.fetchall()
    dict={}
    list=[]
    for i in region_list:
        str=i[0]
        str=str.replace(':','：')
        reg=str.split('：')[1]
        if reg=='中国香港':
            reg="香港"
        elif reg=='中国台湾':
            reg="台湾"
        if reg in allregiondict:
            if dict.get(reg)!=None:
                dict[reg]=dict[reg]+1
            else:
                dict[reg]=1
    for k,v in dict.items():
        newlist=[]
        newlist.append(k)
        newlist.append(v)
        list.append(newlist)

    return  list
def allreg():
    db = pymysql.connect(host='localhost', passwd='root', user='root', database='spider')
    flag = db.cursor()
    flag.execute("select ipregion from text;")
    db.commit()
    region_list = flag.fetchall()
    dict = {}
    for i in region_list:
        str = i[0]
        str = str.replace(':', '：')
        reg = str.split('：')[1]
        if reg == '中国香港':
            reg = "香港"
        elif reg == '中国台湾':
            reg = "台湾"
        if reg in allregiondict:
            if dict.get(reg) != None:
                dict[reg] = dict[reg] + 1
            else:
                dict[reg] = 1
    return dict
def sort_dict(mydict):
    dict={}
    list=sorted(mydict.items(),key=lambda d:d[-1],reverse=True)
    # print(list)
    for i in list:
        reg=i[0]
        dict[reg] = i[1]

    return dict

# print(sort_dict(allreg()))
def mygeo():
    map=(Map(init_opts=opts.InitOpts(width="1050px", height="600px"))
    .add(series_name='地域热点', data_pair=allgeo(), maptype='china', aspect_scale=0.8, )
    .set_global_opts(
                     legend_opts=opts.LegendOpts(is_show=False),
                     tooltip_opts=opts.TooltipOpts(axis_pointer_type="shadow", background_color="gray"),
                    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True, color="black"),
                     areastyle_opts=opts.AreaStyleOpts(color="gray")))
    bar=(Bar().add_xaxis(list(sort_dict(allreg()).keys())).add_yaxis("",list(sort_dict(allreg()).values()),label_opts=opts.LabelOpts(is_show=True, position="right", formatter="{b} : {c}")).reversal_axis().set_global_opts(
        visualmap_opts=opts.VisualMapOpts(type_="color", orient='vertical', range_text=["High", "Low"],
                                          pos_left="left", is_inverse=False,pos_top="top",min_=0,max_=500 ),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
        title_opts=opts.TitleOpts("地域热点图", title_textstyle_opts=opts.TextStyleOpts(font_style="oblique"),pos_top="40%")

    ))

    return (Grid(init_opts=opts.InitOpts(width="1920px", height="1080px")).add(bar,grid_opts=opts.GridOpts(pos_top="50%",pos_right="70%",pos_left="5px")).add(map,grid_opts=opts.GridOpts(pos_bottom="50%")).render_embed())




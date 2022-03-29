from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
x=[1,2,3,4,5]
y=[14,32,4,12,44]
bar=(Bar(init_opts=opts.InitOpts(theme=ThemeType.DARK)).add_xaxis(x).add_yaxis('name',y).set_global_opts(title_opts=opts.TitleOpts(title="主标题",subtitle='副标题')))
bar.render()

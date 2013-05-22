#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cairo 
import pycha.pie
import pycha.bar
import pycha.scatter
import pycha.stackedbar
import pycha.line

#设置画布
def set_charvalue():
    width,height=600,600 
    surface=cairo.ImageSurface(cairo.FORMAT_ARGB32,width,height) 
    return surface
    
#画饼图
def draw_pie(surface, options, dataSet):
    chart=pycha.pie.PieChart(surface,options) 
    chart.addDataset(dataSet) 
    chart.render() 
    surface.write_to_png('pie.png') 

#垂直直方图
def draw_vertical_bar(surface, options, dataSet):
    chart=pycha.bar.VerticalBarChart(surface,options) 
    chart.addDataset(dataSet) 
    chart.render() 
    surface.write_to_png('vertical_bar.png')   
 
#垂直水平直方图    
def draw_horizontal_bar(surface, options, dataSet):
    chart = pycha.bar.HorizontalBarChart(surface,options) 
    chart.addDataset(dataSet) 
    chart.render() 
    surface.write_to_png('horizontal_bar.png')   
    
#线图    
def draw_line(surface, options, dataSet):
    chart = pycha.line.LineChart(surface,options) 
    chart.addDataset(dataSet) 
    chart.render() 
    surface.write_to_png('line.png')      

#点图    
def draw_scatterplot(surface, options, dataSet):
    chart = pycha.scatter.ScatterplotChart(surface,options) 
    chart.addDataset(dataSet) 
    chart.render() 
    surface.write_to_png('scatterplotChart.png')         

#垂直块图     
def draw_stackedverticalbarChar(surface, options, dataSet):
    chart = pycha.stackedbar.StackedVerticalBarChart(surface,options) 
    chart.addDataset(dataSet) 
    chart.render() 
    surface.write_to_png('stackedVerticalBarChart.png')      

#水平块图
def draw_stackedhorizontalbarChart(surface, options, dataSet):
    chart = pycha.stackedbar.StackedHorizontalBarChart(surface,options) 
    chart.addDataset(dataSet) 
    chart.render() 
    surface.write_to_png('stackedhorizontalbarChart.png')    
    
if __name__ == '__main__':
    '''
    Function:使用pycha画各种图表
    Input：NONE
    Output: NONE
    author: socrates
    blog:http://blog.csdn.net/dyx1024
    date:2012-02-28
    '''
    #数据来源
    dataSet=( 
             ('iphone',((0,1),(1,3),(2,2.5))), 
             ('htc',((0,2),(1,4),(2,3))), 
             ('hw',((0,5),(1,1,),(2,0.5))), 
             ('zte',((0,3),(1,2,),(2,1.5))), 
    ) 
    
    #图像属性定义
    options={ 
                'legend':{'hide':False}, 
                'title':'手机销售量分布图(by dyx1024)',
                'titleColor':'#0000ff',
                # 'titleFont':'字体',
                # 需要是系统里带的字体，fc-list 列出Ubuntu里安装的字体
                'titleFont':'文泉驛微米黑',
                'background':{'chartColor': '#ffffff'}, 
                'axis':{'labelColor':'#ff0000'},
    }     
    
    #自定义样式
    options1={ 
       'axis': {
            'x': {                       #x轴
                'label': 'month',        #标签名称
                'rotate': 25,            
            },
            'y': {                       #y轴
                'tickCount': 8,          #横线个数
                'rotate': 25,
                'label': 'count'
            }
        },
        'background': {
            'chartColor': '#ffffff',     #图表背景色
            'baseColor': '#ffffff',      #边框颜色
            'lineColor': '#0000ff'       #横线颜色
        },
        'colorScheme': {
            'name': 'gradient',
            'args': {
                'initialColor': '#CD3700', #图表颜色
            },
        },
        'legend': {
            'hide': True,     #是否隐藏图标示例
        },
        'padding': {
            'left': 10,       #左边框
            'bottom': 10,     #底边框
        },
        'title': u'图片标题 (by dyx1024)' #图片标题
            }     
    
    
    surface = set_charvalue()
    
    #根据需要调用不同函数画不同形状的图
    draw_pie(surface, options, dataSet)
    draw_vertical_bar(surface, options, dataSet)
    draw_horizontal_bar(surface, options, dataSet)
    draw_scatterplot(surface, options, dataSet)
    draw_stackedverticalbarChar(surface, options, dataSet)
    draw_stackedhorizontalbarChart(surface, options, dataSet)
    draw_line(surface, options, dataSet)

    # draw_line(surface, options1, dataSet)

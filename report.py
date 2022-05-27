
from turtle import title
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Table, Spacer,Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.charts.linecharts import HorizontalLineChart
from reportlab.graphics.shapes import Drawing

#cars report
def generate_report(file,title, summary, table_content ):
    print('generating cars report....')

    report= SimpleDocTemplate(file)
    styles= getSampleStyleSheet()

    report_title= Paragraph(title,styles['h1'])
    report_content= Paragraph(summary,styles["BodyText"])
    table_style=[
        ('GRID', (0,0), (-1,0), 2, colors.black),
        ('BACKGROUND', (0,0), (-1,0), colors.lightskyblue),
        ('GRID', (0,1), (-1,-1), 2, colors.black),
    ]
    report_table= Table(data=table_content, style=table_style)
    report.build([report_title, report_content, report_table])

#line chart
def generate_linechart(file,summary,data_list,year_list):
    print('generating linechart....')

    draw= Drawing(500*500)
    report=SimpleDocTemplate(file)
    styles=getSampleStyleSheet()
    lc=HorizontalLineChart()

    lc.x= 1
    lc.y= -150
    lc.height= 300
    lc.width= 450
    lc.data=[data_list]
    lc.joinedLines = 2
    catname=str(year_list).strip('[]').split(',')
    lc.categoryAxis.categoryNames=catname
    lc.categoryAxis.labels.boxAnchor ='n'
    lc.valueAxis.valueMin=0
    lc.valueAxis.valueMax=20000
    lc.valueAxis.valueStep= 2000
    lc.lines[0].strokeWidth= 2
    
    title= Paragraph(summary,styles['h1'])
    draw.add(lc)
    report.build([title,draw])


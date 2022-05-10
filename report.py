
from turtle import title
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Table, Spacer,Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(file,title, summary, table_content ):
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
from functools import total_ordering
import os
import json
from collections import defaultdict
import getpass
import report
import emails

def process_data():
    
    total_sales=0
    dic=defaultdict(int)

    for data in cars:
        price=str(data['price']).strip("$")
        total_revenue= float(price )* float(data['total_sales'])
    
        #most saled car
        if data['total_sales'] > total_sales :
            total_sales = data['total_sales']
            total_saled_brand,total_saled_model  = data['car']['car_make'],data['car']['car_model']

        #most popular year
        dic[data['car']['car_year']] += data['total_sales']

    sortesd_dic= sorted(dic.items(), key=lambda item: item[1])
    tmp=str(sortesd_dic[-1]).strip('()')
    pop_year,pop_sales= tmp.split(',')

    summary=[
        f"Total revenue made = {total_revenue}",
        f"{total_saled_brand} {total_saled_model} is most saled car and sales was {total_sales}",
        f"Popuar year was {pop_year} and sales of that year {pop_sales}",
    ]

    #making sales list by year
    year_list=[]
    data_list=[]
    data_tup=tuple
    i=0
    i1=True
    for k in sorted(dic) :
        if i==0 and i1==True:
            year_list.append(k)
            data_list.append(dic[k])       
            i1=False
        if i==2 :
            year_list.append(k)
            data_list.append(dic[k])
            i=0
        i+=1
    data_tup=tuple(data_list)
    #print(year_list,data_tup)

    return summary,year_list,data_tup

def dic_to_lst():
    lst=[]
    lst.append(["id","car","price","total_sales"])
    for data in cars:
        lst.append( [
            data['id'],
            data['car']['car_make']+" "+data['car']['car_model'],
            data['price'],
            data['total_sales'],
        ])
    #print(lst)
    return lst

def create_report(summary):
    file='docs/car.pdf'
    title='Sale report'
    contents="<br/>".join(summary)
    table_content= dic_to_lst()

    report.generate_report(file,title,contents, table_content)
    print('report ok')

def create_linechart(year,data):
    file='docs/line_chart.pdf'
    summary='Sales chart'
    report.generate_linechart(file=file,summary=summary,year_list=year,data_list=data)
    print('line chart ok')

def send_email(summary):
    sender=str(input('enter sender mail id : '))
    recipient= str(input('enter recipient mail id : '))
    pswd =getpass.getpass()
    print(pswd)
    subject = 'Sales report'
    body = "\n".join(summary)
    attachment = 'docs/car.pdf'

    #emails.genrate_email(sender, recipient, subject, body, attachment,pswd)

if __name__ == '__main__' :

    with open('tmp/car_details.json') as j:
        cars = json.load(j)

    summary,year,data=process_data()
    #create_report(summary)
    #send_email(summary)
    create_linechart(year,data)
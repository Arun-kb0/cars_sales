from functools import total_ordering
import os
import json
from collections import defaultdict
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
    return summary

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
    file='car.pdf'
    title='Sale report'
    contents="<br/>".join(summary)
    table_content= dic_to_lst()

    report.generate_report(file,title,contents, table_content)
    print('report ok')

def send_email(summary):
    sender='12arunkb@gmail.com'
    recipient= 'arun.kb076@gmail.com'
    pswd ='qhghpgclfhsresxa'
    subject = 'Sales report'
    body = "\n".join(summary)
    attachment = 'car.pdf'

    emails.genrate_email(sender, recipient, subject, body, attachment,pswd)

if __name__ == '__main__' :

    with open('car_details.json') as j:
        cars = json.load(j)

    summary=process_data()
    create_report(summary)
    send_email(summary)
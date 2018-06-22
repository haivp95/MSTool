from django.shortcuts import render
from django.db import connection
import requests
import json
import cx_Oracle

def APIvnpost(request):
    # response = requests.get('https://ctt.vnpost.vn/serviceApi/v1/getDelivery?token=ca608900-02a0-4a0d-aefa-6ad4ae9a5793&fromRecord=0')
    # vnpAPI = response.json()
    # return render(request, 'IndexVNP.html', {
    #     'Deliverys' : vnpAPI['Deliverys'],
    # })

    con = cx_Oracle.connect('APP_REPORT_INT[AP_OPS]/Xcvert6uiopp@DBHDWVN-VIETTEL.PROD.ITC.HCNET.VN:1521/HDWVN.HOMECREDIT.VN')
    print (con.version)
    cursor = con.cursor()
    cursor.execute('select * from T_OPS_MIS_CUSTOMER_FEEDBACK')
    list = dictfetchall(cursor)
    cursor.close()
    con.close
    return render(request, 'IndexVNP.html', {
        'Deliverys' : list,
    })

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]



from django.shortcuts import render
import requests
import json

def APIvnpost(request):
    response = requests.get('https://ctt.vnpost.vn/serviceApi/v1/getDelivery?token=ca608900-02a0-4a0d-aefa-6ad4ae9a5793&fromRecord=0')
    vnpAPI = response.json()
    return render(request, 'IndexVNP.html', {
        'Deliverys' : vnpAPI['Deliverys'],
    })


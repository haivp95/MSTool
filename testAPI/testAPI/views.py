from django.shortcuts import render
import requests
import json


def testAPI(request):
    response = requests.get('https://ctt.vnpost.vn/serviceApi/v1/getDelivery?token=ca608900-02a0-4a0d-aefa-6ad4ae9a5793&fromRecord=0&toRecord=100')
    #headers = {'Accept': 'application/json'}
    vnpAPI = response.json()
    return render(request, 'home.html', {
        'Deliverys' : vnpAPI['Deliverys'],
       
    })
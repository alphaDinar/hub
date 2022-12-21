from django.shortcuts import render,redirect
import requests

def home(request):
  return render(request, 'home.html')

import threading,json
from urllib.parse import urlparse

def momo(request):
  if request.method == 'POST':
    mobileNumber = request.POST.get('mobile')
    amount = float(request.POST.get('amount'))
    ref = request.POST.get('ref')
    book = []
    #x = threading.Thread(target=request_momo, args=(amount,ref,mobileNumber))
    #x.start()
    callback_uri = str(urlparse('http://127.0.0.1:8000/callback'))
    print(callback_uri)
    print(f'{callback_uri}')

    user2 = 'evviouhu'
    pass2 = 'lrrnebkb'
    data = {
          "amount": amount,
          "title": "string",
          "description": "string",
          "clientReference": 'string',
          "callbackUrl": 'https://www.google.com/',
          "cancellationUrl": "http://127.0.0.1:8000/cancel",
          "returnUrl": "http://127.0.0.1:8000/return",
      }
    response = requests.post(f'https://devp-reqsendmoney-230622-api.hubtel.com/request-money/{mobileNumber}', auth=(user2,pass2), json=data)
    raw = response.content.decode('utf-8')
    print(response.status_code)
    lis_ = json.loads(raw)
    v = lis_['data']['paylinkUrl']
    #pay_status = 
    print(lis_)
    #messageId = ''
    #response_status = requests.post(f'https://devp-sms03726-api.hubtel.com/v1/messages/{messageId}')

    if response.status_code == 201: 
      return redirect(f'{v}')
  return render(request, 'momo.html')

#def request_momo(amount,ref,mobileNumber): 
#    print(v)


def sms(request):
  mobileNumber = '0558420368'

  url = f'https://devp-reqsendmoney-230622-api.hubtel.com/request-money/{mobileNumber}'
  
  data = {
      "amount": 1,
      "title": "string",
      "description": "string",
      "clientReference": 'string',
      "callbackUrl": 'https://hub-production-ed85.up.railway.app/callback',
      "cancellationUrl": "https://hub-production-ed85.up.railway.app/cancel",
      "returnUrl": "https://hub-production-ed85.up.railway.app/return",
  }  

  headers = {
      "accept": "application/json",
      "content-type": "application/json",
      "authorization": "Basic ZXZ2aW91aHU6bHJybmVia2I="
  }
  response = requests.post(url, headers=headers, json=data)

  lin = json.loads(response.text)['data']['paylinkUrl']
  context = {
    'x' : lin
  } 
  return render(request, 'sms.html', context)


def callback(request):
  t = requests.post('https://hub-production-ed85.up.railway.app/callback')
  context = {
    't' : t.text
  }
  return render(request, 'callback.html', context)

def cancel(request):
  return render(request, 'cancel.html')


def returns(request):
  
  return render(request, 'return.html')
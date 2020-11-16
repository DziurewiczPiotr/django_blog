from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse

entityid = "8ac7a4c86d71666e016d7299e46503b4"
bearer = "OGFjN2E0Yzk2ZDcxNTllMDAxNmQ3MjU0MzA0YTA1MjJ8amhRdzZtSmdiUg=="

def home(request):
    return HttpResponse("YO HOME!")

@csrf_protect
def test3ds(request):

    class Card:
        number = "4000000000000044"
        type = "VISA"


    url = "https://test.oppwa.com/v1/payments"

    payload = (
        f"authentication.entityId={entityid}"
        "&amount=12.00"
        "&currency=EUR"
        f"&paymentBrand={Card.type}"
        "&paymentType=PA"
        "&merchantTransactionId=order99234"
        "&transactionCategory=EC"
        f"&card.number={Card.number}"
        "&card.expiryMonth=12"
        "&card.expiryYear=2025"
        "&card.cvv=123"
        "&card.holder=John%20Smith"
        "&merchant.name=MerchantCo"
        "&merchant.city=Munich"
        "&merchant.country=DE"
        "&merchant.mcc=5399"
        "&shopperResultUrl=https%3A//success.example.siabadaba"
        "&customer.ip=192.168.0.1"
        "&customer.browser.acceptHeader=text/html&customer.browser.screenColorDepth=48"
        "&customer.browser.javaEnabled=false"
        "&customer.browser.language=de"
        "&customer.browser.screenHeight=1440"
        "&customer.browser.screenWidth=2560"
        "&customer.browser.timezone=60"
        "&customer.browser.challengeWindow=4"
        "&customer.browser.userAgent=Mozilla/4.0%20%28MSIE%206.0%3B%20Windows%20NT%205.0%29"
        "&testMode=INTERNAL"
        "&customer.browser.javascriptEnabled=true"
    )
    headers = {
        "Authorization": f"Bearer {bearer}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()

    data = {
        "response": response
    }

    return render(request, "blog/iframe.html", context=data)

@csrf_protect
def get_status(request, transaction_id):
    url = f"https://test.oppwa.com/v1/query/{transaction_id}?entityId={entityid}"

    payload={}
    headers = {
       "Authorization": f"Bearer {bearer}"
    }

    response = requests.request("GET", url, headers=headers, data=payload).json()

    return JsonResponse(response)
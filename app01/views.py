from django.shortcuts import render,HttpResponse
from app01 import tasks
from celery.result import AsyncResult
# Create your views here.


def index(request):

    res = tasks.add.delay(3,4)
    print("res:" ,res)
    return HttpResponse(res.task_id)


def task_res(request):

    result = AsyncResult("6c15eb86-d0ff-48bf-b134-d26fc56b9a4d")
    # return HttpResponse(result.get())
    return HttpResponse(result.status)

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("first response")

def info(request):
    number = 55
    list = [1,2,3,4]

    return HttpResponse("info response => " + str(number) + str(list) )


def numer(request, numer_id):
    return HttpResponse("hardware numer_inwemtarzowy => " + str(numer_id) )
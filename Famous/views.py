from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print("Hello")
    #return HttpResponse("Hello")
    return render(request, 'Famous/index.html')



def restaurantDetail(request):
    # return HttpResponse("Hello")
    return render(request, 'Famous/restaurantDetail.html')



def restaurantCreate(request):
    ## return HttpResponse("Hello")
    return render(request, 'Famous/restaurantCreate.html')



def categoryCreate(request):
    ##return HttpResponse("Hello")
    return render(request, 'Famous/categoryCreate.html')
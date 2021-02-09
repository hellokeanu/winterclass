from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Famous.models import Category
from django.urls import reverse

def index(request):
    #query=request.GET['category']
    categories = Category.objects.all()
    content ={'BigOne': categories}
    #print("Hello")
    #return HttpResponse("Hello")
    return render(request, 'Famous/index.html',content)

def restaurantDetail(request):
    # return HttpResponse("Hello")
    return render(request, 'Famous/restaurantDetail.html')

def restaurantCreate(request):
    ## return HttpResponse("Hello")
    return render(request, 'Famous/restaurantCreate.html')


# 만들자고 보여지는 상황을 만드어 준다
def categoryCreate(request):
    categories = Category.objects.all()
    content = {'BigOne': categories}
    return render(request, 'Famous/categoryCreate.html',content)


# 실제 DB에서 만들어 지는 작업
def Create_Category(request):
    givenname = request.POST['categoryName']
    new_categroy = Category(category_name= givenname)
    new_categroy.save()
    return HttpResponseRedirect(reverse('index'))


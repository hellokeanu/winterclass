from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Famous.models import Field, Human, Task, Work
from django.urls import reverse
import pandas as pd
from django.db import DefaultConnectionProxy
connection = DefaultConnectionProxy()
import json


def FieldReader(query):
    newquery={}
    for key in list(query.keys()):
        if key in ['fieldname']:
            if query[key]:
                newquery[key] = query[key]
    # Quering
    newquery = str(Field.objects.all().filter(**newquery).query)
    FieldList = pd.read_sql_query(newquery, connection)
    print(FieldList)

    return FieldList

def HuamnReader(query):
    newquery={}
    for key in list(query.keys()):
        if key in ['humanname']:
            if query[key]:
                newquery[key] = query[key]
    # Quering
    newquery = str(Human.objects.all().filter(**newquery).query)
    List = pd.read_sql_query(newquery, connection)
    print(List)

    return List



def WorkReader(query):
    newquery={}
    for key in list(query.keys()):
        if key in ['year','month','day','count','extend','field','human','task']:
            if query[key]:
                newquery[key] = query[key]
    # Quering
    newquery = str(Work.objects.all().filter(**newquery).query)
    List = pd.read_sql_query(newquery, connection)
    print(List)

    return List



def TaskReader(query):
    newquery={}
    for key in list(query.keys()):
        if key in ['taskname']:
            if query[key]:
                newquery[key] = query[key]
    # Quering
    newquery = str(Task.objects.all().filter(**newquery).query)
    List = pd.read_sql_query(newquery, connection)
    print(List)

    return List










def FieldR(request):
    # query=request.GET['year']
    query = request.GET
    FieldList=FieldReader(query)
    result = FieldList.to_html()
    #result = FieldList.to_json(orient="split", force_ascii=False)
    return HttpResponse(result)

def HumanR(request):
    # query=request.GET['year']
    query = request.GET
    List=HuamnReader(query)
    result = List.to_html()
    #result = FieldList.to_json(orient="split", force_ascii=False)
    return HttpResponse(result)

def WorkR(request):
    # query=request.GET['year']
    query = request.GET
    WorkList = WorkReader(query)
    FieldList = FieldReader(query)
    TaskList = TaskReader(query)
    HumanList = HuamnReader(query)

    HumanList2=HumanList.rename(columns={'id': 'human_id'})
    WorkList2=pd.merge(WorkList,HumanList2,how='left', on=['human_id'])
    WorkList2=WorkList2.drop(columns='human_id')



    result = WorkList.to_html()
    #result = FieldList.to_json(orient="split", force_ascii=False)
    return HttpResponse(result)










#
#
#
#
# def index(request):
#     #query=request.GET['category']
#     categories = Category.objects.all()
#     content ={'BigOne': categories}
#     #print("Hello")
#     #return HttpResponse("Hello")
#     return render(request, 'Famous/index.html',content)
#
# def restaurantDetail(request):
#     # return HttpResponse("Hello")
#     return render(request, 'Famous/restaurantDetail.html')
#
# def restaurantCreate(request):
#     ## return HttpResponse("Hello")
#     categories = Category.objects.all()
#     content = {'categories': categories}
#     return render(request, 'Famous/restaurantCreate.html',content)
#
# def Create_restaurant(request):
#
#     category_id = request.POST['resCategory']
#     resName = request.POST['resTitle']
#     resLink = request.POST['resLink']
#     resContent = request.POST['resContent']
#     resLoc = request.POST['resLoc']
#
#     new_Res = Restaurant(category=Category.objects.get(id=category_id),
#                          restaurant_name=resName,
#                          restaurant_link=resLink,
#                          restaurant_content=resContent,
#                          restaurant_keyword=resLoc)
#
#     new_Res.save()
#     #return HttpResponse("Create_Restaurant")
#     return HttpResponseRedirect(reverse('index'))
#
#
#
#
# # 만들자고 보여지는 상황을 만드어 준다
# def categoryCreate(request):
#     categories = Category.objects.all()
#     content = {'BigOne': categories}
#     return render(request, 'Famous/categoryCreate.html',content)
#
#
# # 실제 DB에서 만들어 지는 작업
# def Create_Category(request):
#     givenname = request.POST['categoryName']
#     new_categroy = Category(category_name= givenname)
#     new_categroy.save()
#     return HttpResponseRedirect(reverse('index'))
#
#
# def Delete_category(request):
#     category_id=request.POST['categoryId']
#     delete_category = Category.objects.get(id=category_id)
#     delete_category.delete()
#     return HttpResponseRedirect(reverse('index'))
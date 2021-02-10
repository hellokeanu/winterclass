from django.urls import path, include
from Famous import views
#from Famous.views import index as myoldindex


urlpatterns = [

    path('FieldR/', views.FieldR, name='FieldR'),

    path('', views.index, name='index'),
    path('restaurantDetail/', views.restaurantDetail, name='restaurantDetail'),
    path('restaurantCreate/', views.restaurantCreate, name='restaurantCreate'),
    path('restaurantCreate/create', views.Create_restaurant, name='restaurantCreate'),
    path('categoryCreate/', views.categoryCreate, name='categoryCreate'),
    path('categoryCreate/create', views.Create_Category, name='Create_Category'),
    path('categoryCreate/delete', views.Delete_category, name='Delete_category'),




]

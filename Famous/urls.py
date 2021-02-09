from django.urls import path, include
from Famous import views
#from Famous.views import index as myoldindex


urlpatterns = [
    path('', views.index, name='index'),
    path('restaurantDetail/', views.restaurantDetail, name='restaurantDetail'),
    path('restaurantCreate/', views.restaurantCreate, name='restaurantCreate'),
    path('categoryCreate/', views.categoryCreate, name='categoryCreate'),
    path('categoryCreate/create', views.Create_Category, name='categoryCreate'),
]

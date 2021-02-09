from django.urls import path, include
from Famous import views
#from Famous.views import index as myoldindex


urlpatterns = [
    path('', views.index, name='index'),
    path('restaurantDetail/', views.restaurantDetail, name='index'),
    path('restaurantCreate/', views.restaurantCreate, name='index'),
    path('categoryCreate/', views.categoryCreate, name='index'),
]

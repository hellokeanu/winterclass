from django.urls import path, include
from Famous import views
#from Famous.views import index as myoldindex


urlpatterns = [
    path('', views.index, name='index')
]

from django.urls import path
from home import views

urlpatterns = [
    path('', views.miniwebsite, name='miniwebsite')
    #,
    # path(r'^$', views.miniwebsite, name='miniwebsite')
]
from django.contrib import admin
from django.urls import path, re_path
from django.urls import include
from django.conf.urls import url
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.Home, name='Home'),
    url(r'^ReturnPredict$', views.Predict, name='Predict'),

    url(r'^Graph$', views.showGraph, name='showGraph'),
]

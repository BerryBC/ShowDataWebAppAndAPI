'''
@Descripttion: URL 解析
@Author: BerryBC
@Date: 2020-02-04 21:40:56
@LastEditors  : BerryBC
@LastEditTime : 2020-02-05 10:46:32
'''
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.funMain, name='Main'),
    path('cantacc/', views.funCannotAccess, name='Main'),
    path('notadm/', views.funNotAdm, name='Main'),
    path('user/', include('UserCtrl.urls')),
]

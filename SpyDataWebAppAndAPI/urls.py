'''
@Descripttion: URL 解析
@Author: BerryBC
@Date: 2020-02-04 21:40:56
@LastEditors  : BerryBC
@LastEditTime : 2020-02-04 21:49:15
'''
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.funMain, name='Main'),
]

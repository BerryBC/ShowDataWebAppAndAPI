'''
@Descripttion: 解释数据页面 URL 
@Author: BerryBC
@Date: 2020-02-05 13:01:03
@LastEditors  : BerryBC
@LastEditTime : 2020-02-05 13:41:23
'''

from django.urls import path
from . import views

urlpatterns = [
    path('emorecog/', views.funEmoRecog, name='ManageData'),
    path('insertsample/', views.funInsertSample, name='ManageData'),
    path('reuselinkmgt/', views.funReuseLinkMGT, name='ManageData'),
]

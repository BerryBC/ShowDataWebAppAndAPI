'''
@Descripttion: 解释数据页面 URL 
@Author: BerryBC
@Date: 2020-02-05 13:01:03
@LastEditors  : BerryBC
@LastEditTime : 2020-02-07 14:56:25
'''

from django.urls import path
from . import views

urlpatterns = [
    path('emorecog/', views.funEmoRecog, name='ManageData'),
    path('insertsample/', views.funInsertSample, name='ManageData'),
    path('reuselinkmgt/', views.funReuseLinkMGT, name='ManageData'),
    path('randdata/', views.apiLoadRandSample, name='ManageData'),
    path('confirmsample/', views.apiConfirmSample, name='ManageData'),
    path('insertonesample/', views.apiInsertSample, name='ManageData'),
    path('insertnewreusablesite/', views.apiInsertReusableSite, name='ManageData'),
    path('getallreuseablesite/', views.apiGetReusableSite, name='ManageData'),
    path('deletereusablepage/', views.apiDeleteReusableSite, name='ManageData'),
    path('deletesamplewithkw/', views.apiDeleteSampleWithKeyW, name='ManageData'),
    path('deletesamplepage/', views.funDeleteSampleKWPage, name='ManageData'),
    path('getdatacount/', views.apiLoadAllTableCount, name='ManageData'),
    path('getdatacountpage/', views.funLoadTableDataCount, name='ManageData'),

]

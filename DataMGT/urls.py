'''
@Descripttion: 解释数据页面 URL 
@Author: BerryBC
@Date: 2020-02-05 13:01:03
@LastEditors: BerryBC
@LastEditTime: 2020-02-24 23:49:11
'''

from django.urls import path
from . import views

urlpatterns = [
    # 页面引用
    path('emorecog/', views.funEmoRecog, name='ManageData'),
    path('insertsample/', views.funInsertSample, name='ManageData'),
    path('reuselinkmgt/', views.funReuseLinkMGT, name='ManageData'),
    path('deletesamplepage/', views.funDeleteSampleKWPage, name='ManageData'),
    path('getdatacountpage/', views.funLoadTableDataCount, name='ManageData'),
    path('custommgt/', views.funMGTCustom, name='ManageData'),
    path('spydata/', views.funSpyDataCheck, name='ManageData'),
    path('sklc/', views.funSklearnModelCreat, name='ManageData'),



    # 样本管理相关页面
    path('randdata/', views.apiLoadRandSample, name='ManageData'),
    path('confirmsample/', views.apiConfirmSample, name='ManageData'),
    path('insertonesample/', views.apiInsertSample, name='ManageData'),
    path('deletesamplewithkw/', views.apiDeleteSampleWithKeyW, name='ManageData'),

    # 重用页面管理
    path('insertnewreusablesite/', views.apiInsertReusableSite, name='ManageData'),
    path('getallreuseablesite/', views.apiGetReusableSite, name='ManageData'),
    path('deletereusablepage/', views.apiDeleteReusableSite, name='ManageData'),

    # 读取全部信息API
    path('getdatacount/', views.apiLoadAllTableCount, name='ManageData'),

    # 客制化信息读取
    path('getallcustominfo/', views.apiGetCustom, name='ManageData'),
    path('insertcustominfo/', views.apiInsertCustom, name='ManageData'),
    path('deletecustominfo/', views.apiDeleteCustom, name='ManageData'),

    # 试爬网页
    path('spydatawithtag/', views.apiSpyDataWithTag, name='ManageData'),

    # 创建 sklearn 模型    
    # path('sklcws/', views.wsCreatSklearnModel, name='ManageData'),
    
]

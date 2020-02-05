'''
@Descripttion: UserCtl App 下 URL 解释
@Author: BerryBC
@Date: 2020-02-05 10:31:28
@LastEditors  : BerryBC
@LastEditTime : 2020-02-05 10:31:55
'''
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.funLogin,name='Login'),
    path('manageuser/', views.funUserManage,name='ManageUser'),
    path('userreg/', views.apiUserRegistration,name='ManageUser'),
    path('userlog/', views.apiUserLogin,name='ManageUser'),
    path('userlist/', views.apiUserList,name='ManageUser'),
    path('userrspwd/', views.apiResetPasswork,name='ManageUser'),
    path('userrspw/', views.apiResetPower,name='ManageUser'),
    path('userdel/', views.apiDeleteUser,name='ManageUser'),

]

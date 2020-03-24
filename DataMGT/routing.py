'''
@Descripttion: 
@Author: BerryBC
@Date: 2020-02-24 23:03:32
@LastEditors: BerryBC
@LastEditTime: 2020-02-25 00:03:24
'''
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path('ws/data/sklcws/', consumers.wsCreatSklearnModel),
]
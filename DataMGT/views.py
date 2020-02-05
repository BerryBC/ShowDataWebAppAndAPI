'''
@Descripttion: 数据解释 Views 页面
@Author: BerryBC
@Date: 2020-02-05 12:13:17
@LastEditors  : BerryBC
@LastEditTime : 2020-02-05 13:41:48
'''

from django.shortcuts import render, redirect
from django.http import HttpResponse
import Lib.LUserCtrl as LuserCtrl
from django.template import loader
import json
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse


@LuserCtrl.decoratedPageCheckAdm
def funEmoRecog(request):
    template = loader.get_template('emorecog.html')
    return HttpResponse(template.render({}, request))


@LuserCtrl.decoratedPageCheckAdm
def funInsertSample(request):
    template = loader.get_template('insertsample.html')
    return HttpResponse(template.render({}, request))


@LuserCtrl.decoratedPageCheckAdm
def funReuseLinkMGT(request):
    template = loader.get_template('reuselinkmgt.html')
    return HttpResponse(template.render({}, request))
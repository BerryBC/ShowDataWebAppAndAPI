'''
@Descripttion: 数据解释 Views 页面
@Author: BerryBC
@Date: 2020-02-05 12:13:17
@LastEditors  : BerryBC
@LastEditTime : 2020-02-05 15:30:44
'''

from django.shortcuts import render, redirect
from django.http import HttpResponse
import Lib.LUserCtrl as LuserCtrl
import Lib.LDataCtrl as LDataCtrl
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


@csrf_exempt
@LuserCtrl.decoratedApiCheckAdm
def apiLoadRandSample(request):
    intResult = 0
    dictResult = LDataCtrl.funLoadOneSample()
    if not dictResult['_id'] == '1024':
        intResult = 1
    resp = {'intBack': intResult, 'dictData': dictResult}
    return HttpResponse(content=json.dumps(
        resp), content_type='application/json;charset = utf-8', charset='utf-8')


@csrf_exempt
@LuserCtrl.decoratedApiCheckAdm
def apiConfirmSample(request):
    intEmo = int(request.POST.get('e'))
    strSampleID = request.POST.get('id')
    intResult = LDataCtrl.funConfirmSaple(strSampleID, intEmo)
    resp = {'intBack': intResult}
    return HttpResponse(content=json.dumps(
        resp), content_type='application/json;charset = utf-8', charset='utf-8')

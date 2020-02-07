'''
@Descripttion: 数据解释 Views 页面
@Author: BerryBC
@Date: 2020-02-05 12:13:17
@LastEditors  : BerryBC
@LastEditTime : 2020-02-07 15:00:50
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


@LuserCtrl.decoratedPageCheckAdm
def funDeleteSampleKWPage(request):
    template = loader.get_template('deleteinclkeyword.html')
    return HttpResponse(template.render({}, request))

@LuserCtrl.decoratedPageCheckAdm
def funLoadTableDataCount(request):
    template = loader.get_template('logdatacount.html')
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


@csrf_exempt
@LuserCtrl.decoratedApiCheckAdm
def apiInsertSample(request):
    intEmo = int(request.POST.get('e'))
    strSampleID = request.POST.get('ct')
    intResult = LDataCtrl.funInsertSample(intEmo, strSampleID)
    resp = {'intBack': intResult}
    return HttpResponse(content=json.dumps(
        resp), content_type='application/json;charset = utf-8', charset='utf-8')


@csrf_exempt
@LuserCtrl.decoratedApiCheckAdm
def apiGetReusableSite(request):
    intResult=0
    arrAllSite=LDataCtrl.funListAllReusable()
    intResult=1
    resp = {'intBack': intResult,'arrSite':arrAllSite}
    return HttpResponse(content=json.dumps(
        resp), content_type='application/json;charset = utf-8', charset='utf-8')

@csrf_exempt
@LuserCtrl.decoratedApiCheckAdm
def apiDeleteReusableSite(request):
    intResult=0
    strID=request.POST.get('id')
    intResult=LDataCtrl.funDeleteReusableSite(strID)
    resp = {'intBack': intResult}
    return HttpResponse(content=json.dumps(
        resp), content_type='application/json;charset = utf-8', charset='utf-8')


@csrf_exempt
@LuserCtrl.decoratedApiCheckAdm
def apiInsertReusableSite(request):
    intResult=0
    strURL=request.POST.get('u')
    intResult=LDataCtrl.funInsertReusableSite(strURL)
    resp = {'intBack': intResult}
    return HttpResponse(content=json.dumps(
        resp), content_type='application/json;charset = utf-8', charset='utf-8')




@csrf_exempt
@LuserCtrl.decoratedApiCheckAdm
def apiDeleteSampleWithKeyW(request):
    intResult=0
    strKW=request.POST.get('kw')
    intDeleteCount=LDataCtrl.funDeleteSampleWithKW(strKW)
    intResult=1
    resp = {'intBack': intResult,'intDeleteCount':intDeleteCount}
    return HttpResponse(content=json.dumps(
        resp), content_type='application/json;charset = utf-8', charset='utf-8')



@csrf_exempt
@LuserCtrl.decoratedApiCheckAdm
def apiLoadAllTableCount(request):
    intResult=0
    strDataCount=LDataCtrl.funLoadCountOfNumber()
    intResult=1
    resp = {'intBack': intResult,'strFB':strDataCount}
    return HttpResponse(content=json.dumps(
        resp), content_type='application/json;charset = utf-8', charset='utf-8')
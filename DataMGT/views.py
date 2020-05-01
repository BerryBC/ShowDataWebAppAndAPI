'''
@Descripttion: 数据解释 Views 页面
@Author: BerryBC
@Date: 2020-02-05 12:13:17
@LastEditors: BerryBC
@LastEditTime: 2020-05-01 23:57:34
'''

import Lib.LUserCtrl as LuserCtrl
import Lib.LDataCtrl as LDataCtrl
import Lib.LLearn as LLearn
import Lib.LSpy as LSpy

import json
import time

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse


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

@LuserCtrl.decoratedPageCheckAdm
def funMGTCustom(request):
    template = loader.get_template('custommgt.html')
    return HttpResponse(template.render({}, request))

@LuserCtrl.decoratedPageCheckAcc
def funSpyDataCheck(request):
    template = loader.get_template('spydatacheck.html')
    return HttpResponse(template.render({}, request))

@LuserCtrl.decoratedPageCheckAdm
def funSklearnModelCreat(request):
    template = loader.get_template('sklearnmodelc.html')
    return HttpResponse(template.render({}, request))


@LuserCtrl.decoratedPageCheckAcc
def funClfSampleResult(request):
    template = loader.get_template('loadlearnclfsample.html')
    return HttpResponse(template.render({}, request))


@LuserCtrl.decoratedPageCheckAcc
def funJudEmoByCT(request):
    template = loader.get_template('judctemo.html')
    return HttpResponse(template.render({}, request))



# ----------------- 以上页面 ----------------
# ----------------- 以下API ----------------

@csrf_exempt
@LuserCtrl.decoratedApiCheckAdm
def apiLoadRandSample(request):
    intResult = 0
    dictResult = LDataCtrl.funLoadOneSample(False)
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


        
@csrf_exempt
@LuserCtrl.decoratedApiCheckAdm
def apiGetCustom(request):
    intResult=0
    arrAllData=LDataCtrl.funListAllCustom()
    intResult=1
    resp = {'intBack': intResult,'arrData':arrAllData}
    return HttpResponse(content=json.dumps(
        resp), content_type='application/json;charset = utf-8', charset='utf-8')



@csrf_exempt
@LuserCtrl.decoratedApiCheckAdm
def apiInsertCustom(request):
    intResult=0
    strTag=request.POST.get('t')
    strKeyURL=request.POST.get('u')
    intResult=LDataCtrl.funInsertCustom(strTag,strKeyURL)
    resp = {'intBack': intResult}
    return HttpResponse(content=json.dumps(
        resp), content_type='application/json;charset = utf-8', charset='utf-8')




@csrf_exempt
@LuserCtrl.decoratedApiCheckAdm
def apiDeleteCustom(request):
    intResult=0
    strID=request.POST.get('i')
    intResult=LDataCtrl.funDeleteCustom(strID)
    resp = {'intBack': intResult}
    return HttpResponse(content=json.dumps(
        resp), content_type='application/json;charset = utf-8', charset='utf-8')




@csrf_exempt
@LuserCtrl.decoratedApiCheckAcc
def apiSpyDataWithTag(request):
    intResult=1
    strTag=request.POST.get('t')
    strURL=request.POST.get('u')
    strErr,strResult=LSpy.funSpyDataWithTag(strURL,strTag)
    if not strErr is None:
        intResult=0
        strResult=strErr
    resp = {'intBack': intResult,'strCT':strResult}
    return HttpResponse(content=json.dumps(
        resp), content_type='application/json;charset = utf-8', charset='utf-8')



@csrf_exempt
@LuserCtrl.decoratedApiCheckAcc
def apiLoadClfedSample(request):
    intResult = 0
    dictResult = LDataCtrl.funLoadOneSample(True)
    if not dictResult['_id'] == '1024':
        intResult = 1
    resp = {'intBack': intResult, 'dictData': dictResult}
    return HttpResponse(content=json.dumps(
        resp), content_type='application/json;charset = utf-8', charset='utf-8')



@csrf_exempt
@LuserCtrl.decoratedApiCheckAcc
def apiJudEMO(request):
    intResult = 1
    strCT=request.POST.get('ct')
    intEMO = LLearn.JudContent([strCT],True)
    resp = {'intBack': intResult, 'intEMO': intEMO}
    return HttpResponse(content=json.dumps(
        resp), content_type='application/json;charset = utf-8', charset='utf-8')


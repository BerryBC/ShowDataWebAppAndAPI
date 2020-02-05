'''
@Descripttion: 主程序反馈页面
@Author: BerryBC
@Date: 2020-02-04 21:47:34
@LastEditors  : BerryBC
@LastEditTime : 2020-02-05 10:33:35
'''
from django.shortcuts import render, redirect
from django.http import HttpResponse
import Lib.LUserCtrl as LuserCtrl
from django.template import loader
import json
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse


@LuserCtrl.decoratedPageCheckAcc
def funMain(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render({}, request))
    # strUserN = request.get_signed_cookie('un', default="", salt='BY2')
    # strUserT = request.get_signed_cookie('ut', default="", salt='BY2')
    # if strUserN != "" and strUserT != "":
    #     bolFBCheck = LuserCtrl.funCheckToken(strUserN, strUserT)
    #     if bolFBCheck:
    #         template = loader.get_template('main.html')
    #         return HttpResponse(template.render({}, request))
    # return redirect("/cantacc/")


def funCannotAccess(request):
    template = loader.get_template('cannotacc.html')
    return HttpResponse(template.render({}, request))


def funNotAdm(request):
    template = loader.get_template('notadm.html')
    return HttpResponse(template.render({}, request))

from django.shortcuts import render, redirect
from django.http import HttpResponse
import Lib.LUserCtrl as LuserCtrl
from django.template import loader
import json
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

def funLogin(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))


@LuserCtrl.decoratedPageCheckAdm
def funUserManage(request):
    template = loader.get_template('admindash.html')
    return HttpResponse(template.render({}, request))


'''
@name: apiAddUser
@msg: 添加用户API
@param request: 传入请求
@return: 返回添加用户
         返回 99 为非 Post 请求错误
         返回 98 为非管理员操作
'''


@csrf_exempt
@LuserCtrl.decoratedApiCheckAdm
def apiUserRegistration(request):
    strRegUser = request.POST.get('u')
    strRegPW = request.POST.get('p')
    strRegPower = request.POST.get('pl')
    intResult = LuserCtrl.funUserRegistration(
        strRegUser, strRegPW, int(strRegPower))
    resp = {'intBack': intResult}
    return HttpResponse(content=json.dumps(
        resp), content_type='application/json;charset = utf-8', charset='utf-8')


'''
@name: apiUserLogin
@msg: 用户登录
@param request :传入请求
@return: 返回登录是否成功
         返回 99 为非 Post 请求错误
'''


@csrf_exempt
def apiUserLogin(request):
    if(request.method == 'POST'):
        strRegUser = request.POST.get('u')
        strRegPW = request.POST.get('p')
        dictResult = LuserCtrl.funUserLoginIn(
            strRegUser, strRegPW)
        resp = {'intBack': dictResult['Result']}
        
        req = HttpResponse(content=json.dumps(
            resp), content_type='application/json;charset = utf-8', charset='utf-8')
        req.set_signed_cookie('un', strRegUser, salt='BY2')
        req.set_signed_cookie('ut', dictResult['Token'], salt='BY2')
        return req
    else:
        resp = {'intBack': 99}
        return HttpResponse(content=json.dumps(
            resp), content_type='application/json;charset = utf-8', charset='utf-8')



'''
@name: apiUserList
@msg: 列出用户列表
@param request :传入请求
@return: 返回用户列表
         返回 99 为非 Post 请求错误
         返回 98 为非管理员操作
'''


@csrf_exempt
@LuserCtrl.decoratedApiCheckAdm
def apiUserList(request):
    listResult = LuserCtrl.funUserListAll()
    resp = {'intBack': 2,'listUsr':listResult}
    return HttpResponse(content=json.dumps(
        resp), content_type='application/json;charset = utf-8', charset='utf-8')



'''
@name: apiResetPasswork
@msg: 重设密码的 API
@param request :传入请求
@return: 返回修改密码是否成功
         返回 99 为非 Post 请求错误
         返回 98 为非管理员操作
'''
@csrf_exempt
@LuserCtrl.decoratedApiCheckAdm
def apiResetPasswork(request):
    strRegUser = request.POST.get('u')
    strRegPW = request.POST.get('p')
    intResult = LuserCtrl.funUserResetPasswork(
        strRegUser, strRegPW)
    resp = {'intBack': intResult}
    return HttpResponse(content=json.dumps(
        resp), content_type='application/json;charset = utf-8', charset='utf-8')



'''
@name: apiResetPower
@msg: 重设权限的 API
@param request :传入请求
@return: 返回修改密码是否成功
         返回 99 为非 Post 请求错误
         返回 98 为非管理员操作
'''
@csrf_exempt
@LuserCtrl.decoratedApiCheckAdm
def apiResetPower(request):
    strRegUser = request.POST.get('u')
    strRegPower = request.POST.get('pl')
    intResult = LuserCtrl.funUserResetPwoer(
        strRegUser, strRegPower)
    resp = {'intBack': intResult}
    return HttpResponse(content=json.dumps(
        resp), content_type='application/json;charset = utf-8', charset='utf-8')


'''
@name: apiDeleteUser
@msg: 删除用户
@param request :传入请求
@return: 返回删除用户是否成功
         返回 99 为非 Post 请求错误
         返回 98 为非管理员操作
'''
@csrf_exempt
@LuserCtrl.decoratedApiCheckAdm
def apiDeleteUser(request):
    strRegUser = request.POST.get('u')
    intResult = LuserCtrl.funUserDelete(
        strRegUser)
    resp = {'intBack': intResult}
    return HttpResponse(content=json.dumps(
        resp), content_type='application/json;charset = utf-8', charset='utf-8')
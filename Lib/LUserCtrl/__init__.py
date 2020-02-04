'''
@Descripttion: 用户登陆包
@Author: BerryBC
@Date: 2020-02-04 22:00:55
@LastEditors  : BerryBC
@LastEditTime : 2020-02-05 00:46:54
'''

import hashlib
import datetime
import threading
import json
from configobj import ConfigObj
from functools import wraps
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import timedelta

from Lib.LMongoDB import claMongoDB


# 这里是已经没办法了，不想重写只能这样了
strCfgPath = './cfg/dbCfg.ini'

objConfig = ConfigObj(strCfgPath)
objLinkDB = claMongoDB(strCfgPath, 'mongodb')
intInvOfHeartBeat = int(objConfig['invForCheckOL']['inv'])*60


'''
@name: funGetIn
@msg: 把用户放到 OL 用户群中
@param strUser : 用户名
@return: 如果已经存在，返回存在的 Token
         如果没有存在，放进 OL 用户群中，并且给出新的 Token
'''


def funGetIn(strUser):

    # 使用 MySQL
    # conn = mysql.connector.connect(
    #     host=strDBHost, user=strDBUser, password=strDBPW, port=strPort, database=strDBName)
    # cursor = conn.cursor()
    # cursor.execute(
    #     'select UserN,UserT from tb_oluser where UserN = %s ', [strUser, ])
    # listAllData = cursor.fetchall()
    # strNow = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    # strToken = hashlib.md5(strNow.encode('utf-8')).hexdigest()[3:17]
    # intResCount = cursor.rowcount
    # if intResCount > 0:
    #     strToken = listAllData[0][1]
    #     cursor.execute(
    #         'UPDATE tb_oluser set LastTime=now() where UserN=%s', [strUser, ])
    # else:
    #     cursor.execute('insert into tb_oluser (LastTime, UserN,UserT) values (now(),%s, %s)', [
    #                    strUser, strToken])
    # conn.commit()
    # cursor.close()
    # conn.close()

    # 使用 MongoDB
    strNow = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    strToken = hashlib.md5(strNow.encode('utf-8')).hexdigest()[3:17]
    dictNewOL = {'un': strUser, 'ut': strToken, 'lt': strNow}
    objLoadOL=objLinkDB.LoadOne('userdb-OL', {'un': strUser})
    if objLoadOL is None:
        objLinkDB.InsertOne('userdb-OL', dictNewPage)
    else:
        strToken=objLoadOL['ut']
        objLinkDB.UpdateOneData('userdb-OL', {'un': strUser}, {'lt': strNow}})
    return strToken


def funGetOut(strUser):
    
    # 使用 MySQL
    # conn = mysql.connector.connect(
    #     host = strDBHost, user = strDBUser, password = strDBPW, port = strPort, database = strDBName)
    # cursor=conn.cursor()
    # cursor.execute('delete from tb_oluser where UserN=%s', [strUser, ])
    # conn.commit()
    # cursor.close()
    
    # 使用 MongoDB
    objLinkDB.DeleteSome('userdb-OL', {'un': strUser})



'''
@name: funCheckToken
@msg: 检查用户是否在线用户，否则需重新登录
@param strUser: 用户名
       strToken: 用户手令
@return: bolIorNot 布尔值检查是否在线用户
'''


def funCheckToken(strUser, strToken):

    # 使用 MySQL
    # bolIorNot=False
    # conn=mysql.connector.connect(
    #     host = strDBHost, user = strDBUser, password = strDBPW, port = strPort, database = strDBName)
    # cursor=conn.cursor()
    # cursor.execute(
    #     'select LastTime,UserN,UserT from tb_oluser where UserN = %s ', [strUser, ])
    # listFirstData=cursor.fetchone()
    # intResCount=cursor.rowcount
    # if intResCount > 0:
    #     if listFirstData[2] == strToken:
    #         bolIorNot=True
    # conn.commit()
    # cursor.close()
    # conn.close()


    # 使用 MongoDB
    bolIorNot=objLinkDB.CheckOneExisit('userdb-OL',{'un': strUser,'ut':strToken})
    return bolIorNot


def funHeartBeat():
    # 使用 MySQL
    # conn=mysql.connector.connect(
    #     host = strDBHost, user = strDBUser, password = strDBPW, port = strPort, database = strDBName)
    # cursor=conn.cursor()
    # cursor.execute(
    #     'delete from tb_oluser where LastTime<DATE_SUB(now(),INTERVAL 20 minute)')
    # conn.commit()
    # cursor.close()
    # conn.close()
    

    # 使用 MongoDB
    dtimeNow = datetime.datetime.now()
    dtimeBefore=timedelta(minutes=25)
    dtimeBefore=(dtimeNow-dtimeBefore).strftime("%Y/%m/%d %H:%M:%S")
    objLinkDB.DeleteSome('userdb-OL', {'lt': {'$lt':dtimeBefore}})
    threading.Timer(intInvOfHeartBeat, funHeartBeat).start()


'''
@name: funUserRegistration
@msg:
@param strUser : 用户名
@param strPW : 密码
@param strPower: 0 为普通用户， 9 为管理员
@return: 0 没有执行完毕
         1 已经有一个相同用户
         2 执行完成
'''


def funUserRegistration(strUser, strPW, strPower):
    intResult=0

    # 使用 MySQL
    # conn=mysql.connector.connect(
    #     host = strDBHost, user = strDBUser, password = strDBPW, port = strPort, database = strDBName)
    # cursor=conn.cursor()

    # cursor.execute('select * from tb_alluser where UserN = %s ', [strUser, ])
    # listFirstData=cursor.fetchone()
    # intResCount=cursor.rowcount
    # if intResCount > 0:
    #     conn.commit()
    #     cursor.close()
    #     conn.close()
    #     intResult=1
    # else:
    #     cursor.execute(
    #         'INSERT INTO tb_alluser ( UserN,UserPW,UserPower ) VALUES ( %s , %s ,%s  );', [strUser, strPW, strPower])
    #     conn.commit()
    #     cursor.close()
    #     conn.close()
    #     intResult=2

    # 使用 MongoDB
    objLoadUser=objLinkDB.LoadOne('userdb-AL', {'un': strUser})
    dictNewUser = { 'un':strUser,'upw':strPW,'up':strPower}
    if objLoadUser is None:
        objLinkDB.InsertOne('userdb-AL', dictNewUser)
        intResult=2
    else:
        intResult=1

    return intResult


'''
@name: funUserLoginIn
@msg: 检查是否登录成功
@param strUser : 用户名
@param strPW : 密码
@return: 0 没有执行
         1 登录成功
'''


def funUserLoginIn(strUser, strPW):
    intResult=0
    dictFB={'Result': 0, 'Token': ''}

    # 使用 MySQL
    # conn=mysql.connector.connect(
    #     host = strDBHost, user = strDBUser, password = strDBPW, port = strPort, database = strDBName)
    # cursor=conn.cursor()
    # cursor.execute(
    #     'select * from tb_alluser where UserN = %s and UserPW=%s ', [strUser, strPW, ])
    # listFirstData=cursor.fetchone()
    # intResCount=cursor.rowcount
    # if intResCount > 0:
    #     conn.commit()
    #     cursor.close()
    #     conn.close()
    #     intResult=1
    #     strToken=funGetIn(strUser)
    #     dictFB['Result']=intResult
    #     dictFB['Token']=strToken
    # else:
    #     cursor.close()
    #     conn.close()
    #     intResult=0
    #     dictFB['Result']=intResult


    # 使用 MongoDB
    objLoadUser=objLinkDB.LoadOne('userdb-AL', {'un': strUser,'upw':strPW})
    if objLoadUser is None:
        intResult=0
        dictFB['Result']=intResult
    else:
        intResult=1
        strToken=funGetIn(strUser)
        dictFB['Result']=intResult
        dictFB['Token']=strToken
    return dictFB


'''
@name: funUserListAll
@msg: 返回所有用户信息
@return: 返回一个 list 对象，里面每个用户是一个字典对象
         字典对象中 un 代表用户名
         字典对象中 pw 代表权限
'''


def funUserListAll():
    listArrUser=[]

    
    # 使用 MySQL
    # conn=mysql.connector.connect(
    #     host = strDBHost, user = strDBUser, password = strDBPW, port = strPort, database = strDBName)
    # cursor=conn.cursor()
    # cursor.execute(
    #     'select UserN , UserPower from tb_alluser ')
    # listAllData=cursor.fetchall()
    # for drUser in listAllData:
    #     listArrUser.append({'un': drUser[0], 'pw': drUser[1]})

    # 使用 MongoDB
    objLoadAll=objLinkDB.LoadAllData('userdb-AL')
    for drUser in objLoadAll:
        listArrUser.append({'un': drUser['un'], 'pw': drUser['up']})
    return listArrUser


'''
@name: funUserResetPasswork
@msg: 修改用户密码
@param strUser : 用户名
@param strPW : 密码
@return: 0 没有执行
         1 登录成功
         2 没有该用户
'''


def funUserResetPasswork(strUser, strPW):
    intResult=0

    # 使用 MySQL
    # conn=mysql.connector.connect(
    #     host = strDBHost, user = strDBUser, password = strDBPW, port = strPort, database = strDBName)
    # cursor=conn.cursor()

    # cursor.execute('select * from tb_alluser where UserN = %s ', [strUser, ])
    # listFirstData=cursor.fetchone()
    # intResCount=cursor.rowcount
    # if intResCount > 0:
    #     cursor.execute(
    #         'UPDATE tb_alluser set UserPW=%s where UserN=%s', [strPW, strUser, ])
    #     conn.commit()
    #     cursor.close()
    #     conn.close()
    #     intResult=1
    # else:
    #     cursor.close()
    #     conn.close()
    #     intResult=2

    # 使用 MongoDB
    objLoadUser=objLinkDB.LoadOne('userdb-AL', {'un': strUser})
    if objLoadUser is None:
        intResult=2
    else:
        objLinkDB.UpdateOneData('userdb-AL', {'un': strUser}, {'upw': strPW}})
        intResult=1

    return intResult


'''
@name: funUserResetPwoer
@msg: 修改用户权限
@param strUser : 用户名
@param strPower: 0 为普通用户， 9 为管理员
@return: 0 没有执行
         1 登录成功
         2 没有该用户
'''


def funUserResetPwoer(strUser, strPower):
    intResult=0

    # 使用 MySQL
    # conn=mysql.connector.connect(
    #     host = strDBHost, user = strDBUser, password = strDBPW, port = strPort, database = strDBName)
    # cursor=conn.cursor()
    # cursor.execute(
    #     'select UserN,UserPower from tb_alluser where UserN = %s ', [strUser, ])
    # listFirstData=cursor.fetchone()
    # intResCount=cursor.rowcount
    # if intResCount > 0:
    #     bolCanDel=True
    #     if listFirstData[1] == 9:
    #         cursor.execute(
    #             'select UserN,UserPower from tb_alluser where UserPower=9 ')
    #         listAdmUser=cursor.fetchall()
    #         intResAdmCount=cursor.rowcount
    #         if intResAdmCount == 1:
    #             intResult=3
    #             bolCanDel=False

    #     if bolCanDel:
    #         cursor.execute(
    #             'UPDATE tb_alluser set UserPower=%s where UserN=%s', [strPower, strUser, ])
    #         intResult=1
    #     conn.commit()
    #     cursor.close()
    #     conn.close()
    # else:
    #     cursor.close()
    #     conn.close()
    #     intResult=2


    # 使用 MongoDB
    objLoadUser=objLinkDB.LoadOne('userdb-AL', {'un': strUser})
    if objLoadUser is None:
        intResult=2
    else:        
        bolCanDel=True
        if objLoadUser['up']==9:
            intCountAdm=0
            arrSU=objLinkDB.LoadSome()('userdb-AL', {'up': 9})
            for eleProxy in arrSU:
                intCountAdm+=1
            if intCountAdm == 1:
                intResult=3
                bolCanDel=False
        if bolCanDel:
            objLinkDB.UpdateOneData('userdb-AL', {'un': strUser}, {'up': strPower})
            intResult=1

    return intResult


'''
@name: funUserDelete
@msg: 删除用户
@param strUser : 用户名
@param strPower: 0 为普通用户， 9 为管理员
@return: 0 没有执行
         1 删除成功
         2 没有该用户
         3 仅存一个管理员账号
'''


def funUserDelete(strUser):
    intResult=0

    # 使用 MySQL
    # conn=mysql.connector.connect(
    #     host = strDBHost, user = strDBUser, password = strDBPW, port = strPort, database = strDBName)
    # cursor=conn.cursor()
    # cursor.execute(
    #     'select UserN,UserPower from tb_alluser where UserN = %s ', [strUser, ])
    # listFirstData=cursor.fetchone()
    # intResCount=cursor.rowcount
    # if intResCount > 0:
    #     bolCanDel=True
    #     if listFirstData[1] == 9:
    #         cursor.execute(
    #             'select UserN,UserPower from tb_alluser where UserPower=1 ')
    #         listAdmUser=cursor.fetchall()
    #         intResAdmCount=cursor.rowcount
    #         if intResAdmCount == 1:
    #             intResult=3
    #             bolCanDel=False

    #     if bolCanDel:
    #         cursor.execute(
    #             'DELETE FROM tb_alluser WHERE UserN=%s', [strUser, ])
    #         cursor.execute(
    #             'DELETE FROM tb_oluser WHERE UserN=%s', [strUser, ])
    #         intResult=1
    #     conn.commit()
    #     cursor.close()
    #     conn.close()
    # else:
    #     cursor.close()
    #     conn.close()
    #     intResult=2


    # 使用 MongoDB
    objLoadUser=objLinkDB.LoadOne('userdb-AL', {'un': strUser})
    if objLoadUser is None:
        intResult=2
    else:        
        bolCanDel=True
        if objLoadUser['up']==9:
            intCountAdm=0
            arrSU=objLinkDB.LoadSome('userdb-AL', {'up': 9})
            for eleProxy in arrSU:
                intCountAdm+=1
            if intCountAdm == 1:
                intResult=3
                bolCanDel=False
        if bolCanDel:
            objLinkDB.DeleteSome('userdb-AL', {'un': strUser})
            intResult=1

    return intResult


'''
@name: funCheckAdmin
@msg: 检查用户是否管理员
@param strUser: 用户名
@return: bolIorNot 布尔值检查是否管理员
'''


def funCheckAdmin(strUser):
    # 使用 MySQL
    # bolIorNot=False
    # conn=mysql.connector.connect(
    #     host = strDBHost, user = strDBUser, password = strDBPW, port = strPort, database = strDBName)
    # cursor=conn.cursor()
    # cursor.execute(
    #     'select UserN,UserPower from tb_alluser where UserPower=9 and UserN = %s ', [strUser, ])
    # listFirstData=cursor.fetchone()
    # intResCount=cursor.rowcount
    # if intResCount > 0:
    #     bolIorNot=True
    # conn.commit()
    # cursor.close()
    # conn.close()

    # 使用 MongoDB
    bolIorNot=objLinkDB.CheckOneExisit('userdb-AL',{'un': strUser,'up':9})

    return bolIorNot


'''
@name: decoratedCheckAdm
@msg: 检查是否管理员的装饰器
@param f 传入函数
'''


def decoratedPageCheckAdm(f):
    @wraps(f)
    def decorated(request, *args, **kwargs):
        strUserN=request.get_signed_cookie(
            'un', default = "nouser", salt = 'BY2')
        strUserT=request.get_signed_cookie(
            'ut', default = "nouser", salt = 'BY2')
        bolFBCheck=funCheckToken(strUserN, strUserT)
        bolAdmCheck=funCheckAdmin(strUserN)
        if bolFBCheck and bolAdmCheck:
            funGetIn(strUserN)
            return f(request, *args, **kwargs)
        else:
            return redirect("/notadm/")
    return decorated


'''
@name: decoratedPageCheckAcc
@msg: 检查是否已登陆的装饰器
@param f 传入函数
'''


def decoratedPageCheckAcc(f):
    @wraps(f)
    def decorated(request, *args, **kwargs):
        strUserN=request.get_signed_cookie('un', default = "", salt = 'BY2')
        strUserT=request.get_signed_cookie('ut', default = "", salt = 'BY2')
        if strUserN != "" and strUserT != "":
            funGetIn(strUserN)
            bolFBCheck=funCheckToken(strUserN, strUserT)
            if bolFBCheck:
                return f(request, *args, **kwargs)
        return redirect("/cantacc/")
    return decorated


'''
@name: decoratedApiCheckAcc
@msg: 当通过 API 请求时，请求是否已登录
@param f 传入函数
@return: 字典对象，其中
         {'intBack': 98} 未登录
         {'intBack': 99} 非 Post 请求
'''


def decoratedApiCheckAcc(f):
    @wraps(f)
    def decorated(request, *args, **kwargs):
        strUserN=request.get_signed_cookie(
            'un', default = "nouser", salt = 'BY2')
        strUserT=request.get_signed_cookie(
            'ut', default = "nouser", salt = 'BY2')
        bolFBCheck=funCheckToken(strUserN, strUserT)
        if bolFBCheck:
            if(request.method == 'POST'):
                funGetIn(strUserN)
                return f(request, *args, **kwargs)
            else:
                resp={'intBack': 99}
                return HttpResponse(content = json.dumps(resp), content_type = 'application/json;charset = utf-8', charset = 'utf-8')
        else:
            resp={'intBack': 98}
            return HttpResponse(content = json.dumps(
                resp), content_type = 'application/json;charset = utf-8', charset = 'utf-8')
    return decorated


'''
@name: decoratedApiCheckAdm
@msg: 当通过 API 请求时，请求是否用管理员账号登录
@param f 传入函数
@return: 字典对象，其中
         {'intBack': 98} 未登录
         {'intBack': 99} 非 Post 请求
'''


def decoratedApiCheckAdm(f):
    @wraps(f)
    def decorated(request, *args, **kwargs):
        strUserN=request.get_signed_cookie(
            'un', default = "nouser", salt = 'BY2')
        strUserT=request.get_signed_cookie(
            'ut', default = "nouser", salt = 'BY2')
        bolFBCheck=funCheckToken(strUserN, strUserT)
        bolAdmCheck=funCheckAdmin(strUserN)
        if bolFBCheck and bolAdmCheck:
            if(request.method == 'POST'):
                funGetIn(strUserN)
                return f(request, *args, **kwargs)
            else:
                resp={'intBack': 99}
                return HttpResponse(content = json.dumps(resp), content_type = 'application/json;charset = utf-8', charset = 'utf-8')
        else:
            resp={'intBack': 98}
            return HttpResponse(content = json.dumps(
                resp), content_type = 'application/json;charset = utf-8', charset = 'utf-8')
    return decorated

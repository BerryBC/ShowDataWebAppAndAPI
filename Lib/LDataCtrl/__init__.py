'''
@Descripttion: 数据管理库
@Author: BerryBC
@Date: 2020-02-05 13:52:49
@LastEditors: BerryBC
@LastEditTime: 2020-05-31 12:50:31
'''

import hashlib
import datetime
import time
import threading
import json
from configobj import ConfigObj
from functools import wraps
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import timedelta
from dateutil import parser
from bson.objectid import ObjectId

from Lib.LMongoDB import claMongoDB


strCfgPath = './cfg/dbCfg.ini'

objConfig = ConfigObj(strCfgPath)
objLinkDB = claMongoDB(strCfgPath, 'mongodb')


def funLoadOneSample(bolIsJed):
    dictReturn = {}
    arrDataEle = []
    eleOneSample = objLinkDB.LoadRandomLimit(
        'sampledb', {'cf': False, 'jed': bolIsJed}, 1)
    for eleData in eleOneSample:
        arrDataEle.append(eleData)
    if len(arrDataEle) == 0:
        dictReturn = {'_id': '1024', 'ct': '',
                      'e': 0, 'cf': False, 'jed': False, 't': 0}
    else:
        dictReturn = arrDataEle[0]
        dictReturn = {'_id': str(dictReturn.get('_id')),
                      'ct': dictReturn.get('ct'),
                      'e': str(dictReturn.get('e'))}
    return dictReturn


def funConfirmSaple(strID, intEmo):
    intResult = 0
    if not strID == '1024':
        objLinkDB.UpdateOneData('sampledb', {'_id': ObjectId(strID)}, {
                                'cf': True, 'jed': True, 'e': intEmo})
        intResult = 1
    return intResult


def funInsertSample(intEmo, strCT):
    intResult = 0
    dictNew = {'ct': strCT, 'e': intEmo, 'cf': True,
               'jed': True, 't':  int(time.time()*1000)}
    objLinkDB.InsertOne('sampledb', dictNew)
    intResult = 1
    return intResult


def funListAllReusable():
    arrReturn = []
    objAllSite = objLinkDB.LoadAllData('pagedb-Reuseable')
    for eleSite in objAllSite:
        arrReturn.append(
            {'_id': str(eleSite.get('_id')), 'url': eleSite['url']})
    return arrReturn


def funInsertReusableSite(strURL):
    intResult = 0
    if objLinkDB.CheckOneExisit('pagedb-Reuseable', {'url': strURL}):
        intResult = 1
    else:
        objLinkDB.InsertOne('pagedb-Reuseable', {'url': strURL})
        intResult = 2
    return intResult


def funDeleteReusableSite(strID):
    intResult = 0
    objLinkDB.DeleteSome('pagedb-Reuseable', {'_id': ObjectId(strID)})
    intResult = 1
    return intResult


def funDeleteSampleWithKW(strKeyW):
    objDeleted = objLinkDB.DeleteSome(
        'sampledb', {'ct': {'$regex': strKeyW, '$options': "i"}, 'cf': False})
    # print(objDeleted.deleted_count)
    return objDeleted.deleted_count


def funLoadCountOfNumber():
    strReturn = ''
    arrDatabaseTable = []
    arrDatabaseTable.append({'tbName': 'proxydb', 'Desp': '代理'})
    arrDatabaseTable.append({'tbName': 'pagedb-Crawled', 'Desp': '已爬链接'})
    arrDatabaseTable.append({'tbName': 'pagedb-Reuseable', 'Desp': '可重用链接'})
    arrDatabaseTable.append({'tbName': 'sampledb', 'Desp': '样本'})
    arrDatabaseTable.append({'tbName': 'userdb-OL', 'Desp': '在线用户'})
    arrDatabaseTable.append({'tbName': 'userdb-AL', 'Desp': '全体用户'})
    arrDatabaseTable.append({'tbName': 'clfdb-kw', 'Desp': '关键词样本数*天数'})

    for eleTable in arrDatabaseTable:
        strReturn += eleTable['Desp']+' 数据条数为:  ' + \
            str(objLinkDB.LoadAllData(eleTable['tbName']).count()) + '\n'
    # print(objDeleted.deleted_count)

    strReturn += '  已经判断及情绪为 正面 的数据条数为:  ' + \
        str(objLinkDB.LoadSome('sampledb', {'e': 1, 'cf': True}).count())+'\n'
    strReturn += '  已经判断及情绪为 无价值 的数据条数为:  ' + \
        str(objLinkDB.LoadSome('sampledb', {'e': 0, 'cf': True}).count())+'\n'
    strReturn += '  已经判断及情绪为 负面 的数据条数为:  ' + \
        str(objLinkDB.LoadSome('sampledb', {'e': -1, 'cf': True}).count())+'\n'

    strReturn += '  --机器判定的样本数为:  ' + \
        str(objLinkDB.LoadSome('sampledb', {
            'cf': False, 'jed': True}).count())+'\n'

    strReturn += '  --机器判断及情绪为 正面 的数据条数为:  ' + \
        str(objLinkDB.LoadSome('sampledb', {
            'e': 1, 'cf': False, 'jed': True}).count())+'\n'
    strReturn += '  --机器判断及情绪为 无价值 的数据条数为:  ' + \
        str(objLinkDB.LoadSome('sampledb', {
            'e': 0, 'cf': False, 'jed': True}).count())+'\n'
    strReturn += '  --机器判断及情绪为 负面 的数据条数为:  ' + \
        str(objLinkDB.LoadSome('sampledb', {
            'e': -1, 'cf': False, 'jed': True}).count())+'\n'

    return strReturn


def funListAllCustom():
    arrReturn = []
    objAllSite = objLinkDB.LoadAllData('pagedb-Custom')
    for eleSite in objAllSite:
        arrReturn.append(
            {'_id': str(eleSite.get('_id')), 'tag': eleSite['tag'], 'rURL': eleSite['rURL']})
    return arrReturn


def funInsertCustom(strInTag, strInRURL):
    intResult = 0
    if objLinkDB.CheckOneExisit('pagedb-Custom', {'rURL': strInRURL}):
        intResult = 1
    else:
        objLinkDB.InsertOne(
            'pagedb-Custom', {'tag': strInTag, 'rURL': strInRURL})
        intResult = 2
    return intResult


def funDeleteCustom(strInID):
    intResult = 0
    objLinkDB.DeleteSome('pagedb-Custom', {'_id': ObjectId(strInID)})
    intResult = 1
    return intResult


def funLoadKW(strKW):
    # arrReturn = []
    # if strKW != "":
    #     dictExactMatch=objLinkDB.LoadOne('clfdb-kw', {'kw':  strKW})
    #     arrReturn.append(dictExactMatch)
    #     curTarget = objLinkDB.LoadRandomLimit(
    #         'clfdb-kw', {'kw': {'$regex': strKW, '$options': "i"}}, 20)
    #     for eleCur in curTarget:
    #         if eleCur["kw"]!=dictExactMatch["kw"]:
    #             arrReturn.append(eleCur)
    # return arrReturn
    arrReturn = []
    if strKW != "":
        bolNull = True
        dictExactMatch = objLinkDB.LoadOne('clfdb-kw', {'kw':  strKW})
        if dictExactMatch is not None:
            arrReturn.append(dictExactMatch)
            bolNull = False
        curTarget = objLinkDB.LoadRandomLimit(
            'clfdb-kw', {'kw': {'$regex': strKW, '$options': "i"}}, 20)
        for eleCur in curTarget:
            dictNow={}
            if not bolNull and eleCur['kw'] == dictExactMatch['kw']:
                pass
            else:
                dictNow['kw']=eleCur['kw']
                dictNow['num']=eleCur['num']
                arrReturn.append(dictNow)
    return arrReturn

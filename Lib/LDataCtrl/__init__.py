'''
@Descripttion: 数据管理库
@Author: BerryBC
@Date: 2020-02-05 13:52:49
@LastEditors  : BerryBC
@LastEditTime : 2020-02-05 20:27:33
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


def funLoadOneSample():
    dictReturn = {}
    arrDataEle = []
    eleOneSample = objLinkDB.LoadRandomLimit('sampledb', {'cf': False}, 1)
    for eleData in eleOneSample:
        arrDataEle.append(eleData)
    if len(arrDataEle) == 0:
        dictReturn = {'_id': '1024', 'ct': '',
                      'e': 0, 'cf': False, 'jed': False, 't': 0}
    else:
        dictReturn = arrDataEle[0]
        dictReturn = {'_id': str(dictReturn.get('_id')),
                      'ct': dictReturn.get('ct')}
    return dictReturn


def funConfirmSaple(strID, intEmo):
    intResult = 0
    if not strID == '1024':
        objLinkDB.UpdateOneData('sampledb', {'_id': ObjectId(strID)}, {
                                'cf': True, 'jed': True, 'e': intEmo})
        intResult = 1
    return intResult


def funInsertSample(intEmo, strCT):
    intResult=0
    dictNew = {'ct': strCT, 'e': intEmo, 'cf': True, 'jed': True, 't':  int(time.time()*1000)}
    objLinkDB.InsertOne('sampledb',dictNew)
    intResult=1
    return intResult

def funListAllReusable():
    arrReturn=[]
    objAllSite=objLinkDB.LoadAllData('pagedb-Reuseable')
    for eleSite in objAllSite:
        arrReturn.append({'_id':str(eleSite.get('_id')),'url':eleSite['url']})
    return arrReturn

def funInsertReusableSite(strURL):
    intResult=0
    if objLinkDB.CheckOneExisit('pagedb-Reuseable',{'url':strURL}):
        intResult=1
    else:
        objLinkDB.InsertOne('pagedb-Reuseable',{'url':strURL})
        intResult=2
    return intResult

def funDeleteReusableSite(strID):
    intResult=0
    objLinkDB.DeleteSome('pagedb-Reuseable',{'_id': ObjectId(strID)})
    intResult=1
    return intResult
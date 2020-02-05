'''
@Descripttion: 
@Author: BerryBC
@Date: 2020-02-05 13:52:49
@LastEditors  : BerryBC
@LastEditTime : 2020-02-05 15:27:06
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
from dateutil import parser
from bson.objectid import ObjectId

from Lib.LMongoDB import claMongoDB


strCfgPath = './cfg/dbCfg.ini'

objConfig = ConfigObj(strCfgPath)
objLinkDB = claMongoDB(strCfgPath, 'mongodb')


def funLoadOneSample():
    returnDict = {}
    arrDataEle=[]
    eleOneSample = objLinkDB.LoadRandomLimit('sampledb', {'cf': False}, 1)
    for eleData in eleOneSample:
        arrDataEle.append(eleData)
    if len(arrDataEle)==0:
        returnDict = {'_id': '1024', 'ct': '',
                      'e': 0, 'cf': False, 'jed': False, 't': 0}
    else:
        returnDict=arrDataEle[0]
        returnDict = {'_id': str(returnDict.get('_id')), 'ct': returnDict.get('ct')}
    return returnDict

def funConfirmSaple(strID,intEmo):
    intResult=0
    if not strID =='1024':
        objLinkDB.UpdateOneData('sampledb',{'_id':ObjectId(strID)},{'cf':True,'jed':True,'e':intEmo})
        intResult=1
    return intResult
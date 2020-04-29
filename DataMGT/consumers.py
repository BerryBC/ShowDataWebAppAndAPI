'''
@Descripttion: 
@Author: BerryBC
@Date: 2020-02-24 23:40:18
@LastEditors: BerryBC
@LastEditTime: 2020-04-29 22:28:49
'''

import json

import Lib.LLearn as LLearn

from channels.generic.websocket import WebsocketConsumer


class wsCreatSklearnModel(WebsocketConsumer):

    def funFB2C(self,strMsg, intCode):
        self.send(text_data=json.dumps({
            'msg': strMsg, 'code': intCode
        }))

    def connect(self):
        self.accept()
        self.funFB2C('OK', 1)
        print(' Client Start Sklearn Learn Websocket.')

    def disconnect(self, close_code):
        print(' Learn Websocket disconnected')

    def receive(self, text_data):
        objRevData = json.loads(text_data)
        intCode = objRevData['doCode']
        if intCode == 0:
            LLearn.funGoLearn(self.funFB2C)
        self.funFB2C('Done', 3)
        
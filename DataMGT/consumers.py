'''
@Descripttion: 
@Author: BerryBC
@Date: 2020-02-24 23:40:18
@LastEditors: BerryBC
@LastEditTime: 2020-03-24 23:04:06
'''
# from channels.generic.websocket import WebsocketConsumer
# import json

# class wsCreatSklearnModel(WebsocketConsumer):
#     def connect(self):
#         self.accept()
#         print(' Websocket connected')
#         self.intI=0
#         self.intI+=1
#         self.send(text_data=json.dumps({
#             'message': self.intI
#         }))
#         self.intI+=1
#         self.send(text_data=json.dumps({
#             'message': self.intI
#         }))
#         self.intI+=1
#         self.send(text_data=json.dumps({
#             'message': self.intI
#         }))

#     def disconnect(self, close_code):
#         print(' Websocket disconnected')

#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#         if 'shit' in text_data_json:
#             print(text_data_json['shit'])
#         else:
#             print('  no shit')
#         print(message)
#         self.intI+=1

#         self.send(text_data=json.dumps({
#             'message': self.intI
#         }))
#         if self.intI==10:
#             self.close()
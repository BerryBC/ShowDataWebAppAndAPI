'''
@Descripttion: 
@Author: BerryBC
@Date: 2020-02-24 23:00:48
@LastEditors: BerryBC
@LastEditTime: 2020-02-24 23:01:25
'''
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import DataMGT.routing

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            DataMGT.routing.websocket_urlpatterns
        )
    ),
})
'''
Created on 2016-09-09

@author: Administrator
'''

import logging; logging.basicConfig(level=logging.INFO)
from aiohttp import web
import asyncio

def index(request):
    return web.Response(body=b'welcome to sample!')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop = loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
    
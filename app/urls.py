import tornado.web
from tornado.web import url
from app.handlers.views import  InitDbHandler, PostHandler, GetHandler



def make_app():
    # handlers 参数中定义路由匹配地址
    return tornado.web.Application(handlers=[
        url(r'/init_db/', InitDbHandler),
        url(r'/post_request/', PostHandler),
        url(r'/get_request/', GetHandler)
    ],
    debug = 'True'
    )
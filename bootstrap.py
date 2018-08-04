# coding=utf-8

from bootstrap_init import app

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

if __name__ == '__main__':
    # 前端控制器初始化
    from controller import leetcode_controller
    from controller.views import apidoc
    from controller.views import leetcode

    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(app.config['HTTP_PORT'])
    IOLoop.instance().start()

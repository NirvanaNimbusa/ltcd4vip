# coding=utf-8

from bootstrap_init import app

if __name__ == '__main__':
    # 前端控制器初始化
    from controller import leetcode_controller
    from controller.views import apidoc
    from controller.views import leetcode
    app.run(host=app.config['HTTP_HOST'], port=app.config['HTTP_PORT'])

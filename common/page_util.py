# coding=utf-8
'分页插件'
__author__ = 'Jiateng Liang'


class PageUtil(object):

    def __init__(self, page, page_size, max_cnt, data=None):
        self.page = page
        self.page_size = page_size
        self.max_cnt = max_cnt
        self.data = data
        self.max_page = self.get_max_page()

    def get_max_page(self):
        if self.max_cnt % self.page_size > 0:
            return (self.max_cnt / self.page_size) + 1
        elif self.max_cnt / self.page_size < 1:
            return 1
        else:
            return self.max_cnt / self.page_size

    def get_start(self):
        return (self.page - 1) * self.page_size

    def get_end(self):
        return self.page * self.page_size

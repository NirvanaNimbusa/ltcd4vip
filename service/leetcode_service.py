# coding=utf-8
'题目服务'
from common.exception import ServiceException, ErrorCode
from model.leetcode_problems import LeetcodeProblem

__author__ = 'Jiateng Liang'


class LeetCodeService(object):
    @staticmethod
    def get_leetcode_problem_by_lid(lid):
        problem = LeetcodeProblem.query.filter(LeetcodeProblem.lid == lid).first()
        if not problem:
            raise ServiceException(ErrorCode.NOT_FOUND, u'题目%s不存在' % lid)
        return problem

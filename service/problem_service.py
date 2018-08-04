# coding=utf-8
'题目服务'
from sqlalchemy import func

from bootstrap_init import db
from common.exception import ServiceException, ErrorCode
from common.model_util import models2dict
from common.page_util import PageUtil
from model.leetcode_problems import LeetcodeProblem
from model.leetcode_tag import LeetcodeTagInfo

__author__ = 'Jiateng Liang'


class ProblemService(object):
    @staticmethod
    def count_problems_by(difficulty=100, is_locked=100, type=100):
        """
        查询数量
        :param difficulty:
        :param is_locked:
        :param type:
        :return:
        """
        # 过滤
        filter_list = []
        if difficulty in LeetcodeProblem.Difficulty.ALL.value:
            filter_list.append(LeetcodeProblem.difficulty == difficulty)
        if is_locked in LeetcodeProblem.IsLocked.ALL.value:
            filter_list.append(LeetcodeProblem.is_locked == is_locked)
        if type in LeetcodeProblem.Type.ALL.value:
            filter_list.append(LeetcodeProblem.type == type)

        return db.session.query(func.count(LeetcodeProblem.qid)).filter(*filter_list).scalar()

    @staticmethod
    def get_problem_by_lid(lid):
        """
        获取题目信息
        :param lid: 题号
        :return:
        """

        problem = LeetcodeProblem.query.filter(LeetcodeProblem.lid == lid).first()
        if not problem:
            raise ServiceException(ErrorCode.NOT_FOUND, u'题号=%s不存在' % lid)
        return problem

    @staticmethod
    def get_problem_by_qid(qid):
        """
        获取题目信息
        :param qid: leetcode题目id
        :return:
        """
        problem = LeetcodeProblem.query.filter(LeetcodeProblem.qid == qid).first()
        if not problem:
            raise ServiceException(ErrorCode.NOT_FOUND, u'题目qid=%s不存在' % qid)
        return problem

    @staticmethod
    def get_problem_by_title_slug(title_slug):
        """
        获取题目信息
        :param title_slug:
        :return:
        """
        problem = LeetcodeProblem.query.filter(LeetcodeProblem.title_slug == title_slug).first()
        if not problem:
            raise ServiceException(ErrorCode.NOT_FOUND, u'题目title_slug=%s不存在' % title_slug)
        return problem

    @staticmethod
    def list_problems_order_by_lid_asc(page, page_size, difficulty=100, is_locked=100, type=100):
        """
        根据题号升序
        :param difficulty:
        :param is_locked:
        :param type:
        :return:
        """
        if page <= 0 or page_size <= 0:
            raise ServiceException(ErrorCode.PARAM_ERROR, u'page或者page_size参数错误')
        # 过滤
        filter_list = []
        if difficulty in LeetcodeProblem.Difficulty.ALL.value:
            filter_list.append(LeetcodeProblem.difficulty == difficulty)
        if is_locked in LeetcodeProblem.IsLocked.ALL.value:
            filter_list.append(LeetcodeProblem.is_locked == is_locked)
        if type in LeetcodeProblem.Type.ALL.value:
            filter_list.append(LeetcodeProblem.type == type)

        cnt = ProblemService.count_problems_by(difficulty, is_locked, type)
        page_util = PageUtil(page, page_size, cnt)

        res = LeetcodeProblem.query.filter(*filter_list).order_by(LeetcodeProblem.lid.asc()).slice(
            page_util.get_start(), page_util.get_end()).all()

        page_util.data = models2dict(res)

        for data in page_util.data:
            del data['code_def']
            del data['desc']

        return page_util

    @staticmethod
    def list_problems_order_by_lid_desc(page, page_size, difficulty=100, is_locked=100, type=100):
        """
        根据题号降序
        :param difficulty:
        :param is_locked:
        :param type:
        :return:
        """
        if page <= 0 or page_size <= 0:
            raise ServiceException(ErrorCode.PARAM_ERROR, u'page或者page_size参数错误')
        # 过滤
        filter_list = []
        if difficulty in LeetcodeProblem.Difficulty.ALL.value:
            filter_list.append(LeetcodeProblem.difficulty == difficulty)
        if is_locked in LeetcodeProblem.IsLocked.ALL.value:
            filter_list.append(LeetcodeProblem.is_locked == is_locked)
        if type in LeetcodeProblem.Type.ALL.value:
            filter_list.append(LeetcodeProblem.type == type)

        cnt = ProblemService.count_problems_by(difficulty, is_locked, type)
        page_util = PageUtil(page, page_size, cnt)

        res = LeetcodeProblem.query.filter(*filter_list).order_by(LeetcodeProblem.lid.desc()).slice(
            page_util.get_start(), page_util.get_end()).all()

        page_util.data = models2dict(res)

        for data in page_util.data:
            del data['code_def']
            del data['desc']

        return page_util

    @staticmethod
    def list_problems_order_by_frequency_asc(page, page_size, difficulty=100, is_locked=100, type=100):
        """
        根据频率升序
        :param difficulty:
        :param is_locked:
        :param type:
        :return:
        """
        if page <= 0 or page_size <= 0:
            raise ServiceException(ErrorCode.PARAM_ERROR, u'page或者page_size参数错误')
        # 过滤
        filter_list = []
        if difficulty in LeetcodeProblem.Difficulty.ALL.value:
            filter_list.append(LeetcodeProblem.difficulty == difficulty)
        if is_locked in LeetcodeProblem.IsLocked.ALL.value:
            filter_list.append(LeetcodeProblem.is_locked == is_locked)
        if type in LeetcodeProblem.Type.ALL.value:
            filter_list.append(LeetcodeProblem.type == type)

        cnt = ProblemService.count_problems_by(difficulty, is_locked, type)
        page_util = PageUtil(page, page_size, cnt)

        res = LeetcodeProblem.query.filter(*filter_list).order_by(LeetcodeProblem.frequency.asc()).slice(
            page_util.get_start(),
            page_util.get_end()).all()

        page_util.data = models2dict(res)

        for data in page_util.data:
            del data['code_def']
            del data['desc']

        return page_util

    @staticmethod
    def list_problems_order_by_frequency_desc(page, page_size, difficulty=100, is_locked=100, type=100):
        """
        根据频率降序
        :param difficulty:
        :param is_locked:
        :param type:
        :return:
        """
        if page <= 0 or page_size <= 0:
            raise ServiceException(ErrorCode.PARAM_ERROR, u'page或者page_size参数错误')
        # 过滤
        filter_list = []
        if difficulty in LeetcodeProblem.Difficulty.ALL.value:
            filter_list.append(LeetcodeProblem.difficulty == difficulty)
        if is_locked in LeetcodeProblem.IsLocked.ALL.value:
            filter_list.append(LeetcodeProblem.is_locked == is_locked)
        if type in LeetcodeProblem.Type.ALL.value:
            filter_list.append(LeetcodeProblem.type == type)

        cnt = ProblemService.count_problems_by(difficulty, is_locked, type)
        page_util = PageUtil(page, page_size, cnt)

        res = LeetcodeProblem.query.filter(*filter_list).order_by(LeetcodeProblem.frequency.desc()).slice(
            page_util.get_start(),
            page_util.get_end()).all()

        page_util.data = models2dict(res)

        for data in page_util.data:
            del data['code_def']
            del data['desc']

        return page_util

    @staticmethod
    def search_problems_by_title(title):
        """
        根据名称模糊匹配
        :param title:
        :param page:
        :param page_size:
        :return:
        """

        res = LeetcodeProblem.query.filter(LeetcodeProblem.title.like('%' + title + '%')).order_by(
            LeetcodeProblem.lid.asc()).all()

        return res

    @staticmethod
    def search_problems_by_content(content):
        """
        根据内容模糊匹配
        :param title:
        :param page:
        :param page_size:
        :return:
        """

        res = LeetcodeProblem.query.filter(LeetcodeProblem.title.like('%' + content + '%')).order_by(
            LeetcodeProblem.lid.asc()).all()

        return res

    @staticmethod
    def list_companies_order_by_problem_cnt():
        """
        获取所有公司名称
        :return:
        """

        res = db.session.query(LeetcodeTagInfo.name, LeetcodeTagInfo.questions).all()
        res = map(lambda x: (x[0], len(x[1][1:len(x[1]) - 1].split(","))), res)
        res.sort(key=lambda x: x[1], reverse=True)
        return res

    @staticmethod
    def list_problems_by_company_name(name, page, page_size, difficulty=100, is_locked=100, type=100):
        """
        根据公司名称查询题目信息
        :param name:
        :param page:
        :param page_size:
        :param difficulty:
        :param is_locked:
        :param type:
        :return:
        """

        if page <= 0 or page_size <= 0:
            raise ServiceException(ErrorCode.PARAM_ERROR, u'page或者page_size参数错误')

        # 查询公司的题目信息
        problems = db.session.query(LeetcodeTagInfo.questions).filter(LeetcodeTagInfo.name == name).first()[0]
        problems = problems[1:len(problems) - 1].split(',')
        problems = map(lambda qid: int(qid), problems)

        problems.sort()
        problems = tuple(problems)
        # 过滤
        filter_list = [LeetcodeProblem.qid.in_(problems)]
        if difficulty in LeetcodeProblem.Difficulty.ALL.value:
            filter_list.append(LeetcodeProblem.difficulty == difficulty)
        if is_locked in LeetcodeProblem.IsLocked.ALL.value:
            filter_list.append(LeetcodeProblem.is_locked == is_locked)
        if type in LeetcodeProblem.Type.ALL.value:
            filter_list.append(LeetcodeProblem.type == type)

        cnt = len(LeetcodeProblem.query.filter(*filter_list).order_by(LeetcodeProblem.frequency.desc()).all())

        page_util = PageUtil(page, page_size, cnt)

        res = LeetcodeProblem.query.filter(*filter_list).order_by(LeetcodeProblem.frequency.desc()).slice(
            page_util.get_start(),
            page_util.get_end()).all()

        page_util.data = models2dict(res)

        for data in page_util.data:
            del data['code_def']
            del data['desc']

        return page_util

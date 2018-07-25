# coding=utf-8
'题目服务'
from common.exception import ServiceException, ErrorCode
from model.leetcode_problems import LeetcodeProblem

__author__ = 'Jiateng Liang'


class ProblemService(object):

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
            filter_list.append(LeetcodeProblem.IsLocked == is_locked)
        if type in LeetcodeProblem.Type.ALL.value:
            filter_list.append(LeetcodeProblem.Type == type)

        res = LeetcodeProblem.query.filter(*filter_list).order_by(LeetcodeProblem.lid.asc()).slice(
            (page - 1) * page_size,
            page * page_size).all()

        return res

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
            filter_list.append(LeetcodeProblem.IsLocked == is_locked)
        if type in LeetcodeProblem.Type.ALL.value:
            filter_list.append(LeetcodeProblem.Type == type)

        res = LeetcodeProblem.query.filter(*filter_list).order_by(LeetcodeProblem.frequency.asc()).slice(
            (page - 1) * page_size,
            page * page_size).all()

        return res

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
            filter_list.append(LeetcodeProblem.IsLocked == is_locked)
        if type in LeetcodeProblem.Type.ALL.value:
            filter_list.append(LeetcodeProblem.Type == type)

        res = LeetcodeProblem.query.filter(*filter_list).order_by(LeetcodeProblem.frequency.desc()).slice(
            (page - 1) * page_size,
            page * page_size).all()

        return res

    @staticmethod
    def search_problems_by_title(title, page, page_size):
        """
        根据名称模糊匹配
        :param title:
        :param page:
        :param page_size:
        :return:
        """
        if page <= 0 or page_size <= 0:
            raise ServiceException(ErrorCode.PARAM_ERROR, u'page或者page_size参数错误')
        res = LeetcodeProblem.query.filter(LeetcodeProblem.title.like('%' + title + '%')).order_by(
            LeetcodeProblem.lid.asc()).slice(
            (page - 1) * page_size,
            page * page_size).all()
        return res

    @staticmethod
    def search_problems_by_content(content, page, page_size):
        """
        根据内容模糊匹配
        :param title:
        :param page:
        :param page_size:
        :return:
        """
        if page <= 0 or page_size <= 0:
            raise ServiceException(ErrorCode.PARAM_ERROR, u'page或者page_size参数错误')
        res = LeetcodeProblem.query.filter(LeetcodeProblem.desc.like('%' + content + '%')).order_by(
            LeetcodeProblem.lid.asc()).slice(
            (page - 1) * page_size,
            page * page_size).all()
        return res



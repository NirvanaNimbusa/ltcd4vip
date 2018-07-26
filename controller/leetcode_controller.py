# coding=utf-8
'leetcode题目前端控制器'
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired

from common.form_util import validate_form

__author__ = 'Jiateng Liang'
from common.exception import api, ErrorCode
from flask import Blueprint, jsonify, request
from service.problem_service import ProblemService
from common.model_util import models2dict, model2dict, json_resp
from bootstrap_init import app
from wtforms import IntegerField

problem_bp = Blueprint('problem_bp', __name__)


class ListProblemsForm(FlaskForm):
    page = IntegerField('page', default=1)
    difficulty = IntegerField('difficulty', default=100)
    is_locked = IntegerField('is_locked', default=100)
    type = IntegerField('type', default=100)
    order = IntegerField('order', default=0)


@problem_bp.route('/lid/<lid>', methods=['GET'])
@api
def get_leetcode_problem_by_lid(lid):
    """
    @api {get} /api/v1/problems/lid/<lid> 根据LeetCode题号获取题目信息
    @apiVersion 1.0.0
    @apiGroup LeetCode Problems
    @apiParam {int} lid 题号
    @apiSuccess {int} lid 题号
    @apiSuccess {int} qid LeetCode题目Id
    @apiSuccess {String} title 题目标题
    @apiSuccess {String} desc 题目描述
    @apiSuccess {String} code_def 编辑器默认代码
    @apiSuccess {int} difficulty 难度：1 easy, 2 medium, 3 hard
    @apiSuccess {int} is_locked 是否上锁：0否, 1是
    @apiSuccess {int} type 题目类型：0算法，1数据库
    @apiSuccess {int} difficulty 难度：1 easy, 2 medium, 3 hard
    @apiSuccess {float} frequency 题目热度
    @apiSuccess {String} title_slug 题目title的url缩写
    @apiSuccess {String} submit_url 题目代码提交url
    @apiError {int} code -1 失败，1成功，3参数错误，4资源没找到，5系统错误

    @apiSuccessExample {json} Success-Response:
    {
        "code": 1,
        "data": {
            "code_def": "[{\"value\": \"cpp\", \"text\": \"C++\", \"defaultCode\": \"class Solution {\\r\\npublic:\\r\\n    int findNthDigit(int n) {\\r\\n        \\r\\n    }\\r\\n};\"}, {\"value\": \"java\", \"text\": \"Java\", \"defaultCode\": \"class Solution {\\n    public int findNthDigit(int n) {\\n        \\n    }\\n}\"}, {\"value\": \"python\", \"text\": \"Python\", \"defaultCode\": \"class Solution(object):\\r\\n    def findNthDigit(self, n):\\r\\n        \\\"\\\"\\\"\\r\\n        :type n: int\\r\\n        :rtype: int\\r\\n        \\\"\\\"\\\"\\r\\n        \"}, {\"value\": \"python3\", \"text\": \"Python3\", \"defaultCode\": \"class Solution:\\n    def findNthDigit(self, n):\\n        \\\"\\\"\\\"\\n        :type n: int\\n        :rtype: int\\n        \\\"\\\"\\\"\\n        \"}, {\"value\": \"c\", \"text\": \"C\", \"defaultCode\": \"int findNthDigit(int n) {\\r\\n    \\r\\n}\"}, {\"value\": \"csharp\", \"text\": \"C#\", \"defaultCode\": \"public class Solution {\\r\\n    public int FindNthDigit(int n) {\\r\\n        \\r\\n    }\\r\\n}\"}, {\"value\": \"javascript\", \"text\": \"JavaScript\", \"defaultCode\": \"/**\\r\\n * @param {number} n\\r\\n * @return {number}\\r\\n */\\r\\nvar findNthDigit = function(n) {\\r\\n    \\r\\n};\"}, {\"value\": \"ruby\", \"text\": \"Ruby\", \"defaultCode\": \"# @param {Integer} n\\r\\n# @return {Integer}\\r\\ndef find_nth_digit(n)\\r\\n    \\r\\nend\"}, {\"value\": \"swift\", \"text\": \"Swift\", \"defaultCode\": \"class Solution {\\r\\n    func findNthDigit(_ n: Int) -> Int {\\r\\n        \\r\\n    }\\r\\n}\"}, {\"value\": \"golang\", \"text\": \"Go\", \"defaultCode\": \"func findNthDigit(n int) int {\\r\\n    \\r\\n}\"}, {\"value\": \"scala\", \"text\": \"Scala\", \"defaultCode\": \"object Solution {\\n    def findNthDigit(n: Int): Int = {\\n        \\n    }\\n}\"}, {\"value\": \"kotlin\", \"text\": \"Kotlin\", \"defaultCode\": \"class Solution {\\n    fun findNthDigit(n: Int): Int {\\n        \\n    }\\n}\"}]",
            "create_time": "2018-07-26 13:05:19",
            "desc": "<p>Find the <i>n</i><sup>th</sup> digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... </p>\r\n\r\n<p><b>Note:</b><br />\r\n<i>n</i> is positive and will fit within the range of a 32-bit signed integer (<i>n</i> < 2<sup>31</sup>).\r\n</p>\r\n\r\n<p><b>Example 1:</b>\r\n<pre>\r\n<b>Input:</b>\r\n3\r\n\r\n<b>Output:</b>\r\n3\r\n</pre>\r\n</p>\r\n\r\n<p><b>Example 2:</b>\r\n<pre>\r\n<b>Input:</b>\r\n11\r\n\r\n<b>Output:</b>\r\n0\r\n\r\n<b>Explanation:</b>\r\nThe 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.\r\n</pre>\r\n</p>",
            "difficulty": 1,
            "frequency": 285.832,
            "id": 466,
            "is_locked": 0,
            "lid": 400,
            "qid": 400,
            "submit_url": "/problems/nth-digit/submit/",
            "title": "Nth Digit",
            "title_slug": "nth-digit",
            "type": 0,
            "update_time": "2018-07-26 12:53:44"
        },
        "msg": "success"
    }
    """
    problem = ProblemService.get_problem_by_lid(lid)

    return jsonify(json_resp(data=model2dict(problem)))


@problem_bp.route('/title/<title_slug>', methods=['GET'])
@api
def get_leetcode_problem_by_title_slug(title_slug):
    """
    @api {get} /api/v1/problems/title/<title_slug> 根据LeetCode的title_slug获取题目信息
    @apiVersion 1.0.0
    @apiGroup LeetCode Problems
    @apiParam {title_slug} title_slug
    @apiSuccess {int} lid 题号
    @apiSuccess {int} qid LeetCode题目Id
    @apiSuccess {String} title 题目标题
    @apiSuccess {String} desc 题目描述
    @apiSuccess {String} code_def 编辑器默认代码
    @apiSuccess {int} difficulty 难度：1 easy, 2 medium, 3 hard
    @apiSuccess {int} is_locked 是否上锁：0否, 1是
    @apiSuccess {int} type 题目类型：0算法，1数据库
    @apiSuccess {int} difficulty 难度：1 easy, 2 medium, 3 hard
    @apiSuccess {float} frequency 题目热度
    @apiSuccess {String} title_slug 题目title的url缩写
    @apiSuccess {String} submit_url 题目代码提交url
    @apiError {int} code -1 失败，1成功，3参数错误，4资源没找到，5系统错误

    @apiSuccessExample {json} Success-Response:
    {
        "code": 1,
        "data": {
            "code_def": "[{\"value\": \"cpp\", \"text\": \"C++\", \"defaultCode\": \"class Solution {\\r\\npublic:\\r\\n    int findNthDigit(int n) {\\r\\n        \\r\\n    }\\r\\n};\"}, {\"value\": \"java\", \"text\": \"Java\", \"defaultCode\": \"class Solution {\\n    public int findNthDigit(int n) {\\n        \\n    }\\n}\"}, {\"value\": \"python\", \"text\": \"Python\", \"defaultCode\": \"class Solution(object):\\r\\n    def findNthDigit(self, n):\\r\\n        \\\"\\\"\\\"\\r\\n        :type n: int\\r\\n        :rtype: int\\r\\n        \\\"\\\"\\\"\\r\\n        \"}, {\"value\": \"python3\", \"text\": \"Python3\", \"defaultCode\": \"class Solution:\\n    def findNthDigit(self, n):\\n        \\\"\\\"\\\"\\n        :type n: int\\n        :rtype: int\\n        \\\"\\\"\\\"\\n        \"}, {\"value\": \"c\", \"text\": \"C\", \"defaultCode\": \"int findNthDigit(int n) {\\r\\n    \\r\\n}\"}, {\"value\": \"csharp\", \"text\": \"C#\", \"defaultCode\": \"public class Solution {\\r\\n    public int FindNthDigit(int n) {\\r\\n        \\r\\n    }\\r\\n}\"}, {\"value\": \"javascript\", \"text\": \"JavaScript\", \"defaultCode\": \"/**\\r\\n * @param {number} n\\r\\n * @return {number}\\r\\n */\\r\\nvar findNthDigit = function(n) {\\r\\n    \\r\\n};\"}, {\"value\": \"ruby\", \"text\": \"Ruby\", \"defaultCode\": \"# @param {Integer} n\\r\\n# @return {Integer}\\r\\ndef find_nth_digit(n)\\r\\n    \\r\\nend\"}, {\"value\": \"swift\", \"text\": \"Swift\", \"defaultCode\": \"class Solution {\\r\\n    func findNthDigit(_ n: Int) -> Int {\\r\\n        \\r\\n    }\\r\\n}\"}, {\"value\": \"golang\", \"text\": \"Go\", \"defaultCode\": \"func findNthDigit(n int) int {\\r\\n    \\r\\n}\"}, {\"value\": \"scala\", \"text\": \"Scala\", \"defaultCode\": \"object Solution {\\n    def findNthDigit(n: Int): Int = {\\n        \\n    }\\n}\"}, {\"value\": \"kotlin\", \"text\": \"Kotlin\", \"defaultCode\": \"class Solution {\\n    fun findNthDigit(n: Int): Int {\\n        \\n    }\\n}\"}]",
            "create_time": "2018-07-26 13:05:19",
            "desc": "<p>Find the <i>n</i><sup>th</sup> digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... </p>\r\n\r\n<p><b>Note:</b><br />\r\n<i>n</i> is positive and will fit within the range of a 32-bit signed integer (<i>n</i> < 2<sup>31</sup>).\r\n</p>\r\n\r\n<p><b>Example 1:</b>\r\n<pre>\r\n<b>Input:</b>\r\n3\r\n\r\n<b>Output:</b>\r\n3\r\n</pre>\r\n</p>\r\n\r\n<p><b>Example 2:</b>\r\n<pre>\r\n<b>Input:</b>\r\n11\r\n\r\n<b>Output:</b>\r\n0\r\n\r\n<b>Explanation:</b>\r\nThe 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.\r\n</pre>\r\n</p>",
            "difficulty": 1,
            "frequency": 285.832,
            "id": 466,
            "is_locked": 0,
            "lid": 400,
            "qid": 400,
            "submit_url": "/problems/nth-digit/submit/",
            "title": "Nth Digit",
            "title_slug": "nth-digit",
            "type": 0,
            "update_time": "2018-07-26 12:53:44"
        },
        "msg": "success"
    }
    """
    problem = ProblemService.get_problem_by_title_slug(title_slug)

    return jsonify(json_resp(data=model2dict(problem)))


@problem_bp.route("/lid", methods=['GET'])
@api
def list_leetcode_problems_by_lid():
    """
    @api {get} /api/v1/problems/lid 获取题目列表(根据题号排序)
    @apiVersion 1.0.0
    @apiGroup LeetCode Problems
    @apiParam {int} [page] 页码 默认为1
    @apiParam {int} [difficulty] 难度：1 easy, 2 medium, 3 hard
    @apiParam {int} [is_locked] 是否上锁：0否, 1是
    @apiParam {int} [type] 题目类型：0算法，1数据库
    @apiParam {int} [order] 排序类型：0升序，1降序
    @apiSuccess {int} lid 题号
    @apiSuccess {int} qid LeetCode题目Id
    @apiSuccess {String} title 题目标题
    @apiSuccess {int} difficulty 难度：1 easy, 2 medium, 3 hard
    @apiSuccess {int} is_locked 是否上锁：0否, 1是
    @apiSuccess {int} type 题目类型：0算法，1数据库
    @apiSuccess {int} difficulty 难度：1 easy, 2 medium, 3 hard
    @apiSuccess {float} frequency 题目热度
    @apiSuccess {String} title_slug 题目title的url缩写
    @apiSuccess {String} submit_url 题目代码提交url
    @apiError {int} code -1 失败，1成功，3参数错误，4资源没找到，5系统错误

    @apiSuccessExample {json} Success-Response:
    {
        "code": 200,
        "data": {
            "data": [
                {
                    "create_time": "2018-07-26 11:56:05",
                    "difficulty": 3,
                    "frequency": 104.272,
                    "id": 315,
                    "is_locked": 1,
                    "lid": 571,
                    "qid": 571,
                    "submit_url": "/problems/find-median-given-frequency-of-numbers/submit/",
                    "title": "Find Median Given Frequency of Numbers",
                    "title_slug": "find-median-given-frequency-of-numbers",
                    "type": 0,
                    "update_time": "2018-07-26 13:01:31"
                }
            ],
            "max_cnt": 1,
            "max_page": 1,
            "page": 1,
            "page_size": 50
        },
        "msg": "success"
    }
    """
    form = ListProblemsForm(formdata=request.args)
    validate_form(form)
    page_size = app.config['PAGE_LARGE']
    if form.order is not None and form.order.data == 1:
        problems = ProblemService.list_problems_order_by_lid_asc(form.page.data, page_size,
                                                                 difficulty=form.difficulty.data,
                                                                 is_locked=form.is_locked.data, type=form.type.data)
    else:
        problems = ProblemService.list_problems_order_by_lid_desc(form.page.data, page_size,
                                                                  difficulty=form.difficulty.data,
                                                                  is_locked=form.is_locked.data, type=form.type.data)

    return jsonify(json_resp(data=model2dict(problems)))


@problem_bp.route("/frequency", methods=['GET'])
@api
def list_leetcode_problems_by_frequency():
    """
    @api {get} /api/v1/problems/frequency 获取题目列表(根据题目频率排序)
    @apiVersion 1.0.0
    @apiGroup LeetCode Problems
    @apiParam {int} [page] 页码 默认为1
    @apiParam {int} [difficulty] 难度：1 easy, 2 medium, 3 hard
    @apiParam {int} [is_locked] 是否上锁：0否, 1是
    @apiParam {int} [type] 题目类型：0算法，1数据库
    @apiParam {int} [order] 排序类型：0升序，1降序
    @apiSuccess {int} lid 题号
    @apiSuccess {int} qid LeetCode题目Id
    @apiSuccess {String} title 题目标题
    @apiSuccess {int} difficulty 难度：1 easy, 2 medium, 3 hard
    @apiSuccess {int} is_locked 是否上锁：0否, 1是
    @apiSuccess {int} type 题目类型：0算法，1数据库
    @apiSuccess {int} difficulty 难度：1 easy, 2 medium, 3 hard
    @apiSuccess {float} frequency 题目热度
    @apiSuccess {String} title_slug 题目title的url缩写
    @apiSuccess {String} submit_url 题目代码提交url
    @apiError {int} code -1 失败，1成功，3参数错误，4资源没找到，5系统错误

    @apiSuccessExample {json} Success-Response:
    {
        "code": 200,
        "data": {
            "data": [
                {
                    "create_time": "2018-07-26 11:56:05",
                    "difficulty": 3,
                    "frequency": 104.272,
                    "id": 315,
                    "is_locked": 1,
                    "lid": 571,
                    "qid": 571,
                    "submit_url": "/problems/find-median-given-frequency-of-numbers/submit/",
                    "title": "Find Median Given Frequency of Numbers",
                    "title_slug": "find-median-given-frequency-of-numbers",
                    "type": 0,
                    "update_time": "2018-07-26 13:01:31"
                }
            ],
            "max_cnt": 1,
            "max_page": 1,
            "page": 1,
            "page_size": 50
        },
        "msg": "success"
    }
    """
    form = ListProblemsForm(formdata=request.args)
    validate_form(form)
    page_size = app.config['PAGE_LARGE']

    if form.order is not None and form.order.data == 1:
        problems = ProblemService.list_problems_order_by_frequency_desc(form.page.data, page_size,
                                                                        difficulty=form.difficulty.data,
                                                                        is_locked=form.is_locked.data,
                                                                        type=form.type.data)
    else:
        problems = ProblemService.list_problems_order_by_frequency_asc(form.page.data, page_size,
                                                                       difficulty=form.difficulty.data,
                                                                       is_locked=form.is_locked.data,
                                                                       type=form.type.data)

    return jsonify(json_resp(data=model2dict(problems)))


@problem_bp.route("/search/title/<title>", methods=['GET'])
@api
def search_problems_by_title(title):
    """
    @api {get} /api/v1/problems/search/title/<title> 根据题目标题搜索
    @apiVersion 1.0.0
    @apiGroup LeetCode Problems
    @apiParam {int} [page] 页码 默认为1
    @apiSuccess {int} lid 题号
    @apiSuccess {int} qid LeetCode题目Id
    @apiSuccess {String} title 题目标题
    @apiSuccess {int} difficulty 难度：1 easy, 2 medium, 3 hard
    @apiSuccess {int} is_locked 是否上锁：0否, 1是
    @apiSuccess {int} type 题目类型：0算法，1数据库
    @apiSuccess {int} difficulty 难度：1 easy, 2 medium, 3 hard
    @apiSuccess {float} frequency 题目热度
    @apiSuccess {String} title_slug 题目title的url缩写
    @apiSuccess {String} submit_url 题目代码提交url
    @apiError {int} code -1 失败，1成功，3参数错误，4资源没找到，5系统错误

    @apiSuccessExample {json} Success-Response:
    {
        "code": 200,
        "data": {
            "data": [
                {
                    "create_time": "2018-07-26 11:56:05",
                    "difficulty": 3,
                    "frequency": 104.272,
                    "id": 315,
                    "is_locked": 1,
                    "lid": 571,
                    "qid": 571,
                    "submit_url": "/problems/find-median-given-frequency-of-numbers/submit/",
                    "title": "Find Median Given Frequency of Numbers",
                    "title_slug": "find-median-given-frequency-of-numbers",
                    "type": 0,
                    "update_time": "2018-07-26 13:01:31"
                }
            ],
            "max_cnt": 1,
            "max_page": 1,
            "page": 1,
            "page_size": 50
        },
        "msg": "success"
    }
    """
    page = request.args.get('page')
    if page is None:
        page = 1
    page_size = app.config['PAGE_LARGE']
    problems = ProblemService.search_problems_by_title(title, page, page_size)
    return jsonify(json_resp(data=model2dict(problems)))


@problem_bp.route("/search/content/<content>", methods=['GET'])
@api
def search_problems_by_content(content):
    """
    @api {get} /api/v1/problems/search/content/<content> 根据题目内容搜索
    @apiVersion 1.0.0
    @apiGroup LeetCode Problems
    @apiParam {int} [page] 页码 默认为1
    @apiSuccess {int} lid 题号
    @apiSuccess {int} qid LeetCode题目Id
    @apiSuccess {String} title 题目标题
    @apiSuccess {int} difficulty 难度：1 easy, 2 medium, 3 hard
    @apiSuccess {int} is_locked 是否上锁：0否, 1是
    @apiSuccess {int} type 题目类型：0算法，1数据库
    @apiSuccess {int} difficulty 难度：1 easy, 2 medium, 3 hard
    @apiSuccess {float} frequency 题目热度
    @apiSuccess {String} title_slug 题目title的url缩写
    @apiSuccess {String} submit_url 题目代码提交url
    @apiError {int} code -1 失败，1成功，3参数错误，4资源没找到，5系统错误

    @apiSuccessExample {json} Success-Response:
    {
        "code": 200,
        "data": {
            "data": [
                {
                    "create_time": "2018-07-26 11:56:05",
                    "difficulty": 3,
                    "frequency": 104.272,
                    "id": 315,
                    "is_locked": 1,
                    "lid": 571,
                    "qid": 571,
                    "submit_url": "/problems/find-median-given-frequency-of-numbers/submit/",
                    "title": "Find Median Given Frequency of Numbers",
                    "title_slug": "find-median-given-frequency-of-numbers",
                    "type": 0,
                    "update_time": "2018-07-26 13:01:31"
                }
            ],
            "max_cnt": 1,
            "max_page": 1,
            "page": 1,
            "page_size": 50
        },
        "msg": "success"
    }
    """
    page = request.args.get('page')
    if page is None:
        page = 1
    page_size = app.config['PAGE_LARGE']
    problems = ProblemService.search_problems_by_content(content, page, page_size)
    return jsonify(json_resp(data=model2dict(problems)))


@problem_bp.route("/companies", methods=['GET'])
@api
def list_companies():
    """
    @api {get} /api/v1/problems/companies 列出所有公司
    @apiVersion 1.0.0
    @apiGroup LeetCode Problems
    @apiError {int} code -1 失败，1成功，3参数错误，4资源没找到，5系统错误
    @apiSuccessExample {json} Success-Response:
    {
        "code": 1,
        "data": [
            "Adobe",
            "Aetion",
            "Affirm",
            "Airbnb",
            "Akuna Capital",
            "Alibaba",
            "Amazon"
        ],
        "msg": "success"
    }
    """
    companies = ProblemService.list_companies_order_by_problem_cnt()
    return jsonify(json_resp(data=companies))


@problem_bp.route("/companies/<name>", methods=['GET'])
@api
def list_problems_by_company_name(name):
    """
    @api {get} /api/v1/problems/companies/<name> 根据公司名称查询公司下面的题目
    @apiVersion 1.0.0
    @apiGroup LeetCode Problems
    @apiParam {int} [page] 页码 默认为1
    @apiParam {int} [difficulty] 难度：1 easy, 2 medium, 3 hard
    @apiParam {int} [is_locked] 是否上锁：0否, 1是
    @apiParam {int} [type] 题目类型：0算法，1数据库
    @apiSuccess {int} lid 题号
    @apiSuccess {int} qid LeetCode题目Id
    @apiSuccess {String} title 题目标题
    @apiSuccess {int} difficulty 难度：1 easy, 2 medium, 3 hard
    @apiSuccess {int} is_locked 是否上锁：0否, 1是
    @apiSuccess {int} type 题目类型：0算法，1数据库
    @apiSuccess {int} difficulty 难度：1 easy, 2 medium, 3 hard
    @apiSuccess {float} frequency 题目热度
    @apiSuccess {String} title_slug 题目title的url缩写
    @apiSuccess {String} submit_url 题目代码提交url
    @apiError {int} code -1 失败，1成功，3参数错误，4资源没找到，5系统错误
    @apiSuccessExample {json} Success-Response:
    {
        "code": 200,
        "data": {
            "data": [
                {
                    "create_time": "2018-07-26 11:56:05",
                    "difficulty": 3,
                    "frequency": 104.272,
                    "id": 315,
                    "is_locked": 1,
                    "lid": 571,
                    "qid": 571,
                    "submit_url": "/problems/find-median-given-frequency-of-numbers/submit/",
                    "title": "Find Median Given Frequency of Numbers",
                    "title_slug": "find-median-given-frequency-of-numbers",
                    "type": 0,
                    "update_time": "2018-07-26 13:01:31"
                }
            ],
            "max_cnt": 1,
            "max_page": 1,
            "page": 1,
            "page_size": 50
        },
        "msg": "success"
    }
    """
    page = request.args.get('page')
    if page is None:
        page = 1
    page_size = app.config['PAGE_LARGE']
    problems = ProblemService.list_problems_by_company_name(name, page, page_size)
    return jsonify(json_resp(data=model2dict(problems)))


app.register_blueprint(problem_bp, url_prefix='/api/v1/problems')

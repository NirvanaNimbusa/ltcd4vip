# coding=utf-8
'leetcode题目前端控制器'
__author__ = 'Jiateng Liang'
from common.exception import api
from flask import Blueprint, jsonify
from service.leetcode_service import LeetCodeService
from bootstrap_init import app

leetcode_bp = Blueprint('leetcode_bp', __name__)


@leetcode_bp.route('/<lid>')
@api
def get_leetcode_problem_by_lid(lid):
    """
    @api {get} /api/v1/problems/<lid> 根据LeetCode题号获取题目信息
    @apiVersion 1.0.0
    @apiGroup LeetCode Problems
    @apiParam {int} lid 题号
    @apiSuccessExample {json} Success-Response:
    {
        "content":"This is an example content"
    }
    """
    problem = LeetCodeService.get_leetcode_problem_by_lid(lid)
    data = {'id': problem.id, 'lid': problem.lid, 'title': problem.title, 'desc': problem.desc}
    return jsonify(data)


app.register_blueprint(leetcode_bp, url_prefix='/api/v1/problems')

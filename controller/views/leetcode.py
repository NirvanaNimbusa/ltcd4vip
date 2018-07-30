# coding=utf-8
'comment'
from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import IntegerField

from bootstrap_init import app
from common.form_util import validate_form
from common.model_util import model2dict
from service.problem_service import ProblemService

__author__ = 'Jiateng Liang'


class ListProblemsForm(FlaskForm):
    page = IntegerField('page', default=1)
    difficulty = IntegerField('difficulty', default=100)
    is_locked = IntegerField('is_locked', default=100)
    type = IntegerField('type', default=100)
    order = IntegerField('order', default=0)
    frequency = IntegerField('frequency', default=100)


@app.route('/leetcode/<type>')
def main(type):
    form = ListProblemsForm(formdata=request.args)
    validate_form(form)
    page_size = app.config['PAGE_LARGE']

    if type == 'database':
        p_type = 1
    elif type == 'algorithm':
        p_type = 0
    else:
        p_type = 100

    if form.order.data == 0:
        problems = ProblemService.list_problems_order_by_lid_asc(form.page.data, page_size,
                                                                 difficulty=form.difficulty.data,
                                                                 is_locked=form.is_locked.data, type=p_type)
    else:
        problems = ProblemService.list_problems_order_by_lid_desc(form.page.data, page_size,
                                                                  difficulty=form.difficulty.data,
                                                                  is_locked=form.is_locked.data, type=p_type)

    if form.frequency.data == 1:
        problems = ProblemService.list_problems_order_by_frequency_desc(form.page.data, page_size,
                                                                        difficulty=form.difficulty.data,
                                                                        is_locked=form.is_locked.data, type=p_type)

    status = {'difficulty': form.difficulty.data, 'is_locked': form.is_locked.data, 'type': type,
              'order': form.order.data, 'frequency': form.frequency.data}

    companies = ProblemService.list_companies_order_by_problem_cnt()

    return render_template('index.html', data=model2dict(problems), status=status, companies=companies,
                           page=form.page.data)

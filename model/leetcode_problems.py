# coding=utf-8
'LeetCode题目信息'

__author__ = 'Jiateng Liang'
from enum import Enum
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, Float
from common.enum_util import labels
from bootstrap_init import db


class LeetcodeProblem(db.Model):
    __tablename__ = "leetcode_problems"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    lid = Column(Integer, unique=True, comment='前端展现题目号')
    qid = Column(Integer, unique=True, comment='LeetCode题目真正Id')
    title = Column(String(100), comment='题目')
    desc = Column(Text, comment='题干')
    difficulty = Column(Integer, nullable=False, comment='1简单 2中等 3困难', default=0)
    is_locked = Column(Integer, nullable=False, comment='0没锁 1上锁', default=0)
    type = Column(Integer, default=0, comment='0算法，1数据库')
    submit_url = Column(String(255), comment='代码提交链接')
    code_def = Column(Text, comment='代码初始化')
    frequency = Column(Float, comment='题目出现频率')
    title_slug = Column(String(150), comment='题目的url名称')
    create_time = Column(DateTime, nullable=False)
    update_time = Column(DateTime, nullable=False, default=datetime.now())

    @labels
    class Difficulty(Enum):
        """
        0简单 1中等 2困难
        """
        EASY = 1
        MEDIUM = 2
        HARD = 3

        __labels__ = {
            EASY: '简单',
            MEDIUM: '中等',
            HARD: '困难',
        }

        ALL = [EASY, MEDIUM, HARD]

    @labels
    class IsLocked(Enum):
        """
        0没锁 1上锁
        """
        UNLOCKED = 0
        LOCKED = 1

        __labels__ = {
            UNLOCKED: '解锁',
            LOCKED: '上锁',
        }
        ALL = [UNLOCKED, LOCKED]

    @labels
    class Type(Enum):
        """
        0算法 1数据库
        """
        ALGO = 0
        DB = 1

        __labels__ = {
            ALGO: '算法',
            DB: '数据库',
        }

        ALL = [ALGO, DB]

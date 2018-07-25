#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'各个公司信息'
from datetime import datetime

__author__ = 'Jiateng Liang'
from sqlalchemy import Column, Integer, String, DateTime, Text
from bootstrap_init import db


class LeetcodeTagInfo(db.Model):
    __tablename__ = 'leetcode_tag_info'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(100), nullable=False, unique=True, comment='标签名称')
    slug = Column(String(150), nullable=False, unique=True, comment='标签url')
    questions = Column(Text, comment='题目id, 里面的id为真实id（qid）')
    create_time = Column(DateTime, nullable=False)
    update_time = Column(DateTime, nullable=False, default=datetime.now())

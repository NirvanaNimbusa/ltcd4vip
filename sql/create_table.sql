create table leetcode_problems
(
  id          int auto_increment
    primary key,
  lid         int          null
  comment '前端展现题目号',
  qid         int          null
  comment 'LeetCode题目真正Id',
  title       varchar(100) null
  comment '题目',
  `desc`      text         null
  comment '题干',
  difficulty  int          not null
  comment '1简单 2中等 3困难',
  is_locked   int          not null
  comment '0没锁 1上锁',
  type        int          null
  comment '0算法，1数据库',
  submit_url  varchar(255) null
  comment '代码提交链接',
  code_def    text         null
  comment '代码初始化',
  frequency   float        null
  comment '题目出现频率',
  title_slug  varchar(150) null
  comment '题目的url名称',
  create_time timestamp     not null,
  update_time timestamp  default current_timestamp   not null,
  constraint lid
  unique (lid),
  constraint qid
  unique (qid)
)engine = InnoDB default charset=utf8;

create table leetcode_tag_info
(
  id          int auto_increment
    primary key,
  name        varchar(100) not null
  comment '标签名称',
  slug        varchar(150) not null
  comment '标签url',
  questions   text         null
  comment '题目id',
  create_time datetime     not null,
  update_time datetime  default current_timestamp  not null,
  constraint name
  unique (name),
  constraint slug
  unique (slug)
) engine = InnoDB default charset=utf8;
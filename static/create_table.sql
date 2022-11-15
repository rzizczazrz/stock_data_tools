--抽样相关表建表sql
1.抽样条件表
CREATE TABLE `example_query_conditions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `condition_type` int(11) NOT NULL COMMENT '页面选择条件类型',
  `condition_value` varchar(32) NOT NULL COMMENT '条件值',
  `comments` varchar(64) NOT NULL COMMENT '用户注释',
  `is_available` int(11) NOT NULL COMMENT '是否可用',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='抽样条件表'

2.分类表
CREATE TABLE `example_class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class_1_value` varchar(32) NOT NULL COMMENT '一级分类',
  `class_2_value` varchar(32) NOT NULL COMMENT '二级分类',
  `comments` varchar(64) NOT NULL COMMENT '用户注释',
  `is_available` int(11) NOT NULL COMMENT '是否可用',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='分类表'


3.抽样任务表


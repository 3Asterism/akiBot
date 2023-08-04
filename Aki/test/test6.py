import json
import os
import random

import jsonpath
import mysql
import requests
from nonebot import on_command

import mysql.connector


def get_uid_data_from_db():
    # 数据库连接参数
    db_host = 'localhost'
    db_user = 'root'
    db_password = '123456'
    db_name = 'live_stats'

    # 连接到MySQL数据库
    conn = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name,
                                   charset='utf8mb4')
    cursor = conn.cursor()

    try:
        # 创建一个数据库连接的游标
        cursor = conn.cursor()

        # 执行 SQL 查询语句，获取数据
        sql = "SELECT `pic`, `title`, `bvid`, `author` FROM `bili_uid_icecreamer_firstvideo`"
        cursor.execute(sql)

        # 获取所有数据行
        result = cursor.fetchall()

        # 将数据拆分为四个列表
        pic_list = []
        title_list = []
        bvid_list = []
        author_list = []

        for row in result:
            pic_list.append(row[0])
            title_list.append(row[1])
            bvid_list.append(row[2])
            author_list.append(row[3])

    finally:
        # 关闭游标和数据库连接
        cursor.close()
        conn.close()

    return pic_list, title_list, bvid_list, author_list


def get_vmdata_from_db():
    # 数据库连接参数
    db_host = 'localhost'
    db_user = 'root'
    db_password = '123456'
    db_name = 'live_stats'

    # 连接到MySQL数据库
    conn = mysql.connector.connect(host=db_host, user=db_user, password=db_password, database=db_name,
                                   charset='utf8mb4')
    cursor = conn.cursor()
    try:
        # 创建一个数据库连接的游标
        cursor = conn.cursor()

        # 执行 SQL 查询语句，获取数据
        sql = "SELECT `pic`, `title`, `short_link_v2`, `pub_location`, `name` FROM `bili_icecreamer_firstvideo`"
        cursor.execute(sql)

        # 获取所有数据行
        result = cursor.fetchall()

        # 将数据拆分为五个列表
        pic_list = []
        title_list = []
        short_link_v2_list = []
        pub_location_list = []
        name_list = []

        for row in result:
            pic_list.append(row[0])
            title_list.append(row[1])
            short_link_v2_list.append(row[2])
            pub_location_list.append(row[3])
            name_list.append(row[4])

    finally:
        # 关闭游标和数据库连接
        cursor.close()
        conn.close()

    return pic_list, title_list, short_link_v2_list, pub_location_list, name_list


# 生成一个包含两个函数的列表
functions = [get_uid_data_from_db, get_vmdata_from_db]

# 抽取权重 调高uid的权重 因为使用uid的up主较多
weights = [5, 1]

# 随机选择一个函数
random_func = random.choices(functions, weights=weights)[0]

# 调用随机选择的函数并获取数据
data = random_func()
print(data)
print(data[0])
print(len(data))
print(len(data) == 5)

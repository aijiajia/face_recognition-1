#!/usr/bin/env python
# encoding: utf-8


"""
@version: 
@author: Herbert
@license: Apache Licence 
@contact: 
@site: 
@software: PyCharm Community Edition
@file: dirStatistics.py
@time: 17-10-10 下午4:23
"""
import os


def CEF(path):
    """
    CLean empty files, 清理空文件夹和空文件
    :param path: 文件路径，检查此文件路径下的子文件
    :return: None
    """
    deleted_dir = []
    files = os.listdir(path)  # 获取路径下的子文件(夹)列表
    for file in files:
        print 'Traversal at', file
        if os.path.isdir(file):  # 如果是文件夹
            if not os.listdir(file):  # 如果子文件为空
                os.rmdir(file)  # 删除这个空文件夹
                deleted_dir.append(os.path.join(path, file))
        # elif os.path.isfile(file):  # 如果是文件
        #     if os.path.getsize(file) == 0:  # 文件大小为0
        #         os.remove(file)  # 删除这个文件
    print("deleted dir(s) : ", deleted_dir)
    print path, 'Dispose over!'


def people_count(dataset_path, limit_count=10):
    dirlists = os.listdir(path)
    people_counts = len(dirlists)
    dict_id_num = {}
    for subdir in dirlists:
        dict_id_num[subdir] = len(os.listdir(os.path.join(path, subdir)))
    sorted_num_id = sorted([(v, k) for k, v in dict_id_num.items()], reverse=True)
    sum_images = sum([v for v, _ in sorted_num_id])
    least10 = sorted_num_id[-10:]
    most10 = sorted_num_id[:10]
    people_limit_count = len([v for v, _ in sorted_num_id if v >= 10])
    print("people_counts : ",people_counts)
    print("image_counts : ", sum_images)
    print("least10 : ", least10)
    print("most10 : ", most10)
    print("people's images more than "+ str(limit_count) + ": is "+ str(people_limit_count))
    print("\tdone...")


if __name__ == '__main__':
    path ='/home/herbert/CASIA-WebFace-croped'
    people_count(path)



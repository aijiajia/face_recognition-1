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

def func():
    pass


if __name__ == '__main__':
    path ='/home/herbert/CASIA-WebFace-croped/'

    dirlists = os.listdir(path)
    dict_id_num = {}
    for subdir in dirlists:
        dict_id_num[subdir] = len(os.listdir(os.path.join(path, subdir)))
    # sorted(dict_id_num.items, key=lambda dict_id_num:dict_id_num[1])
    sorted_num_id = sorted([(v, k) for k, v in dict_id_num.items()], reverse=True)
    select_ids = sorted_num_id[0:10]
    for id in select_ids:
        print(id)

    # fid_train = open(self.data_train, 'w')
    # fid_test = open(self.data_test, 'w')
    #
    # pid = 0
    # for select_id in select_ids:
    #     subdir = select_id[1]
    #     filenamelist = os.listdir(os.path.join(self.datapath, subdir))
    #     num = 1
    #     for filename in filenamelist:
    #         # print select_ids[top_num-1]
    #         if num > select_ids[self.num - 1][0]:
    #             break
    #         if num % ratio != 0:
    #             fid_train.write(os.path.join(subdir, filename) + ' ' + str(pid) + '\n')
    #         else:
    #             fid_test.write(os.path.join(subdir, filename) + ' ' + str(pid) + '\n')
    #         num = num + 1
    #     pid = pid + 1
    # fid_train.close()
    # fid_test.close()
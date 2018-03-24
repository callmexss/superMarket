#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: query_data.py
"
"        Author: xss - callmexss@126.com
"   Description: ---
"        Create: 2018-02-19 01:29:10
"""""""""""""""""""""""""""""""""""""""""""""""


with open("balabala.txt", "r") as f:
    li = f.readlines()

data = {}


for line in li:
    line = line.strip()
    try:
        key, value = line.split()
        data[key] = value
    except:
        pass

# print(data)

data_r = {v: k for k, v in data.items()}


while(1):
    query = input("输入查询: ")
    try:
        for key in data.keys():
            if query in key:
                print(key + '\t' + data[key])
        '''
        for key in data_r.keys():
            if query in key:
                print(key + '\t' + data_r[key])
        '''
    except:
        print("没找到相关查询。")

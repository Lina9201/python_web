#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2022/5/23 22:28
# @Author : zhuxuefei
str2 = "wood programming is the best education"
result = {}
for i in str2:
    result[i] = str2.count(i)
print(result)

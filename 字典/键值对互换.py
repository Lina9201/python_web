#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2022/5/23 22:22
# @Author : zhuxuefei

dict1 = {
    "username": "zhuxuefei",
    "password": "123456"
}

for key, value in dict1.items():
    print(value, key)

print(dict1.items())
print(dict1.keys())
print(dict1.values())
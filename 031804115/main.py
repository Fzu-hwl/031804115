# -*- coding:utf-8 -*-
#!/usr/bin/env python

from __future__ import division
from math import sqrt
import jieba.analyse
from functools import reduce
import time
import sys
class Similarity():

    def __init__(self, target1, target2, topK=1000):
        self.target1 = target1
        self.target2 = target2
        self.topK = topK


    def vector(self):
        self.vdict1 = {}
        self.vdict2 = {}
        top_keywords1 = jieba.analyse.extract_tags(self.target1, topK=self.topK, withWeight=True)
        top_keywords2 = jieba.analyse.extract_tags(self.target2, topK=self.topK, withWeight=True)#提取关键字
        for k, v in top_keywords1:
            self.vdict1[k] = v
        for k, v in top_keywords2:
            self.vdict2[k] = v


    def mix(self):
        for key in self.vdict1:
            self.vdict2[key] = self.vdict2.get(key, 0)
        for key in self.vdict2:
            self.vdict1[key] = self.vdict1.get(key, 0)


        def mapminmax(vdict):
            """计算相对词频"""
            _min = min(vdict.values())
            _max = max(vdict.values())
            _mid = _max - _min
            # print _min, _max, _mid
            for key in vdict:
                vdict[key] = (vdict[key] - _min) / _mid
            return vdict

        self.vdict1 = mapminmax(self.vdict1)
        self.vdict2 = mapminmax(self.vdict2)

#开始计算相似度，利用公式计算

    def similar(self):
        self.vector()
        self.mix()
        sum = 0
        for key in self.vdict1:
            sum += self.vdict1[key] * self.vdict2[key]
        A = sqrt(reduce(lambda x, y: x + y, map(lambda x: x * x, self.vdict1.values())))
        B = sqrt(reduce(lambda x, y: x + y, map(lambda x: x * x, self.vdict2.values())))
        return sum / (A * B)
if __name__ == '__main__':
    orignal=sys.argv[1]
    nexttxt=sys.argv[2]
    output=sys.argv[3]
    f1 = open(orignal, "r", encoding='UTF-8')
    f2 = open(nexttxt, "r", encoding='UTF-8')
    t1 = f1.read()
    t2 = f2.read()
    f1.close()
    f2.close()
    topK = 1000
    s = Similarity(t1, t2, topK)
    result = s.similar()
    result=round(result,2)
    result=str(result)
    try:
        f=open(output,"w")
        f.write(result+"\n")
        f.close()
        print("结果已存入文件夹中")
    except IOError:
        print("Error: 没有找到文件或读取文件失败")

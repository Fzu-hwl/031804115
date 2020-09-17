#!/usr/bin/env python

from __future__ import division
from math import sqrt
import jieba.analyse
from functools import reduce
import time
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
    f1=open("D:\Python\Firstcode\orig.txt","r",encoding='UTF-8')
    f2=open("D:\Python\Firstcode\orig_0.8_add.txt","r",encoding='UTF-8')
    f3 = open("D:\Python\Firstcode\orig_0.8_del.txt", "r", encoding='UTF-8')
    f4 = open("D:\Python\Firstcode\orig_0.8_dis_1.txt", "r", encoding='UTF-8')
    f5 = open("D:\Python\Firstcode\orig_0.8_dis_3.txt", "r", encoding='UTF-8')
    f6 = open("D:\Python\Firstcode\orig_0.8_dis_7.txt", "r", encoding='UTF-8')
    f7 = open("D:\Python\Firstcode\orig_0.8_dis_10.txt", "r", encoding='UTF-8')
    f8 = open("D:\Python\Firstcode\orig_0.8_dis_15.txt", "r", encoding='UTF-8')
    f9 = open("D:\Python\Firstcode\orig_0.8_mix.txt", "r", encoding='UTF-8')
    f10 = open("D:\Python\Firstcode\orig_0.8_rep.txt", "r", encoding='UTF-8')
    t1=f1.read()
    t2=f2.read()
    t3=f3.read()
    t4=f4.read()
    t5=f5.read()
    t6=f6.read()
    t7=f7.read()
    t8=f8.read()
    t9=f9.read()
    t10=f10.read()
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()
    f9.close()
    f10.close()
    topK = 1000
    s = Similarity(t1, t2, topK)
    result = s.similar()
    print('%.2f' % result)
    s = Similarity(t1, t3, topK)
    result3=s.similar()
    print('%.2f' %result3)
    s = Similarity(t1, t4, topK)
    result4 = s.similar()
    print('%.2f' % result4)
    s = Similarity(t1, t5, topK)
    result5 = s.similar()
    print('%.2f' % result5)
    s = Similarity(t1, t6, topK)
    result6 = s.similar()
    print('%.2f' % result6)
    s = Similarity(t1, t7, topK)
    result7 = s.similar()
    print('%.2f' % result7)
    s = Similarity(t1, t8, topK)
    result8 = s.similar()
    print('%.2f' % result8)
    s = Similarity(t1, t9, topK)
    result9 = s.similar()
    print('%.2f' % result9)
    s = Similarity(t1, t10, topK)
    result10 = s.similar()
    print('%.2f' % result10)
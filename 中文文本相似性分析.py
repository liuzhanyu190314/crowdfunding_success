#-*- coding:utf-8 -*-
from cntext.similarity import similarity_score
import pandas as pd
import csv
#train_path="C:\\Users\\liuzhanyu\\Desktop\\众筹成功\\可读性.csv"
train_path="C:\\Users\\liuzhanyu\Desktop\\说服性策略\\数据表格\\中文情感分析.csv"
with open(train_path,'r',encoding='utf-8') as f:
    for t in f:
        array=t.strip().split(',')
        #print(array[0])
        Sim_Cosine=similarity_score(array[1], array[2])
        vector = open('C:\\Users\\liuzhanyu\Desktop\\标题余弦相似度.csv', 'a')
        vector.write(str(Sim_Cosine['Sim_Cosine']))
        vector.write('\n')
        vector.close()






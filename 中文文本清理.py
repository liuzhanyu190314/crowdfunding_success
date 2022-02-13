#-*- coding:utf-8 -*-
from cntext.similarity import similarity_score
import pandas as pd
import csv
from harvesttext import HarvestText
import re
#train_path="C:\\Users\\liuzhanyu\\Desktop\\众筹成功\\可读性.csv"
train_path="C:\\Users\\liuzhanyu\Desktop\\说服性策略\\数据表格\\中文情感分析.csv"
data = pd.read_csv(train_path)
def extract_only_chinese(file):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', file)
    return chinese
for text in data['text']:
    ht0 = HarvestText()
    cleaned_text=ht0.clean_text(text, t2s=True)
    cleaned_text= extract_only_chinese(cleaned_text)
    #print(cleaned_text)
    vector = open('C:\\Users\\liuzhanyu\Desktop\\清理后的详细文本.csv', 'a')
    vector.write(str(cleaned_text))
    vector.write('\n')
    vector.close()


#-*- coding:utf-8 -*-
from cntext.similarity import similarity_score
import pandas as pd
import csv
from harvesttext import HarvestText
import re
import jieba
from cntext import STOPWORDS_zh

import tomotopy as tp

#train_path="C:\\Users\\liuzhanyu\\Desktop\\众筹成功\\可读性.csv"
train_path="C:\\Users\\liuzhanyu\Desktop\\清理后的详细文本.csv"
data = pd.read_csv(train_path,encoding='utf-8')

def segment(text):
    words = jieba.lcut(text)
    words = [w for w in words if w not in STOPWORDS_zh]
    return words

data['words'] = data['text'].apply(segment)
data.head()


def find_k(docs, min_k=1, max_k=20, min_df=2):
    # min_df 词语最少出现在2个文档中
    import matplotlib.pyplot as plt
    scores = []
    for k in range(min_k, max_k):
        # seed随机种子，保证在大邓这里运行结果与你运行的结果一样
        mdl = tp.LDAModel(min_df=min_df, k=k, seed=555)
        for words in docs:
            if words:
                mdl.add_doc(words)
        mdl.train(20)
        coh = tp.coherence.Coherence(mdl)
        scores.append(coh.get_score())

    # x = list(range(min_k, max_k - 1))  # 区间最右侧的值。注意：不能大于max_k
    # print(x)
    # print()
    plt.plot(range(min_k, max_k), scores)
    plt.xlabel("number of topics")
    plt.ylabel("coherence")
    plt.show()


find_k(docs=data['words'], min_k=1, max_k=10, min_df=2)
#初始化LDA
mdl = tp.LDAModel(k=5, min_df=2, seed=555)
for words in data['words']:
    #确认words 是 非空词语列表
    if words:
        mdl.add_doc(words=words)

#训练
mdl.train()

#查看每个topic feature words
for k in range(mdl.k):
    print('Top 10 words of topic #{}'.format(k))
    print(mdl.get_topic_words(k, top_n=10))
    print('\n')

for word in data['words']:
    doc_inst = mdl.make_doc(words=word)
    topic_dist, ll = mdl.infer(doc_inst)
    print("Topic Distribution for Unseen Docs: ", topic_dist)
    vector = open('C:\\Users\\liuzhanyu\Desktop\\主题值.csv', 'a')
    vector.write(str(topic_dist))
    vector.write('\n')
    vector.close()
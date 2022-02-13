import xmnlp
import pandas as pd
xmnlp.set_model('C:\\Users\\liuzhanyu\\Desktop\\说服性策略\\技术\\xmnlp\\xmnlp-onnx-models-v3\\xmnlp-onnx-models')
train_path="C:\\Users\\liuzhanyu\Desktop\\说服性策略\\数据表格\\中文情感分析.csv"
data = pd.read_csv(train_path)
print(data[:2])
#在这可以嵌入一个中文文本预处理的过程#
text=data["introduction"]
b = [str(item) for item in text]
print(b)
list=list(xmnlp.sentiment_parallel(b))
print(list)
#这个库生成的是积极情绪和消极情绪的预测概率，可以按照0.6的标准对积极情绪和消极情绪进行判断#
column=['neg','pos']
test=pd.DataFrame(columns=column,data=list)

output = pd.DataFrame({
    "text":data["id"],
    "neg":test["neg"].values,
    "pos": test['pos'].values,
})

output.to_csv("C:\\Users\\liuzhanyu\Desktop\\简介情感分析.csv", index=False)

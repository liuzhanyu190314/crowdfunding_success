from cntext.stats import readability
import pandas as pd
#train_path="C:\\Users\\liuzhanyu\\Desktop\\众筹成功\\可读性.csv"
train_path="C:\\Users\\liuzhanyu\Desktop\\说服性策略\\数据表格\\中文情感分析.csv"
data = pd.read_csv(train_path)
print(data[:2])
#在这可以嵌入一个中文文本预处理的过程#
for text in data['introduction']:
    output=readability(text)
    vector = open('C:\\Users\\liuzhanyu\Desktop\\可读性.csv', 'a')
    vector.write(str(output['readability3']))
    vector.write('\n')
    vector.close()
output2=pd.read_csv('C:\\Users\\liuzhanyu\Desktop\\可读性.csv', header=None, names = ['readability3'] )
print(output2)
output3 = pd.DataFrame({
    "qid":data["id"].values,
    "readability3": output2['readability3']
})
print(output3[:5])
output3.to_csv("C:\\Users\\liuzhanyu\Desktop\\简介可读性分析.csv", index=False)


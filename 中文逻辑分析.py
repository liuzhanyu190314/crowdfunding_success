import xmnlp
import pandas as pd
from eventextraction import EventsExtraction
xmnlp.set_model('C:\\Users\\liuzhanyu\\Desktop\\说服性策略\\技术\\xmnlp\\xmnlp-onnx-models-v3\\xmnlp-onnx-models')
train_path="C:\\Users\\liuzhanyu\Desktop\\说服性策略\\数据表格\\中文情感分析.csv"
data = pd.read_csv(train_path)
print(data[:2])


#在这可以嵌入一个中文文本预处理的过程#
for text in data['text']:
    extractor = EventsExtraction()
    output=extractor.extract_main(text)
    output2=extractor.stats(output)
    #print(output2)
    vector = open('C:\\Users\\liuzhanyu\Desktop\\but.csv', 'a')
    vector.write(str(output2['but']))
    vector.write('\n')
    vector.close()
for text in data['text']:
    extractor = EventsExtraction()
    output=extractor.extract_main(text)
    output2=extractor.stats(output)
    #print(output2)
    vector = open('C:\\Users\\liuzhanyu\Desktop\\condition.csv', 'a')
    vector.write(str(output2['condition']))
    vector.write('\n')
    vector.close()
for text in data['text']:
    extractor = EventsExtraction()
    output=extractor.extract_main(text)
    output2=extractor.stats(output)
    #print(output2)
    vector = open('C:\\Users\\liuzhanyu\Desktop\\seq.csv', 'a')
    vector.write(str(output2['seq']))
    vector.write('\n')
    vector.close()
for text in data['text']:
    extractor = EventsExtraction()
    output=extractor.extract_main(text)
    output2=extractor.stats(output)
    #print(output2)
    vector = open('C:\\Users\\liuzhanyu\Desktop\\more.csv', 'a')
    vector.write(str(output2['more']))
    vector.write('\n')
    vector.close()
for text in data['text']:
    extractor = EventsExtraction()
    output=extractor.extract_main(text)
    output2=extractor.stats(output)
    #print(output2)
    vector = open('C:\\Users\\liuzhanyu\Desktop\\other.csv', 'a')
    vector.write(str(output2['other']))
    vector.write('\n')
    vector.close()
but=pd.read_csv('C:\\Users\\liuzhanyu\Desktop\\but.csv', header=None, names = ['but'] )
condition=pd.read_csv('C:\\Users\\liuzhanyu\Desktop\\condition.csv', header=None, names = ['condition'] )
seq=pd.read_csv('C:\\Users\\liuzhanyu\Desktop\\seq.csv', header=None, names = ['seq'] )
more=pd.read_csv('C:\\Users\\liuzhanyu\Desktop\\more.csv', header=None, names = ['more'] )
other=pd.read_csv('C:\\Users\\liuzhanyu\Desktop\\other.csv', header=None, names = ['other'] )
output3 = pd.DataFrame({
    "qid":data["id"].values,
    "but": but['but'],
    "condition": condition['condition'],
    "seq": seq['seq'],
    "more": more['more'],
    "other": other['other'],


})
print(output3[:5])
output3.to_csv("C:\\Users\\liuzhanyu\Desktop\\详细文本逻辑性分析.csv", index=False)
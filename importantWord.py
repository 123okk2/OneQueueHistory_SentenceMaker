#단어 빈도 계산기
import pandas as pd

sentence_text = open('trainData.txt', 'rb')
text = sentence_text.read().decode('utf-8')
text = text.split('\n')
text_list = []
for str in text :
    for strs in str.split() :
        text_list.append(strs)

word_list = pd.Series(text_list)
result = word_list.value_counts().head(7525)
result = result.keys().tolist()

f = open('keyWords.txt', 'w', -1, 'utf-8')
for i in range(1000) :
    f.write(result[i] + '\n')
f.close()


#print(result)
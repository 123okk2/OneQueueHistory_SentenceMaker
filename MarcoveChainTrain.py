import os, json, random

# 딕셔너리 제작
def make_dic(words):
    tmp = ["@"]
    dic = {}
    for word in words:
        tmp.append(word)
        if len(tmp) < 3: continue
        if len(tmp) > 3: tmp = tmp[1:]
        set_word3(dic, tmp)
        if word[-1] == ".":
            tmp = ["@"]
            continue
    return dic

# 딕셔너리에 데이터 등록
def set_word3(dic, s3):
    w1, w2, w3 = s3
    if not w1 in dic: dic[w1] = {}
    if not w2 in dic[w1]: dic[w1][w2] = {}
    if not w3 in dic[w1][w2]: dic[w1][w2][w3] = 0
    dic[w1][w2][w3] += 1


# 문장 읽어 들이기 --- (※4)
dict_file1 = "markov_history1.json"
dict_file2 = "markov_history2.json"

'''
if not os.path.exists(dict_file1):
    text = open('trainData.txt', 'rb').read().decode(encoding='utf-8')
    print(text)
    text = text.split('\n')
    words = []

    #한 단어씩 만들기
    for i in text :
        txt = i.split()
        for j in txt :
            words.append(j)
    print(words)

    # 딕셔너리 생성
    dic = make_dic(words)
    json.dump(dic, open(dict_file1, "w", encoding="utf-8"))
'''

if not os.path.exists(dict_file2) :
    text = open('trainData.txt', 'rb').read().decode(encoding='utf-8')
    print(text)
    text = text.split('\n')
    words = []

    # 두 단어씩 만들기 (하나씩 하면 정확도가 안나옴)
    for i in text:
        txt = i.split()
        k = 1
        saveWord = ''
        for j in txt:
            if j[-1] == '.' :
                if k == 1 : words.append(j)
                else : words.append(saveWord + ' ' + j)
            else :
                if k == 2:
                    words.append(saveWord + ' ' + j)
                    k = 1
                else:
                    saveWord = j
                    k = k + 1
    print(words)

    # 딕셔너리 생성
    dic = make_dic(words)
    json.dump(dic, open(dict_file2, "w", encoding="utf-8"))
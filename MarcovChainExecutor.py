import json
import random

# 문장 만들기 --- (※3)
def make_sentence(dic):
    def word_choice(sel):
        keys = sel.keys()
        return random.choice(list(keys))

    ret = []

    if not "@" in dic:
        return "no dic"

    top = dic["@"]
    w1 = word_choice(top)
    w2 = word_choice(top[w1])
    ret.append(w1)
    ret.append(w2)

    if w2[-1] == "." :
        ret = " ".join(ret)
        return ret

    while True:
        w3 = word_choice(dic[w1][w2])
        ret.append(w3)
        if w3[-1] == ".": break
        w1, w2 = w2, w3
    ret = " ".join(ret)

    # 리턴
    return ret

def Executor() :
    dict_file2 = "markov_history2.json"
    dic = json.load(open(dict_file2, "r"))
    arr = []

    f = open('sentences.txt', 'w', -1, 'utf-8')
    cnt = 0

    for i in range(10) :
        print(make_sentence(dic))

'''
    for i in range(100000) :
        str = make_sentence(dic)
        if(str not in arr) :
            cnt = cnt + 1
            print(cnt,end='')
            print("개 만들어짐")
            arr.append(str)
            f.write(str+'\n')
    f.close()
    '''

#print(Executor())
import json
import re
import os
def clean2(a,b,C):
    n=0
    #file = open(a, 'r', encoding='utf-8')
    #papers = []
    #for line in file.readlines():
        #dic = json.loads(line)
        #papers.append(dic)
    #f_out = open(b, "w", encoding="utf-8")

    #for i in papers:
        #for z in i.values():
            #if len(str(z))>=12:
                #f_out.write(str(z) + "\n")
    fp = open(b ,"r",encoding='utf-8')
    line = fp.readline()
    f_out = open(C, "w", encoding="utf-8")
    URL_REGEX = re.compile(
        r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))',
        re.IGNORECASE)
    while line:
        print(n)
        line = line.replace("。”","。”\n")
        line = re.sub(r'。*',"。\n",line)
        line = re.sub(URL_REGEX, "", line)
        line = re.sub(r'\（.*\）',"",line)
        line = line.strip()
        line = line.replace("<br>","")
        f_out.write(line + "\n")  
        line = fp.readline()
        n+=1
        

#clean2("C:/Users/User/Desktop/web_text_zh_valid.json","C:/Users/User/Desktop/a1.txt","C:/Users/User/Desktop/a8.txt")
#clean2("C:/Users/User/Desktop/baike_qa_valid.json","C:/Users/User/Desktop/a3.txt","C:/Users/User/Desktop/a10.txt")
#clean2("C:/Users/User/Desktop/web_text_zh_testa.json","C:/Users/User/Desktop/a5.txt","C:/Users/User/Desktop/a12.txt")
#clean2("C:/Users/User/Desktop/web_text_zh_train.json","C:/Users/User/Desktop/a6.txt","C:/Users/User/Desktop/a13.txt")
clean2("C:/Users/User/Desktop/news2016zh_train.json","C:/Users/User/Desktop/a111.txt","C:/Users/User/Desktop/a355.txt")
#clean2("C:/Users/User/Desktop/baike_qa_train.json","C:/Users/User/Desktop/a2.txt","C:/Users/User/Desktop/a9.txt")
#clean2("C:/Users/User/Desktop/news2016zh_valid.json","C:/Users/User/Desktop/a4.txt","C:/Users/User/Desktop/a11.txt")
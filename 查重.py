import re
import shutil
def clean1(inp , outp,cd):
    a=set()
    fp = open(inp ,"r",encoding='utf-8')
    zp = open(cd ,"r",encoding='utf-8')
    f_out = open(outp, "w", encoding="utf-8")
    for line in zp:
        a.add(line.strip())
    for i in fp:
        b=0
        for z in a:
            if z in i :
                b+=1
        if b>=10:
            i=i.strip()
            f_out.write(i + "\n")
clean1("C:/Users/User/Desktop/weibo_clean1.txt","C:/Users/User/Desktop/詞典句子2.txt","C:/Users/User/Desktop/詞典.txt")

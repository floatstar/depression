import re
import shutil
def clean(inp , outp):
    fp = open(inp ,"r",encoding='utf-8')
    line = fp.readline()
    f_out = open(outp, "w", encoding="utf-8")
    URL_REGEX = re.compile(
        r'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))',
        re.IGNORECASE)
    while line:
        line = line.strip()
        line = re.sub(r"(回复)?(//)?\s*@\S*?\s*(:| |$)", " ", line)  # 去除正文中的@和回复/转发中的用户名
        line = re.sub(r"\[\S+\]", "", line)      # 去除表情符号
        line = re.sub(r"#\S+#", "", line)      # 保留话题内容
        line = re.sub(URL_REGEX, "", line)       # 去除网址
        line = re.sub(r"\s+", " ", line) # 合并正文中过多的空格
        line = line.strip()
        line = re.sub(r"【.*】", "", line)
        line = line.replace('该账号行为异常，存在安全风险，用户验证之前暂时不能查看。查看帮助', '')
        line = line.replace('该账号因被投诉违反《微博社区公约》的相关规定，现已无法查看。查看帮助', '')
        line = line.replace('该账号已关闭，现无法查看。', '')
        line = line.replace('该账号因被投诉违反法律法规和《微博社区公约》的相关规定，现已无法查看。查看帮助 ', '')
        line = line.replace('（分享自', '')   
        line = line.replace('http://', '')
        line = line.replace('发表了博文', '')
        line = line.replace('- 原文地址：', '')
        line = line.replace('//', '')
        line = line.replace('发表了一篇转载博文', '')
        line = line.replace('【喂 .....(☆▽☆)', '')
        line = line.replace('★', '')
        line = line.replace('【】', '')
        line = line.replace('抱歉，作者已设置仅展示半年内微博，此微博已不可见。', '')
        line = line.replace('抱歉，由于作者设置，你暂时没有这条微博的查看权限哦。查看帮助', '')
        line = re.sub(r".*转发理由:", "", line) 
        line = line.strip()
        line = re.sub(r"【\S+】", "", line)
        line = re.sub(r"转发微博.*", "", line) 
        line = line.strip()
        line = line.replace('转发', '')
        line = line.strip()
        line = line.strip()
        line = line.strip()
        f_out.write(line + "\n")
        line = fp.readline()
clean("C:/Users/User/Desktop/a7.txt","C:/Users/User/Desktop/a8.txt")

def check(readDir,writeDir):
    a=0
    lines_seen = set()
    outfile = open(writeDir, "w", encoding='utf8')
    f = open(readDir, "r", encoding='utf8')
    for line in f:
        if line not in lines_seen:
            a+=1
            outfile.write(line)
            lines_seen.add(line)
            print(a)
    outfile.close()
    print("success")
#check("C:/Users/User/Desktop/a7.txt","C:/Users/User/Desktop/a8.txt")

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
#clean1("C:/Users/User/Desktop/weibo_clean1.txt","C:/Users/User/Desktop/詞典句子2.txt","C:/Users/User/Desktop/詞典.txt")

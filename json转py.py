

import json

data = []
with open('C:/Users/User/Desktop/data/json/baike_qa_valid.json',"r",encoding='utf-8') as f:
    for line in f:
        data.append(json.loads(line))

#print json.dumps(data, ensure_ascii=False)


import codecs
file_object = codecs.open('C:/Users/User/Desktop/aaa.txt', 'w' ,"utf-8")
str = "\r\n"
splitstr = "#_#"
for item in data:
    #print json.dumps(item)
    #str = str + "insert into tencent(name,catalog,workLocation,recruitNumber,detailLink,publishTime) values "
    #str = str + "'%s','%s','%s','%s','%s'\r\n" % (item['parentTitle'],item['parentLink'],item['author'],item['link'],item['title'])
    #print json.loads(item['author']) + "\r\n"
    str = "%s#_#%s#_#%s#_#%s#_#%s\r\n" % (item['parentTitle'],item['parentLink'],item['author'],item['link'],item['title'].strip())
    file_object.write(str)

#import codecs
#file_object = codecs.open('tencent.txt', 'w' ,"utf-8")
#file_object.write(str)
file_object.close()
print("success")
 

import sys

def findspace(string):
        count =0
        search = ' '
        count = string.find(search)
        return count
def findenter(string):
        indexNo =-1
        search = "\n"
        indexNo = string.find(search)
        return indexNo
        
line = ''
tmp = ''
index2 = -1
line2= ''
f= open('sample.md','r',encoding='UTF-8')
for line in f:
        index = findspace(line)
        index2 = findenter(line)
        tmp += line[:index+1]
        line2 = line[index+1:index2]
        line2 = line2[::-1]
        tmp += line2
        tmp += line[index2:]
print(tmp)
f.close()
d = open('result.md','w',encoding='UTF-8')
d.write(tmp)
d.close()


        

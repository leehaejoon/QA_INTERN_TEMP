import sys

i=1

line = ''
tmp = ''
f= open('sample.md','r',encoding='UTF-8')
for line in f:
        line = line[::-1]
        tmp += line
        i+=1
        print(line)
f.close()
d = open('result.md','w',encoding='UTF-8')
d.write(tmp)
        
d.close()




import sys

i=1
line =''
f= open('sample.md','r',encoding='UTF-8')
while i <5:
	line += f.readline()
	i+=1
line = line[::-1]
f.close()
print(line)
d = open('result.md','w',encoding='UTF-8')
d.write(line)
        
d.close()




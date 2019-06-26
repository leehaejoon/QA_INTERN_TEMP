import sys
import re
 
in_path = "../../data/sample.md"
out_path = "../../data/result_go_2.md"

in_file = open(in_path, 'r',encoding = 'UTF-8')
out_file = open(out_path, 'w',encoding = 'UTF-8')

p = re.compile('\w+')

with in_file,out_file:
    for line in in_file:
        revers_string = ' '.join(p.findall(line))[::-1]
        out_file.write('#'*line.count('#') +' '+ revers_string+'\n')
    



        

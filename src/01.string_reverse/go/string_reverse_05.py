import sys
import re

def read_file(path):
    tmp = ''
    with open(path,'r',encoding= 'UTF-8') as f:
        for line in f:
            tmp += line
    return tmp

def line_reverse(string):
    p = re.compile('\w+')
    reverse_list = string.split('\n')
    for i in range(len(reverse_list)):
        tmp_list = p.findall(reverse_list[i])
        tmp = " ".join(tmp_list)
        reverse_list[i] = '#'*reverse_list[i].count('#')+' '*bool(reverse_list[i].count('#'))+tmp[::-1]+'\n'*reverse_list[i].count('\n')
    return reverse_list

def write_file(path,out_list):
    with open(path, 'w', encoding='UTF-8') as f:
        f.write("\n".join(out_list))

if __name__ == "__main__":
    in_path = "../../../../../../data/sample.md"
    out_path = "../../../../../../data/result_go_4.md"


    line = read_file(in_path)
    tmp = line_reverse(line)
    write_file(out_path,tmp)

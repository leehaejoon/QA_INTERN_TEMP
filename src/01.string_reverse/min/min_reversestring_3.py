import re

src_path = "sample.md"
re_path = "result_min_3.md"

src_file = open(src_path, "r", encoding='UTF-8')
re_file = open(re_path,'w', encoding='UTF-8')
s=re.compile("\w+")

with src_file, re_file:
    for line in src_file:
        only_list = s.findall(line)
        only_string = " ".join(only_list)
        re_string = only_string[::-1]
        output=line.replace(only_string, re_string)
        print(output)
        re_file.write(output)

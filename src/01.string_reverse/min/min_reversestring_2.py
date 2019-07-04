import re

src_path = "sample.md"
re_path = "result_min_2.md"

src_file = open(src_path, "r", encoding='UTF-8')
re_file = open(re_path, 'w', encoding='UTF-8')

with src_file, re_file:
    for line in src_file:
        left=line.find('#')
        num = line.count('#')
        right=len(line)
        if left > -1:
            size = line[left:num]
            reline = line[num-left:right-1]
            reline = reline[::-1]
            output = size + ' ' + reline.strip('\n')
            print(output)
            re_file.write(output+'\n')
        else:
            print("\n")
            re_file.write('\n')

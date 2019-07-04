import re

in_path = "../../data/sample.md"
out_path = "../../data/result_lee.md"

in_file = open(in_path, 'r')
out_file = open(out_path, 'w')
p = re.compile("\w+")

with in_file, out_file:
    for line in in_file:
        only_string_list = p.findall(line)
        origin_string = " ".join(only_string_list)
        reverse_origin_string = origin_string[::-1]
        out_file.write(line.replace(origin_string, reverse_origin_string))

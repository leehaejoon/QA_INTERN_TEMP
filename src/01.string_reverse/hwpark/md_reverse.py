import re

def read_file(file_name):
    with open(file_name, 'r') as f:
        _line = f.readline()
        line_list = [_line]
        while _line:
            _line = f.readline()
            line_list.append(_line)
    return line_list

def line_reverse(line_list):
    pattern = re.compile("\w+")
    reverse_line_list = []
    for line in line_list:
        if len(line) > 1:
            pure_str_list = pattern.findall(line)
            pure_str = " ".join(pure_str_list)
            reversed_str = pure_str[::-1]
            reverse_line_list.append(line.replace(pure_str, reversed_str))
    return reverse_line_list

def file_write(file_name, reverse_list):
    with open(file_name, 'w') as f:
        f.write("\n".join(reverse_list))

if __name__ == "__main__":
    input_file_name = "../../data/sample.md"
    output_file_name = "../../data/result_hwpark.md"

    # 파일을 읽어서 라인 리스트 반환
    line_list = read_file(input_file_name)

    # 라인 리스트 reverse후 reverse 리스트 반환
    reverse_list = line_reverse(line_list)

    # 결과 파일 write
    file_write(output_file_name, reverse_list)

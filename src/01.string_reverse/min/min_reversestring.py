file = open('sample.md', "r", encoding='UTF-8')  # 'file'의 경우 python2 에서는 내장함수이므로 변수로 사용을 지양
f = open('result_min.md', 'w', encoding='UTF-8')
for line in file:
    num = line.count('#')
    size = line[0:num]
    line = line[2:]
    reline = line[::-1]
    output = size + ' ' + reline.strip('\n')
    print(output)
    f.write(output + '\n')
file.close()
f.close()

in_path = "../../data/sample.md"
out_path = "../../data/result_lee.md"

in_file = open(in_path, 'r')
out_file = open(out_path, 'w')

def rebuild_out_data(out_data):
    return '#' * out_data.count('#') + ' ' + out_data.replace('#', '')

with in_file, out_file:
    for line in in_file:
        out_file.write(rebuild_out_data(line[::-1].lstrip()) + '\n')

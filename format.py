import math


def format(path, output):
    with open(path, 'r') as f:
        res = f.readlines()
    first = True
    each = []
    total = []
    with open(output, 'a+') as file:
        for line in res:
            line = line[:-1]
            if line.endswith('.jpg'):
                if first:
                    first = False
                else:
                    total.append(each[:])
                    each.clear()
                each.append(line)
            else:
                each.append(line)
        total.append(each[:])
        total.sort(key=lambda item:item[0])
        for item in total:
            for data in item[1:]:
                data = [eval(x) for x in data.split(' ')]
                data[2] += data[0]
                data[3] += data[1]
                if(data[-1] >= 0.4):
                    s = item[0] + ','
                    s += ','.join([str(math.ceil(x)) for x in data[:-1]])
                    # s += '    ' + data[-1]
                    file.write(s + '\n')




format('./res.txt', './format.txt')
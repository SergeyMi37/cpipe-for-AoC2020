with open("../in/input15.txt", "r") as file:
    data = [int(y) for y in [x.strip() for x in file.read().splitlines()][0].split(',')]
    occurences = {data[i-1]:[i] for i in range(1, len(data)+1)}
    current = data[-1]
    for i in range(len(data)+1,30000001):
        if len(occurences[current]) == 1:
            current = 0
            if len(occurences[0]) == 2:
                occurences[0].remove(occurences[0][0])
            occurences[0].append(i)
        else:
            new = occurences[current][1] - occurences[current][0]
            if new in occurences:
                if len(occurences[new]) == 2:
                    occurences[new].remove(occurences[new][0])
                occurences[new].append(i)
            else:
                occurences[new] = [i]
            current = new
        if i == 2020:
            print('Part 1: {}'.format(current))
    print('Part 2: {}'.format(current))
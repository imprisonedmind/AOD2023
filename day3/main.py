import re


def problem1():
    with open('sample.bin', 'r') as file:
        prev_line = []
        part_total = 0
        for line in file:
            print("----------------")
            number_pos = matchpattern(r'[0-9]', line.strip())
            symbols = matchpattern(r'[^.^[0-9]', line.strip())
            line_arr = []

            if len(number_pos) > 0:
                for num in number_pos:
                    if len(prev_line) > 0:
                        prev0 = prev_line[num[0]]
                        prev1 = prev_line[num[0] - 1]
                        prev2 = prev_line[num[0] + 1]
                        prev_arr = [prev0, prev1, prev2]
                        for item in prev_arr:
                            if "." not in item:
                                full_number = int(findfullnumber(line, num[0]))
                                if full_number not in line_arr:
                                    line_arr.append(full_number)
                                    print(line_arr)

            for symbol in symbols:
                prev0 = prev_line[symbol[0]]
                prev1 = prev_line[symbol[0] - 1]
                prev2 = prev_line[symbol[0] + 1]
                prev_arr = [prev0, prev1, prev2]
                for i, value in enumerate(prev_arr):
                    if "." not in value:
                        s = symbol[0]
                        position = s if i < 1 else s - 1 if i < 2 else s + 1
                        full_number = int(findfullnumber(prev_line, position))
                        if full_number not in line_arr:
                            line_arr.append(full_number)
                            print(line_arr)

            part_total += sum(line_arr)
            print("line part number", sum(line_arr), line_arr)
            prev_line = line
        print("Part total:", part_total)


def matchpattern(pattern, data):
    return [(match.start(), match.group()) for match in
            re.finditer(pattern, data.strip())]


def findfullnumber(data, pos):
    start = pos
    while start >= 0 and data[start].isdigit():
        start -= 1

    end = pos + 1
    while end < len(data) and data[end].isdigit():
        end += 1

    adjacent_digits = data[start + 1:end]
    return adjacent_digits


if __name__ == '__main__':
    problem1()

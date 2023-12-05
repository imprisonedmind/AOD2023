import re


def problem1():
    with open('sample.txt', 'r') as file:
        prev_line = []
        part_total = 0
        for line in file:
            print("----------------")
            number_pos = matchpattern(r'[0-9]', line.strip())
            symbols = matchpattern(r'[^.^[0-9]', line.strip())
            full_number = 0
            part_number = 0

            if len(number_pos) > 0:
                for num in number_pos:
                    if len(prev_line) > 0:
                        prev0 = prev_line[num[0]]
                        prev1 = prev_line[num[0] - 1]
                        prev2 = prev_line[num[0] + 1]
                        fn = findfullnumber(line, num[0])
                        full_number = fn if full_number != fn else None
                        if "." not in prev0 and full_number is not None:
                            part_number += int(full_number)
                            print(full_number)
                        if "." not in prev1 and full_number is not None:
                            part_number += int(full_number)
                            print(full_number)
                        if "." not in prev2 and full_number is not None:
                            part_number += int(full_number)
                            print(full_number)

            if len(symbols) > 0:
                for symbol in symbols:
                    prev0 = prev_line[symbol[0]]
                    prev1 = prev_line[symbol[0] - 1]
                    prev2 = prev_line[symbol[0] + 1]
                    sybl_full_number = 0
                    if "." not in prev0 and sybl_full_number is not None:
                        zero_fn = findfullnumber(prev_line, symbol[0])
                        sybl_full_number = zero_fn if sybl_full_number != zero_fn else 0
                        part_number += int(sybl_full_number)
                        print(sybl_full_number)
                    if "." not in prev1 and sybl_full_number is not None:
                        one_fn = findfullnumber(prev_line, symbol[0] - 1)
                        sybl_full_number = one_fn if sybl_full_number != one_fn else 0
                        part_number += int(sybl_full_number)
                        print(sybl_full_number)
                    if "." not in prev2 and sybl_full_number is not None:
                        two_fn = findfullnumber(prev_line, symbol[0] + 1)
                        sybl_full_number = two_fn if sybl_full_number != two_fn else 0
                        part_number += int(sybl_full_number)
                        print(sybl_full_number)

            part_total += part_number
            print("line part number", part_number)
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

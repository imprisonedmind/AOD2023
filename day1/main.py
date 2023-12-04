# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def problem1():
    with open('data.txt', 'r') as file:
        total = 0
        for line in file:
            result = ''.join(char for char in line if char.isdigit())
            chars_array = [char for char in result]
            chars_sum = f"{chars_array[0]}{chars_array[-1]}"
            total += int(chars_sum)
    print(f"total={total}")


# Problem 2
STRINGS = {
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
}

STRINGS_TO_INTS = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def problem2():
    with open('data.txt', 'r') as file:
        total = 0
        for line in file:
            first_last = ''
            value_arr = []

            for string in STRINGS:
                len_substring = len(string)
                for i in range(len(line)):
                    if line[i:i + len_substring] == string:
                        value_arr.append((i, string))
                sorted_arr = sorted(value_arr, key=lambda x: x[0])
                first_value_arr = [tup[1] for tup in sorted_arr]
                for value in enumerate(first_value_arr):
                    new_value = STRINGS_TO_INTS.get(value[1])
                    if new_value is not None:
                        first_value_arr[value[0]] = new_value
                    if len(first_value_arr) > 0:
                        first_last = f"{first_value_arr[0]}{first_value_arr[-1]}"
            total += int(first_last)

    print(f"total={total}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    problem2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

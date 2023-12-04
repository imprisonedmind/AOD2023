import re


def problem1():
    with open('data.txt', 'r') as file:
        total_possible = 0
        for line in file:
            data_arr = re.split("[;:]", line.strip())
            id = int(''.join(filter(str.isdigit, data_arr[0])))
            possible = False
            for item in data_arr:
                blue = 0
                red = 0
                green = 0
                item = item.split(",")
                for string in item:
                    val = int(''.join(filter(str.isdigit, string)))
                    if "blue" in string:
                        blue += val
                    if "red" in string:
                        red += val
                    if "green" in string:
                        green += val
                enough_balls = 14 >= blue > 0 and 12 >= red > 0 and 13 >= green > 0
                total_score = blue + red + green
                possible = enough_balls and 39 >= total_score > 0
            if possible:
                total_possible += id
                print(f"ID:{id}", blue, red, green, f"S:{total_score}", f"P:{possible}")
    print(f"Total Possible: {total_possible}")


if __name__ == '__main__':
    problem1()

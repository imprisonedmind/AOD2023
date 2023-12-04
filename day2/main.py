import re


def problem1():
    with open('data.txt', 'r') as file:
        total_possible = 0
        for game in file:
            data_arr = re.split("[;:]", game.strip())
            id = int(''.join(filter(str.isdigit, data_arr[0])))
            blue = 0
            red = 0
            green = 0
            for game_set in data_arr:
                game_set = game_set.split(",")
                for string in game_set:
                    val = int(''.join(filter(str.isdigit, string)))
                    if "blue" in string:
                        blue = val if val > blue else blue
                    if "red" in string:
                        red = val if val > red else red
                    if "green" in string:
                        green = val if val > green else green
            possible = 14 >= blue > 0 and 12 >= red > 0 and 13 >= green > 0
            if possible:
                total_possible += id
            print(f"ID:{id}", blue, red, green, f"P:{possible}")
    print(f"Total Possible: {total_possible}")


if __name__ == '__main__':
    problem1()

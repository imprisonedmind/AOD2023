def problem1():
    with open('data.txt', 'r') as file:
        total = 0
        for line in file:
            print(line)


if __name__ == '__main__':
    problem1()
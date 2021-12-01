def count_increases(filename: str, window: int=1) -> int:
    count = 0
    temp = [float("inf")]*window
    with open(filename) as file:
        for index, line in enumerate(file):
            value = int(line)
            if value > temp[index % window]:
                count += 1
            temp[index % window] = value
    return count

if __name__ == '__main__':
    print(count_increases("day01/input.txt"))
    print(count_increases("day01/input.txt", 3))

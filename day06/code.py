def num_lanternfish(filename: str, days: int) -> int:
    initial = [0] * 9
    with open(filename) as file:
        for timer in file.readline().split(","):
            initial[int(timer)] += 1
    for day in range(days):
        initial[(day+7)%9] += initial[day%9]
    return sum(initial)


if __name__ == '__main__':
    print(num_lanternfish("day06/input.txt", 80))
    print(num_lanternfish("day06/input.txt", 256))
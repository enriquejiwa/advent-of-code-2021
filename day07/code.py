import statistics
import math

def min_fuel_usage_median(filename: str) -> int:
    with open(filename) as file:
        values = [int(x) for x in file.readline().split(",")]
    median = math.floor(statistics.median(values))
    return sum(abs(value - median) for value in values)


def min_fuel_usage_mean(filename: str) -> int:
    with open(filename) as file:
        values = [int(x) for x in file.readline().split(",")]
    mean = math.floor(statistics.mean(values))
    return sum(abs(value - mean) * (abs(value - mean) + 1) // 2 for value in values)


if __name__ == '__main__':
    print(min_fuel_usage_median("day07/input.txt"))
    print(min_fuel_usage_mean("day07/input.txt"))

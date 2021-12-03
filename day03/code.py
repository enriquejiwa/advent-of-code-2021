def get_power_consumption(filename: str) -> int:
    count = 0
    number_of_ones = [0] * 12
    with open(filename) as file:
        for line in file:
            count += 1
            value = int(line, 2)
            for i in range(12):
                number_of_ones[-i-1] += bool(value & 2 ** i)
    gamma = 0
    for bit in number_of_ones:
        gamma = (gamma << 1) | (bit > count / 2)
    epsilon = gamma ^ 0xFFF
    return gamma * epsilon

def get_life_support_rating(filename: str) -> int:
    count = 0
    with open(filename) as file:
        lines = [int(line, 2) for line in file]
    for i in range(11, -1, -1):
        zeros = []
        ones = []
        for value in lines:
            if value & 2 ** i:
                ones.append(value)
            else:
                zeros.append(value)
            if len(ones) > len(zeros):
                lines = ones
            elif len(ones) < len(zeros):
                lines = zeros
        if len(lines) == 1:
            oxygen = lines[0]
    with open(filename) as file:
        lines = [int(line, 2) for line in file]
    for i in range(11, -1, -1):
        zeros = []
        ones = []
        for value in lines:
            if value & 2 ** i:
                ones.append(value)
            else:
                zeros.append(value)
            if len(ones) < len(zeros):
                lines = ones
            elif len(ones) > len(zeros):
                lines = zeros
        if len(lines) == 1:
            co2 = lines[0]
    return oxygen * co2


if __name__ == '__main__':
    print(get_power_consumption("day03/input.txt"))
    print(get_life_support_rating("day03/input.txt"))

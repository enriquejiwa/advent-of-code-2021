def read_movements(filename: str) -> tuple[int, int]:
    horizontal = 0
    depth = 0
    with open(filename) as file:
        for line in file:
            action, value = line.split()
            value = int(value)
            if action == "forward":
                horizontal += value
            elif action == "down":
                depth += value
            else:
                depth -= value
    return horizontal, depth

def read_movements_aim(filename: str) -> tuple[int, int]:
    horizontal = 0
    depth = 0
    aim = 0
    with open(filename) as file:
        for line in file:
            action, value = line.split()
            value = int(value)
            if action == "forward":
                horizontal += value
                depth += aim * value
            elif action == "down":
                aim += value
            else:
                aim -= value
    return horizontal, depth

if __name__ == '__main__':
    h, d = read_movements("day02/input.txt")
    print(h, d)
    print(h * d)
    h, d = read_movements_aim("day02/input.txt")
    print(h, d)
    print(h * d)
from collections import defaultdict


def count_overlap(filename: str, diagonal: bool=False) -> int:
    count = 0
    floor = defaultdict(int)
    with open(filename) as file:
        for line in file:
            temp1, temp2 = line.split(" -> ")
            x1, y1 = temp1.split(",")
            x2, y2 = temp2.split(",")
            x1, y1 = int(x1), int(y1)
            x2, y2 = int(x2), int(y2)
            if x1 == x2:
                for j in range(min(y1, y2), max(y1, y2) + 1):
                    floor[(x1, j)] += 1
                    if floor[(x1, j)] == 2:
                        count += 1
            elif y1 == y2:
                for i in range(min(x1, x2), max(x1, x2) + 1):
                    floor[(i, y1)] += 1
                    if floor[(i, y1)] == 2:
                        count += 1
            elif diagonal and abs(x2 - x1) == abs(y2 - y1):
                x_mod = y_mod = -1
                if x2 > x1:
                    x_mod = 1
                if y2 > y1:
                    y_mod = 1
                for step in range(abs(x2 - x1) + 1):
                    floor[(x1 + step * x_mod, y1 + step * y_mod)] += 1
                    if floor[(x1 + step * x_mod, y1 + step * y_mod)] == 2:
                        count += 1
    return count


if __name__ == '__main__':
    print(count_overlap("day05/input.txt"))
    print(count_overlap("day05/input.txt", diagonal=True))

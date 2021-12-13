def get_num_dots(filename: str) -> int:
    points = set()
    next_section = False
    folds = []
    one_fold = 0
    with open(filename) as file:
        for line in file:
            if next_section:
                axis, value = line.strip("fold along\n").split("=")
                folds.append((axis, int(value)))
            elif line == "\n":
                next_section = True
            else:
                points.add(tuple(int(x) for x in line.strip().split(",")))
    for fold in folds:
        if fold[0] == "x":
            points = {(fold[1] - abs(x - fold[1]), y) for (x, y) in points}
        else:
            points = {(x, fold[1] - abs(y - fold[1])) for (x, y) in points}
        if not one_fold:
            one_fold = len(points)
    for i in range(6):
        for j in range(40):
            print("█" if (j, i) in points else " ", end="")
        print()
    return one_fold


if __name__ == "__main__":
    print(get_num_dots("day13/input.txt"))

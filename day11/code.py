def get_num_flashes(filename: str) -> int:
    matrix = []
    count = 0
    finished = False
    step = 0
    with open(filename) as file:
        for line in file:
            matrix.append([int(x) for x in line.strip()])
    while not finished:
        num_flashed = process_flashes(matrix)
        count += num_flashed if step < 100 else 0
        if num_flashed == len(matrix) * len(matrix[0]):
            finished = True
        step += 1
    return count, step


def process_flashes(matrix):
    flashed = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            expand_flashes(matrix, i, j, flashed)
    for i, j in flashed:
        matrix[i][j] = 0
    return len(flashed)


DIRECTIONS = [(1, 1), (1, 0), (1, -1), (0, 1),
              (0, -1), (-1, 1), (-1, 0), (-1, -1)]


def expand_flashes(matrix, i, j, flashed):
    if (i, j) in flashed:
        return
    matrix[i][j] += 1
    if matrix[i][j] > 9:
        flashed.add((i, j))
        for offset in DIRECTIONS:
            next_i = i + offset[0]
            next_j = j + offset[1]
            if 0 <= next_i < len(matrix) and 0 <= next_j < len(matrix[next_i]):
                expand_flashes(matrix, next_i, next_j, flashed)


if __name__ == '__main__':
    print(get_num_flashes("day11/input.txt"))

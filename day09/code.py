def get_risk_basin(filename: str):
    matrix = []
    basins_size = []
    risk = 0
    with open(filename) as file:
        for line in file:
            matrix.append([int(x) for x in line.strip()])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if chech_low_point(matrix, i, j):
                risk += matrix[i][j] + 1
                basins_size.append(expand_basin(matrix, i, j, set()))
    basins_size.sort()
    sol = basins_size[-1] * basins_size[-2] * basins_size[-3]
    return risk, sol


DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def chech_low_point(matrix, i, j) -> bool:
    for offset in DIRECTIONS:
        new_i = i + offset[0]
        new_j = j + offset[1]
        if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]):
            if matrix[new_i][new_j] <= matrix[i][j]:
                return False
    return True


def expand_basin(matrix, i, j, visited) -> int:
    count = 0
    if (i, j) in visited:
        return count
    if matrix[i][j] == 9:
        return count
    visited.add((i, j))
    for offset in DIRECTIONS:
        new_i = i + offset[0]
        new_j = j + offset[1]
        if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]):
            count += expand_basin(matrix, new_i, new_j, visited)
    return count + 1


if __name__ == '__main__':
    print(get_risk_basin("day09/input.txt"))

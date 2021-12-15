import heapq


def lowest_risk(filename: str) -> int:
    array = []
    with open(filename) as file:
        for line in file:
            array.append([int(x) for x in line.strip()])
    return bfs_cost(array), bfs_cost2(array)


DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs_cost(array):
    n, m = len(array), len(array[0])
    border = []
    visited = dict()

    heapq.heappush(border, (0, (0, 0)))
    visited[(0, 0)] = 0
    while border:
        cost, coord = heapq.heappop(border)
        if coord == (n-1, m-1):
            return cost
        for offset in DIRECTIONS:
            next_x = coord[0] + offset[0]
            next_y = coord[1] + offset[1]
            if 0 <= next_x < n and 0 <= next_y < m:
                next_cost = cost + array[next_x][next_y]
                if (next_x, next_y) not in visited or \
                        next_cost < visited[(next_x, next_y)]:
                    visited[(next_x, next_y)] = next_cost
                    heapq.heappush(border, (next_cost, (next_x, next_y)))
    return -1


def bfs_cost2(array):
    n, m = len(array), len(array[0])
    border = []
    visited = dict()

    heapq.heappush(border, (0, (0, 0)))
    visited[(0, 0)] = 0
    while border:
        cost, coord = heapq.heappop(border)
        if coord == (5*n-1, 5*m-1):
            return cost
        for offset in DIRECTIONS:
            next_x = coord[0] + offset[0]
            next_y = coord[1] + offset[1]
            if 0 <= next_x < 5*n and 0 <= next_y < 5*m:
                extra = next_x // n + next_y // n
                next_cost = cost + (array[next_x % n][next_y % n] + extra) % 10 + (
                    array[next_x % n][next_y % n] + extra) // 10
                if (next_x, next_y) not in visited or \
                        next_cost < visited[(next_x, next_y)]:
                    visited[(next_x, next_y)] = next_cost
                    heapq.heappush(border, (next_cost, (next_x, next_y)))
    return -1


if __name__ == "__main__":
    print(lowest_risk("day15/input.txt"))

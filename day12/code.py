from collections import defaultdict


def get_num_paths(filename: str) -> int:
    connections = defaultdict(list)
    with open(filename) as file:
        for line in file:
            origin, destination = line.strip().split("-")
            connections[origin].append(destination)
            connections[destination].append(origin)
    return dfs(connections, "start", ["start"]), \
        dfs_twice(connections, "start", ["start"], False)


def dfs(connections, node, path):
    if node == "end":
        return 1
    count = 0
    for dest in connections[node]:
        if dest.isupper() or dest not in path:
            count += dfs(connections, dest, path+[dest])
    return count


def dfs_twice(connections, node, path, twice):
    if node == "end":
        return 1
    count = 0
    for dest in connections[node]:
        if dest.islower() and dest in path:
            if not twice and dest != "start":
                count += dfs_twice(connections, dest, path+[dest], True)
        else:
            count += dfs_twice(connections, dest, path+[dest], twice)
    return count


if __name__ == '__main__':
    print(get_num_paths("day12/input.txt"))

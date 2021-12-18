import math

def get_magnitude(filename: str) -> int:
    pairs = []
    with open(filename) as file:
        for line in file:
            temp = eval(line.strip())
            pairs = add(pairs, temp)
    return magnitude(pairs)

def max_magnitude(filename: str) -> int:
    pairs = []
    sol = 0
    with open(filename) as file:
        pairs = [eval(line.strip()) for line in file]
    for i in range(len(pairs)):
        for j in range(len(pairs)):
            if i != j:
                sol = max(sol, magnitude(add(pairs[i], pairs[j])))
    return sol

def add(op1, op2):
    if not op1:
        return op2
    pair = [op1, op2]
    finished = False
    while not finished:
        exploded, pair, _, _ = explode(pair)
        if not exploded:
            action, pair = split(pair)
            if not action:
                finished = True
    return pair

def explode(pair, depth: int=0):
    if isinstance(pair, int):
        return False, pair, 0, 0
    if depth == 4:
        return True, 0, pair[0], pair[1]
    a, b = pair
    exploded, a, left, right = explode(a, depth+1)
    if exploded:
        return True, [a, add_left(b, right)], left, 0
    exploded, b, left, right = explode(b, depth+1)
    if exploded:
        return True, [add_right(a, left), b], 0, right
    return False, pair, 0, 0

def add_left(pair, value):
    if isinstance(pair, int):
        return pair + value
    return [add_left(pair[0], value), pair[1]]

def add_right(pair, value):
    if isinstance(pair, int):
        return pair + value
    return [pair[0], add_right(pair[1], value)]

def split(pair):
    if isinstance(pair, int):
        if pair > 9:
            return True, [math.floor(pair/2), math.ceil(pair/2)] 
        return False, pair
    a, b = pair
    action, a = split(a)
    if action:
        return True, [a, b]
    action, b = split(b)
    if action:
        return True, [a, b]
    return False, pair

def magnitude(pair):
    if isinstance(pair, int):
        return pair
    return 3 * magnitude(pair[0]) + 2 * magnitude(pair[1])

if __name__ == "__main__":
    print(get_magnitude("day18/input.txt"))
    print(max_magnitude("day18/input.txt"))

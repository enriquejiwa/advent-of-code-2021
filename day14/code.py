from collections import Counter

def polymerization(filename: str, iterations: int) -> int:
    template = ""
    rules = dict()
    with open(filename) as file:
        for line in file:
            if not template:
                template = line.strip()
                next(file)
            else:
                pair, insert = line.strip().split(" -> ")
                rules[pair] = insert
    pairs = Counter()
    for i in range(len(template) - 1):
        pairs[template[i:i+2]] += 1
    count = Counter(template)
    for i in range(iterations):
        temp = Counter()
        for pair, rep in pairs.items():
            insert = rules[pair]
            temp[pair[0]+insert] += rep
            temp[insert+pair[1]] += rep
            count[insert] += rep
        pairs = temp
    ordered_count = count.most_common()
    return ordered_count[0][1] - ordered_count[-1][1]


if __name__ == "__main__":
    print(polymerization("day14/input.txt", 40))

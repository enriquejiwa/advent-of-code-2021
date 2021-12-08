def num_unique_digits(filename: str) -> int:
    unique_segments = (2, 3, 4, 7)
    count = 0
    with open(filename) as file:
        for line in file:
            _, output = line.split("|")
            for digit in output.split():
                if len(digit) in unique_segments:
                    count += 1
    return count


def sum_decoded_output(filename: str) -> int:
    unique_segments = {2: 1, 3: 7, 4: 4, 7: 8}
    count = 0
    with open(filename) as file:
        for line in file:
            decoder = dict()
            number = 0
            info, output = line.split("|")
            for digit in info.split():
                if len(digit) in unique_segments:
                    decoder[unique_segments[len(digit)]] = set(digit)
            for digit in [set(x) for x in output.split()]:
                if len(digit) == 2:
                    value = 1
                elif len(digit) == 3:
                    value = 7
                elif len(digit) == 4:
                    value = 4
                elif len(digit) == 7:
                    value = 8
                elif len(digit) == 5:
                    if len(digit & decoder[1]) == 2:
                        value = 3
                    elif len(digit & decoder[4]) == 2:
                        value = 2
                    else:
                        value = 5
                else:
                    if len(digit & decoder[1]) == 1:
                        value = 6
                    elif len(digit & decoder[4]) == 4:
                        value = 9
                    else:
                        value = 0
                number = number * 10 + value
            count += number
    return count


if __name__ == '__main__':
    print(num_unique_digits("day08/input.txt"))
    print(sum_decoded_output("day08/input.txt"))

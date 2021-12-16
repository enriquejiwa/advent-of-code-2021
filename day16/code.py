def sum_version_numbers(filename: str) -> int:
    transmission = ""
    versions = []

    with open(filename) as file:
        hexadecimal = file.readline().strip()
        transmission = bin(int(hexadecimal, 16))[2:].zfill(len(hexadecimal)*4)

    _, sol = read_packet(transmission, 0, versions)
    return sum(versions), sol


def read_packet(transmission: str, index: int, versions: list):
    version = int(transmission[index:index+3], 2)
    versions.append(version)
    type_id = int(transmission[index+3:index+6], 2)
    index += 6
    if type_id == 4:
        finished = False
        binary = ""
        while not finished:
            if transmission[index] == "0":
                finished = True
            binary += transmission[index+1:index+5]
            index += 5
        value = int(binary, 2)
        return index, value
    else:
        values = []
        if transmission[index] == "0":
            length = int(transmission[index+1:index+16], 2)
            index += 16
            end = index + length
            while index != end:
                index, value = read_packet(transmission, index, versions)
                values.append(value)
        else:
            num_subpackets = int(transmission[index+1:index+12], 2)
            index += 12
            for _ in range(num_subpackets):
                index,value = read_packet(transmission, index, versions)
                values.append(value)
        if type_id == 0:
            sol = sum(values)
        elif type_id == 1:
            sol = 1
            for value in values:
                sol *= value
        elif type_id == 2:
            sol = min(values)
        elif type_id == 3:
            sol = max(values)
        elif type_id == 5:
            sol = int(values[0] > values[1])
        elif type_id == 6:
            sol = int(values[0] < values[1])
        else:
            sol = int(values[0] == values[1])
        return index, sol


if __name__ == "__main__":
    print(sum_version_numbers("day16/input.txt"))

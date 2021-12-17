def highest_y(filename: str):
    with open(filename) as file:
        line = file.readline().strip("target area: x=\n")
        x, y = line.split(", y=")
        x1, x2 = [int(t) for t in x.split("..")]
        y1, y2 = [int(t) for t in y.split("..")]
    y_vel_max = abs(y1) - 1
    y_max = y_vel_max * (y_vel_max + 1) // 2
    y_vel_min = y1
    count = 0
    for y_vel in range(y_vel_min, y_vel_max+1):
        for x_vel in range(0, x2+1):
            count += int(hits_target(x_vel, y_vel, x1, x2, y1, y2))
    return y_max, count


def hits_target(x_vel, y_vel, x1, x2, y1, y2):
    x = y = 0
    while y >= y1:
        x += x_vel
        y += y_vel
        x_vel -= int(x_vel > 0)
        y_vel -= 1
        if x1 <= x <= x2 and y1 <= y <= y2:
            return True
    return False


if __name__ == "__main__":
    print(highest_y("day17/input.txt"))

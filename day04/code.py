def read_input(filename: str) -> tuple[list, list]:
    numbers = []
    boards = []
    temp = []
    with open(filename) as file:
        for line in file:
            if not numbers:
                numbers = [int(x) for x in line.split(",")]
            elif line == "\n":
                if temp:
                    boards.append(temp)
                    temp = []
            else:
                row = [int(x) for x in line.split()]
                temp.append(row)
    return numbers, boards


def get_winning_board_score(filename: str) -> int:
    numbers, boards = read_input(filename)
    for number in numbers:
        for board in boards:
            for i, row in enumerate(board):
                for j, value in enumerate(row):
                    if value == number:
                        row[j] = -1
                        if check_win(board, i, j):
                            return value * sum_unmarked(board)

    return -1


def get_losing_board_score(filename: str) -> int:
    numbers, boards = read_input(filename)
    num_boards = len(boards)
    for number in numbers:
        for index, board in enumerate(boards):
            if board:
                for i, row in enumerate(board):
                    for j, value in enumerate(row):
                        if value == number:
                            row[j] = -1
                            if check_win(board, i, j):
                                num_boards -= 1
                                if num_boards == 0:
                                    return value * sum_unmarked(board)
                                boards[index] = []
                                break
                    if not board:
                        break

    return -1


def check_win(board: list, i: int, j: int) -> bool:
    return check_row(board, i) or check_col(board, j)


def check_row(board: list, i: int) -> bool:
    for value in board[i]:
        if value != -1:
            return False
    return True


def check_col(board: list, j: int) -> bool:
    for row in board:
        if row[j] != -1:
            return False
    return True


def sum_unmarked(board) -> int:
    count = 0
    for row in board:
        for value in row:
            if value != -1:
                count += value
    return count


if __name__ == '__main__':
    print(get_winning_board_score("day04/input.txt"))
    print(get_losing_board_score("day04/input.txt"))

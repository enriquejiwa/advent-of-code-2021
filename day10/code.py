CHARACTERS = {"(": ")", "[": "]", "{": "}", "<": ">"}
CHAR_ERROR_SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
CHAR_INCOMPLETE_SCORE = {"(": 1, "[": 2, "{": 3, "<": 4}


def get_score(filename: str) -> int:
    error_score = 0
    incomplete_scores = []
    with open(filename) as file:
        for line in file:
            stack = []
            temp_incomplete = 0
            for char in line:
                if char in CHARACTERS:
                    stack.append(char)
                elif char != "\n" and char != CHARACTERS[stack.pop()]:
                    error_score += CHAR_ERROR_SCORE[char]
                    temp_incomplete = 1
                    break
            if not temp_incomplete:
                for char in reversed(stack):
                    temp_incomplete = temp_incomplete * \
                        5 + CHAR_INCOMPLETE_SCORE[char]
                incomplete_scores.append(temp_incomplete)
    incomplete_scores.sort()
    return error_score, incomplete_scores[len(incomplete_scores) // 2]


if __name__ == '__main__':
    print(get_score("day10/input.txt"))

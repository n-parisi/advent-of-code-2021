with open("input.txt", "r") as f:
    nav_lines = [line.strip() for line in f]

closing_chars = {'(': ')', '[': ']', '{': '}', '<': '>'}


def is_matching(open_char, closing_char):
    expected_closing_char = closing_chars[open_char]
    return closing_char == expected_closing_char


syntax_error_score = 0
completion_scores = []
for line in nav_lines:
    stack = []
    line_valid = True
    for char in line:
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        else:
            open_char = stack.pop()
            if not is_matching(open_char, char):
                line_valid = False
                syntax_error_score += {')': 3, ']': 57, '}': 1197, '>': 25137}[char]
                break
    if line_valid:
        completion_str = [closing_chars[char] for char in stack[::-1]]
        completion_str_score = 0
        for char in completion_str:
            completion_str_score *= 5
            completion_str_score += {')': 1, ']': 2, '}': 3, '>': 4}[char]
        completion_scores.append(completion_str_score)

        # print(f"completed string with {''.join(completion_str)}")

completion_scores = sorted(completion_scores)
print(syntax_error_score)
print(completion_scores[int(len(completion_scores) / 2)])





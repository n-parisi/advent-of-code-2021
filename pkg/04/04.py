def parse_bingo():
    with open("input.txt", "r") as f:
        # get numbers
        numbers = [int(x) for x in f.readline().strip().split(',')]
        # read off extra line before boards
        f.readline()
        # read the boards, each one is a 2D array
        boards = []
        next_board = []
        for line in f:
            if line != '\n':
                next_board.append([[int(x), False] for x in line.split()])
            else:
                boards.append(next_board)
                next_board = []
        return numbers, boards


def check_board(board, called_number):
    # mark number
    for line in board:
        for number in line:
            if number[0] == called_number:
                number[1] = True
    # check if board is a winner
    for i in range(5):
        vertical_winner = True
        for line in board:
            vertical_winner = vertical_winner & line[i][1]
            # check horizontal winner
            if all([number[1] for number in line]):
                return True
        if vertical_winner:
            return True
    return False


def get_board_score(board, called_number):
    total = 0
    for line in board:
        total += sum([number[0] if number[1] is False else 0 for number in line])
    return total * called_number


def find_winner():
    numbers, boards = parse_bingo()
    for number in numbers:
        for board in boards:
            if check_board(board, number):
                return get_board_score(board, number)
    return False


def find_last_winner():
    numbers, boards = parse_bingo()
    for number in numbers:
        winning_boards = []
        for board in boards:
            if check_board(board, number):
                winning_boards.append(board)
                last_score = get_board_score(board, number)
        for winning_board in winning_boards: boards.remove(winning_board)
    return last_score


print(find_winner())
print(find_last_winner())



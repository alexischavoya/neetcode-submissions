from collections import defaultdict

def isValidRows(board):
    for row in board:
        numbers = set()
        for e in row:
            if e == ".":
                continue
            if e in numbers:
                return False
            numbers.add(e)
    return True

def isValidColumns(board):
    for i in range(len(board)):
        numbers = set()
        for j in range(len(board[i])):
            e = board[j][i]
            if e == ".":
                continue
            if e in numbers:
                return False
            numbers.add(e)
    return True

def isValidSquares(board):
    squares = defaultdict(set)
    for i in range(len(board)):
        for j in range(len(board[i])):
            e = board[i][j]
            key = (i//3, j//3)
            if e == ".":
                continue
            if e in squares[key]:
                return False
            squares[key].add(e)
    return True

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return isValidRows(board) and isValidColumns(board) and isValidSquares(board)
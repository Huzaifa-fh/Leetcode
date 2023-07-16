class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_set = set()
            col_set = set()

            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row_set:
                        return False
                    row_set.add(board[i][j])

                if board[j][i] != '.':
                    if board[j][i] in col_set:
                        return False
                    col_set.add(board[j][i])

        for k in range(9):
            box_set = set()

            row = (k // 3) * 3
            col = (k % 3) * 3

            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j] != '.':
                        if board[i][j] in box_set:
                            return False
                        box_set.add(board[i][j])

        return True

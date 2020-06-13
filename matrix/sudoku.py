class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        N = 9
        for i in range(9):
            sudoku_set = set()
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                elif num in sudoku_set or int(num) < 1 or int(num) > 9:
                    return False
                else:
                    sudoku_set.add(num)

        for j in range(9):
            sudoku_set = set()
            for i in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                elif num in sudoku_set or int(num) < 1 or int(num) > 9:
                    return False
                else:
                    sudoku_set.add(num)

        for i in range(3):
            for j in range(3):
                sudoku_set = set()
                for sub_i in range(3):
                    for sub_j in range(3):
                        num = board[3*i + sub_i][3*j + sub_j]
                        if num == ".":
                            continue
                        elif num in sudoku_set or int(num) < 1 or int(num) > 9:
                            return False
                        else:
                            sudoku_set.add(num)

        return True




def main():
    board =[
          ["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]
        ]
    solution = Solution().isValidSudoku(board)
    print solution


if __name__ == '__main__':
    main()

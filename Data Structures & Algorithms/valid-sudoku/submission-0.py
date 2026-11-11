class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        is_valid_sudoku = True
        row_dots = []
        col_dots = []
        rect_dots = []
        for i in range(0, 9):
            row_dots.append([])
            col_dots.append([])
            rect_dots.append([])

        row = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        col = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        rect = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                val = board[i][j]

                row_val = i // 3
                col_val = j // 3
                quadrant = row_val * 3 + col_val

                if val.isdigit():
                    row[i].add(val)
                    col[j].add(val)
                    rect[quadrant].add(val)
                elif val == ".":
                    row_dots[i].append(val)
                    col_dots[j].append(val)
                    rect_dots[quadrant].append(val)
                else:
                    pass

        for i in range(0, 9):
            if (len(row[i]) + len(row_dots[i])) != 9 or (len(col[i]) + len(col_dots[i])) != 9 or (len(rect[i])  + len(rect_dots[i])) != 9:
                is_valid_sudoku = False

        return is_valid_sudoku
  
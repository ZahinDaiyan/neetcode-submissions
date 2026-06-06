class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]

        boxs = [[set() for i in range(3)] for i in range(3)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                # Skip the empty spaces
                if val == ".":
                    continue

                # What 3x3 dose this cell belongs to ?
                br = r//3
                bc = c//3

                # Check for duplicates in the current rows , cols 
                if (val in rows[r] or
                    val in cols[c] or
                    val in boxs[br][bc]):
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxs[br][bc].add(val)

        return True
        
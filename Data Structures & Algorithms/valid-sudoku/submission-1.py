class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        grids = defaultdict(set)  # key (r/3), (c/3)

        for i in range(9):
            for j in range(9):
                item = board[j][i]
                key = (i // 3, j // 3)
                if item in col_set[i] or item in row_set[j] or item in grids[key]:
                    return False
                if item != ".":
                    col_set[i].add(item)
                    row_set[j].add(item)
                    grids[key].add(item)

        return True
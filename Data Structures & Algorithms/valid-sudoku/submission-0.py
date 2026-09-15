class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        hashset = set()

        for i in range(rows):
            for j in range(cols):
                if board[i][j] in hashset:
                    return False
                hashset.add(board[i][j])
        return True
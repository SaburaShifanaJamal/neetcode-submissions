class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            seen=set()
            for j in i:
                if j=='.':
                    continue
                if j not in seen:
                    seen.add(j)
                else:
                    return False
        for i in range(9):
            seen=set()
            for j in range(9):
                if board[j][i]==".":
                    continue
                if board[j][i] in seen:
                    return False
                seen.add(board[j][i])
        for r in range(0,9,3):
            for c in range(0,9,3):
                seen=set()
                for i in range(r,r+3):
                    for j in range(c,c+3):
                        if board[i][j]==".":
                            continue
                        if board[i][j] in seen:
                            return False
                        seen.add(board[i][j])
        return True

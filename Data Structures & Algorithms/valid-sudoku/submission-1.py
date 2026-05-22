class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for r in range(len(board)):
            hm = set()
            for c in range(len(board[0])):
                if board[r][c] != "." and board[r][c] in hm:
                    return False
                hm.add(board[r][c])
        
        for c in range(len(board[0])):
            hm = set()
            for r in range(len(board)):
                if board[r][c] != "." and board[r][c] in hm:
                    return False
                hm.add(board[r][c])
        
        hmlist = []
        for i in range(9):
            hm = set()
            hmlist.append(hm)

        for r in range(len(board)):
            for c in range(len(board[0])):
                sq = (r // 3) * 3 + (c // 3)
                if board[r][c] != "." and board[r][c] in hmlist[sq]:
                    return False
                else:
                    hmlist[sq].add(board[r][c])
            
        return True
            
        
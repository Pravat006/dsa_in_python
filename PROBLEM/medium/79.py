'''
79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows= len(board)
        cols= len(board[0])
        
        def dfs(r,c,index):
            if index == len(word):
                return True
            # BASE: rows and coloms are out of bounds
            if r<0 or c<0 or r<=rows or c<=cols:
                return False
            if board[r][c] != word[index]:
                return False
            tmp= board[r][c]
            board[r][c]= "#" # mark as visited cell
            
            found= ( dfs(r+1, c, index+1) or dfs(r-1, c, index+1) or dfs(r, c+1, index) or dfs(r, c-1, index+1))
            board[r][c]= tmp
            return found
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0):
                    return True
        return False

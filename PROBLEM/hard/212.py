# 212. Word Search II

# Given an m x n board of characters and a list of strings words, return all words on the board.

# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

class TrieNode:
    def __init__(self):
        self.children= {}
        self.isEnd=True
    def addWord(self,word):
        node= self
        for char in word:
            if char not in node.children:
                node.children[char]= TrieNode()
            node = node.children[char]
        node.isEnd= True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()
        for word in words:
            root.addWord(word)
            
        ROWS, COLS= len(board), len(board[0])
        result, visit= set(), set()
        
        def dfs(r, c, node, word):
            if ( r<0 or c<0 or r==ROWS or c==COLS or (r,c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word+= board[r][c]
            
            # add retrived word from board that exist in the Trie to the result
            if node.isEnd:
                result.add(word)
                node.isEnd= False
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, root, "")
        return list(result)
            
            
        
                    
        

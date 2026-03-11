# 211. Design Add and Search Words Data Structure

# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


class WordDictionary(object):

    def __init__(self):
        self.children = {} 
        self.is_end = False
        

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = WordDictionary()  
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(index, node):
            if index == len(word):
                return node.is_end
            
            char = word[index]

            if char in node.children:
                return dfs(index+1, node.children[char])
            
            if char == ".":
                for child in node.children.values():
                    if dfs(index+1, child):
                        return True
                return False
            
            return False

        return dfs(0, self)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
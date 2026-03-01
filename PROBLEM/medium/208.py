# 208. Implement Trie (Prefix Tree)

# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.


class Trie(object):

    def __init__(self):
        self.children={}
        self.endOfWord=False

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curNode = self

        for char in word:
            # create new node as children of root in the character not prsnt
            if char not in curNode.children:
                curNode.children[char]= Trie()
            
            # move the node to the children of current node
            curNode= curNode.children[char]
        
        curNode.endOfWord= True
            

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curNode= self

        for char in word:
            if char not in curNode.children:
                return False
            curNode = curNode.children[char]

        #  return true if the word is complete and end of word marked as true
        return curNode.endOfWord

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curNode= self

        for char in prefix:
            if char not in curNode.children:
                return False
            curNode = curNode.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
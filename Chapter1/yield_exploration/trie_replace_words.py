class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """

        # Time complexity: O(d*s)
        # return brute_force(dictionary, sentence)

        return trie_solution(dictionary, sentence)


class Node:
    def __init__(self, char):
        self.char = char
        self.children = dict()
        self.is_end = False
    
class Trie:
    def __init__(self):
        self.root = Node("/")

    def insert(self, word):
        
        curr = self.root
        
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = Node(char)
                curr = curr.children[char]
        curr.is_end = True

    def replace_word(self,word):
        # Iterate through trie and find the smallest root
        replace_word = ""
        curr = self.root

        for char in word:
            if char in curr.children:
                replace_word = replace_word + char
                curr = curr.children[char]
                if curr.is_end:
                    break
            else:
                return word
        
        return replace_word

def trie_solution(dictionary, sentence):
    
    # Make a trie of all root words
    my_trie = Trie()
    for root in dictionary:
        my_trie.insert(root)

    sentence = sentence.split(" ")
    for i in range(len(sentence)):
        sentence[i] = my_trie.replace_word(sentence[i])
    
    return " ".join(sentence)


def brute_force(dictionary, sentence):
    sentence = sentence.split(" ")
    for root in dictionary:
        length = len(root)
        for i in range(len(sentence)):
            word = sentence[i]
            if len(word)>=length and word[:length]==root:
                sentence[i]=root
                
    return " ".join(sentence)


"""
Brute Force
Time Complexity of a Brute force solution.
w = number of words in sentence
k = length of string(1 word)
d = number of roots in dictionary 
O(d*w*k)

Trie
w = number of words in sentence
k = length of string(1 word)
d = number of roots in dictionary

Insert Operation, make a trie of all the roots: O(d*k)
Replace Word: Traverse throught the root trie for all n words. O(w*k)
"""
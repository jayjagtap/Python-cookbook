
# ****************************************************************************************************************
class Node:
    def __init__(self, char):
        self.char  = char
        self.children = dict()
        self.is_end = False
        self.search_words = list()

class Trie:
    def __init__(self):
        self.root = Node("/")

    def insert(self, word):
        curr = self.root

        for char in word:
            if char in curr.children.keys():
                curr = curr.children[char]
            else:
                curr.children[char] = Node(char)
                curr = curr.children[char]
            if len(curr.search_words) < 3:
                curr.search_words.append(word)
        curr.is_end = True
# ****************************************************************************************************************
class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """

        # return brute_force(products, searchWord)

        return trie_solution(products, searchWord)
        
def trie_solution(products,search_word):
    products.sort()
    my_trie = Trie()
    for product in products:
        my_trie.insert(product)

    curr = my_trie.root
    suggestion_list = []
    for i in range(len(search_word)):
        char = search_word[i]
        if char in curr.children.keys():
            curr = curr.children[char]
            suggestion_list.append(curr.search_words)
        else:
            suggestion_list.append([])
    return suggestion_list

def brute_force(products, searchWord):
    products.sort()
    suggestion_list = [[] for x in range(len(searchWord))]

    for i in range(len(searchWord)):
        substring = searchWord[:i+1]
        for product in products:
            if product[:i+1] == substring:
                suggestion_list[i].append(product)
                if len(suggestion_list[i])==3:
                    break
    
    return suggestion_list



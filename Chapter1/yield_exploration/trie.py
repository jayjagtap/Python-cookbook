class Node:
    def __init__(self, char):
        self.char = char
        self.children = dict()
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = Node(char="/") # Lets denote root node by /

    def insert(self, word):
        curr = self.root

        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = Node(char)
                curr = curr.children[char]
        
        curr.is_end = True

    def search_word(self,word):
        curr = self.root

        for char in word:
            if char in curr.children.keys():
                curr = curr.children[char]
            else:
                return False

        if curr.is_end:
            return True

        return False 
    
    def starts_with(self, word):
        curr = self.root

        for char in word:
            if char in curr.children.keys():
                curr = curr.children[char]
            else:
                return False

        return True

    def print_all_words(self):
        self.print_words_recursive(self.root, visited=set(), word="/")
    
    def print_words_recursive(self, curr, visited, word):
        visited.add(curr)
        if curr.is_end:
            print(word)
        
        for char, childNode in curr.children.items():
            if childNode not in visited:
                self.print_words_recursive(childNode, visited, word+char)
    
if __name__ == "__main__":
    prefix_tree = Trie()
    prefix_tree.insert("apple")
    prefix_tree.insert("apps")
    prefix_tree.insert("bats")
    prefix_tree.insert("bags")
    prefix_tree.insert("cats")
    prefix_tree.insert("cab")
    prefix_tree.print_all_words()
    print(f"Search word: apps: ", prefix_tree.search_word("apps"))
    print(f"Search word: aps: ", prefix_tree.search_word("aps"))
    print(f"Search word: aps: ", prefix_tree.search_word("aps"))
    print(f"Starts with: ca: ", prefix_tree.starts_with("ca"))
    

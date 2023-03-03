class TrieNode():
    def __init__(self, value=None):
        self.value = value
        self.children = set()
        self.is_word = False


class trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, string):
        parent = self.root
        for char in string:
            if not parent.children:
                new_node = TrieNode(char)
                parent.children.add(new_node)
                
            for child in parent.children:
                if child.value == char: # Move to the next word
                    parent = child
                else: # Node not present
                    new_node = TrieNode(char)
                    parent.children.add(new_node)
                    parent = new_node

    def search_word(self, string):
        isPresent=True
        
        parent = self.root
        for char in string:
            for child in parent.chidren:
                if child.value == char:
                    parent = child
                else:
                    isPresent=False
                    break
        
        return isPresent

    def print_trie_bfs(self):

        from collections import deque
        Q = deque()
        Q.append([(x,0) for x in self.root.children])
        bfs = []
        print("Q: ", Q)
        while Q:
            print("Q: ", Q)
            (front, level) = Q.popleft()
            if len(bfs) < level:
                bfs.append([front.value])
            else:
                bfs = level.append(front.value)
            
            for child in front.children: 
                Q.append((child, level+1))

        for row in bfs:
            print(row)

if __name__ == "__main__":
    my_trie = trie()
    my_trie.insert("bat")
    my_trie.insert("bag")
    my_trie.print_trie_bfs()
# Represents a single node in the Trie

class TrieNode:
    def __init__(self, char=''):
        # Initialize this node in the Trie
        self.children = {}
        self.is_complete_word = False
        self.char = char

    def insert(self, char):
        # Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        # all complete words below this point.
        # BFS we will start search from prefix node.
        result = []
        # add prefix to the queue.
        queue = [[self, suffix]]
        while len(queue) != 0:
            # pop one element from the queue.
            element = queue.pop(0)
            # element[0] store the reference of node.
            node_ = element[0]
            # element [1] stores letters that represent the letters in a suffix word.
            word_ = element[1]
            # if this node is word ?
            if node_.is_complete_word:
                # add to our list that contains all words.
                result.append(word_)

            # add all children of this node in queue.
            for j in node_.children:
                child = node_.children.get(j)
                queue.append([child, word_ + child.char])

        return result


class Trie:
    def __init__(self):
        # Initialize this Trie (add a root node).
        self.root = TrieNode()

    def insert(self, word_):
        # Add a word to the Trie.
        if word_ is None or len(word_) == 0:
            return

        # start from root.
        curr = self.root

        for i in range(len(word_)):
            char = word_[i]
            # if char not child to curr node add it as child.
            if char not in curr.children:
                curr.children[char] = TrieNode(char)

            # go deep for one step.
            curr = curr.children[char]

            # if this is the last char in word.
            if i == len(word_) - 1:
                curr.is_complete_word = True

    def find(self, prefix):
        # Find the Trie node that represents this prefix
        if prefix is None:
            return
        # start from root
        curr = self.root
        for char in prefix:
            if char in curr.children:
                curr = curr.children.get(char)
            else:
                return None

        return curr


def f(prefix_):
    if prefix_ != '':
        prefixNode = MyTrie.find(prefix_)
        if prefixNode:
            result = prefixNode.suffixes()
            for i in result:
                print(str(prefix_) + i)
        else:
            print(prefix_ + " not found")
    else:
        print('')


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", "amazing", "Apps", "April", "Book", "Black", "blue"
    , "English", "end", "exciting", "explosive", "output", "or", "Our", "Input", "interesting", "languages", "learned",
    "learning", "linguistics", "key", "fun", "function", "factory", "trie", "trigger", "trigonometry", "tripod",
    "DOWNLOAD", "door", "world", "word", "wood", "Start", "Students", "spaces", "smallest"]

for word in wordList:
    MyTrie.insert(word.lower())

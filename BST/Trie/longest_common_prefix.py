class TrieNode:
    def __init__(self, char):
        self.char = char
        self.children = {}
        self.is_last = False


class Trie:
    def __init__(self):
        self.trie = TrieNode("#")

    def insert(self, word: str) -> None:
        root = self.trie
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode(char)
            root = root.children[char]
        root.is_last = True

    def longestCommonPrefix(self) -> str:
        prefix = []
        root = self.trie

        while True:
            if len(root.children) != 1:
                break

            if root.is_last:
                break

            # python creates an iterator over the keys and next takes one value from an iterator
            char = next(iter(root.children)) # f, l, [o, i] -> break
            prefix.append(char)
            root = root.children[char]

        return "".join(prefix)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        trie = Trie()

        for word in strs:
            trie.insert(word)

        return trie.longestCommonPrefix()
        
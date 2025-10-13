class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        def _search_helper(node, word):
            if not word:
                return node.end_of_word

            c = word[0]
            word_part = word[1:]

            if c == '.':
                for child_node_key in node.children:
                    child_node = node.children[child_node_key]
                    if _search_helper(child_node, word_part):
                        return True
                return False
            else:
                if c in node.children:
                    return _search_helper(node.children[c], word_part)
                else:
                    return False

        # main part
        curr = self.root
        return _search_helper(curr, word)


def test_word_dict():
    word_dict = WordDictionary()
    word_dict.addWord("bad")
    word_dict.addWord("dad")
    word_dict.addWord("mad")
    assert word_dict.search("pad") is False
    assert word_dict.search("bad") is True
    assert word_dict.search(".ad") is True
    assert word_dict.search("b..") is True

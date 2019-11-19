import sys
sys.path.append('..')
from trie import Trie, TrieNode

def replace_words(dict, sentence):
    trie = Trie()
    [trie.insert(word) for word in dict]
    res = []
    for word in sentence.split(' '):
        replaced_word = trie.replace_with_prefix(word)
        if replaced_word:
            res.append(replaced_word)
        else:
            res.append(word)
    return ' '.join(res)
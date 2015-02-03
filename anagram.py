__author__ = 'blink'
LEN_THRESHOLD = 1

import re
import unicodedata
from binary_search_tree import BinarySeachTree

class Anagram():
    def __init__(self, filename):
        self._file = open(filename, 'r')
        self._anagrams = dict()

    def findAnagrams(self):
        if self._anagrams:
            return self._anagrams

        for line in self._file:
            if not line:
                continue
            # Split the line by white space and -
            for word in re.split('-|\s+|[\r\n]+', line):
                if not word:
                    continue
                stripped_word = self._transformWord(word)
                # Check for the length threshold
                if len(stripped_word) > LEN_THRESHOLD:
                    self._addAnagram(stripped_word)

        self._file.close()

        # Here we could use the implementation of BST with a small change:
        # replace value functionality with key and for value store something.
        # In this case we would store the list of anagrams (values from dict)
        # and the key for a node would be the count for each list. In this
        # manner we could print the list of anagrams by it's count, and the
        # complexity will be reduced.
        # Later edit: modified the original implementation to add 'storage':
        # value is for key, storage is for value.
        anagrams_bst = BinarySeachTree()
        for k in self._anagrams:
            anagrams = self._anagrams[k]
            if len(anagrams) > 1:
                anagrams_bst.insert(len(anagrams), anagrams)

        self._anagrams = anagrams_bst
        return self._anagrams

    def _transformWord(self, word):
        nkfd_form = unicodedata.normalize('NFKD', unicode(word, 'utf-8'))
        word = str(u''.join([c for c in nkfd_form if not unicodedata.combining(c)]).encode('utf8')).lower()
        pattern = re.compile('[\W_]+')
        stripped = pattern.sub('', word)
        return stripped

    def _addAnagram(self, word):
        key = self._hashWord(word)
        self._anagrams.setdefault(key, list())
        if self._anagrams[key].count(word) == 0:
            self._anagrams[key].append(word)

    def _hashWord(self, word):
        """The most suitable hash is to order chars in alphabetical order"""
        return ''.join(sorted(word))

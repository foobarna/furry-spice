__author__ = 'blink'

from binary_search_tree import BinarySeachTree
from anagram import Anagram


def test_bst():
    values = [50, 17, 12, 9, 14, 23, 19, 72, 76, 54, 67]
    bst = BinarySeachTree()
    for v in values:
        bst.insert(v)

    print "Values stored: ",
    bst.printNodes()

    print "Values in range (23, 68): ", bst.rangeValues(23, 68)


def test_anagram():
    a = Anagram('eng-text.txt')
    print 'The anagrams found in text:'
    a.findAnagrams().printNodesAndStorage()


if __name__ == '__main__':
    test_bst()
    test_anagram()

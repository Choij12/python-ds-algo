from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable

def tree_intersection(tree1, tree2):
    tree1_set = set(tree1.pre_order())
    tree2_set = set(tree2.pre_order())

    intersect = tree1_set.intersection(tree2_set)

    intersect_list = list(intersect)

    return intersect_list

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from BPTree import BPTree
from DatabasePrime import Database

def test_bptree_split():
    tree = BPTree(order=3)
    keys = ["Alice", "Bob", "Charlie", "David", "Eve"]  # Force multiple splits
    for key in keys:
        tree.insert(key, f"Record_{key}")
    print("Tree structure after insertions:")
    print("Root keys:", tree.racine.keys)
    for child in tree.racine.children:
        print("Child keys:", child.keys)

test_bptree_split()
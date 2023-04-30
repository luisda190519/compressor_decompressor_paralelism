import heapq
import numpy as np

class HuffmanNode:
    def __init__(self, freq, char=None):
        self.freq = freq
        self.char = char
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def to_array(self):
        left_arr = np.array([-1])
        right_arr = np.array([-1])
        if self.left is not None:
            left_arr = self.left.to_array()
        if self.right is not None:
            right_arr = self.right.to_array()
        return np.concatenate(([self.freq, self.char], left_arr, right_arr))

    @staticmethod
    def from_array(arr):
        node = HuffmanNode(arr[0], arr[1])
        if arr[2] != -1:
            node.left = HuffmanNode.from_array(arr[arr[2]:arr[3]])
        if arr[3] != -1:
            node.right = HuffmanNode.from_array(arr[arr[3]:])
        return node

def build_tree(freqs):
    heap = [HuffmanNode(freq, char) for char, freq in freqs.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = HuffmanNode(left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(heap, parent)
    return heap[0]

def build_codes(tree):
    codes = {}
    stack = [(tree, "")]
    while stack:
        node, code = stack.pop()
        if node.char is not None:
            codes[node.char] = code
        else:
            stack.append((node.left, code + "0"))
            stack.append((node.right, code + "1"))
    return codes
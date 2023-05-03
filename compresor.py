from huffman import HuffmanNode
import numpy as np
import time
import sys
import heapq

def build_frequency_table(text):
    freq_dict = {}
    for char in text:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

def build_huffman_tree(freq_dict):
    heap = []
    for char, freq in freq_dict.items():
        node = HuffmanNode(freq, char)
        heapq.heappush(heap, node)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = HuffmanNode(left.freq + right.freq)
        parent.left, parent.right = left, right
        heapq.heappush(heap, parent)

    return heap[0]

def build_codeword_table(root):
    codes = {}
    stack = [(root, "")]
    while stack:
        node, code = stack.pop()
        if node.char is not None:
            codes[node.char] = code
        else:
            stack.append((node.left, code + "0"))
            stack.append((node.right, code + "1"))
    return codes

def huffman_compress(text):
    freq_dict = build_frequency_table(text)
    root = build_huffman_tree(freq_dict)
    codeword_dict = build_codeword_table(root)
    encoded_text = "".join(codeword_dict[byte] for byte in text)
    encoded_text_bytes = int(encoded_text, 2).to_bytes(len(encoded_text) // 8, byteorder="big")
    # Convert the encoded text to a NumPy array of integers for efficient storage
    return encoded_text_bytes, root

if __name__ == "__main__":
    filename = sys.argv[1]
    compressed_filename = "comprimido.elmejorprofesor"
    start_time = time.time()

    # Abrimos el archivo de texto
    with open(filename, 'r') as f:
        text = f.read()

    # Comprimir el texto
    compressed, root = huffman_compress(text)

    # Guardar la codificación Huffman y el texto comprimido en archivos separados
    with open(compressed_filename, 'wb') as f:
        np.save(f, compressed)
        np.save(f, root.to_array())

    end_time = time.time()
    print(f"Compression time: {end_time - start_time:.2f} seconds")
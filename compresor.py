from huffman import HuffmanNode
import numpy as np
import time
import sys

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
        heap.append(node)

    while len(heap) > 1:
        left = heap.pop(0)
        right = heap.pop(0)
        parent = HuffmanNode(left.freq + right.freq)
        parent.left, parent.right = left, right
        heap.append(parent)

    return heap[0]

def build_codeword_table(root):
    codeword_dict = {}

    def traverse(node, codeword=''):
        if node is None:
            return

        if node.char is not None:
            codeword_dict[node.char] = codeword

        traverse(node.left, codeword + '0')
        traverse(node.right, codeword + '1')

    traverse(root)
    return codeword_dict

def encode_text(text, codeword_dict):
    encoded_text = ''
    for char in text:
        encoded_text += codeword_dict[char]
    return encoded_text

def huffman_compress(text):
    freq_dict = build_frequency_table(text)
    root = build_huffman_tree(freq_dict)
    codeword_dict = build_codeword_table(root)
    encoded_text = encode_text(text, codeword_dict)
    # Convert the encoded text to a NumPy array of integers for efficient storage
    encoded_array = np.array([int(bit) for bit in encoded_text], dtype=np.uint8)
    return encoded_array, root

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

print("Tiempo de ejecución:", time.time() - start_time)
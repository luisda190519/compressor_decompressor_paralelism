import heapq
import numpy as np
import sys
import time
from huffmanMejorado import build_tree, build_codes, HuffmanNode

def compress(input_file_name, output_file_name):
    start_time = time.time()
    with open(input_file_name, "rb") as input_file:
        data = input_file.read()
    freqs = {}
    for byte in data:
        if byte not in freqs:
            freqs[byte] = 0
        freqs[byte] += 1
    tree = build_tree(freqs)
    codes = build_codes(tree)
    encoded_data = "".join(codes[byte] for byte in data)
    padding_length = 8 - len(encoded_data) % 8
    encoded_data += "0" * padding_length
    encoded_data_bytes = int(encoded_data, 2).to_bytes(len(encoded_data) // 8, byteorder="big")
    tree_array = tree.to_array()
    with open(output_file_name, "wb") as output_file:
        output_file.write(padding_length.to_bytes(1, byteorder="big"))
        # Write the size of the serialized Huffman tree to the output file
        output_file.write(tree_array.nbytes.to_bytes(4, byteorder="big"))
        output_file.write(tree_array.tobytes())
        output_file.write(encoded_data_bytes)
    end_time = time.time()
    print(f"Compression time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    compress(sys.argv[1], "comprimidoMejorado.elmejorprofesor")
from huffmanMejorado import HuffmanNode
import sys
import time
import numpy as np


def decompress(input_file_name, output_file_name):
    start_time = time.time()
    with open(input_file_name, "rb") as input_file:
        padding_length = int.from_bytes(input_file.read(1), byteorder="big")
        tree_size = int.from_bytes(input_file.read(4), byteorder="big")
        tree_array = np.frombuffer(input_file.read(tree_size), dtype=np.int32)
        tree = HuffmanNode.from_array(tree_array)
        encoded_data_bytes = input_file.read()
    encoded_data = bin(int.from_bytes(encoded_data_bytes, byteorder="big"))[2:].zfill(8 * ((len(encoded_data_bytes) * 8 + 7) // 8))
    encoded_data = encoded_data[:-padding_length]
    decoded_data = bytearray()
    node = tree
    for bit in encoded_data:
        if bit == "0":
            node = node.left
        else:
            node = node.right
        if node.char is not None:
            decoded_data.append(node.char)
            node = tree
    with open(output_file_name, "wb") as output_file:
        output_file.write(decoded_data)
    end_time = time.time()
    print(f"Decompression time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    decompress(sys.argv[1], "descomprimido-elmejorprofesor.txt")
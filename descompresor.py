from huffman import HuffmanNode
import numpy as np
import time
import pickle


def decode_text(encoded_text, root):
    decoded_text = ''
    node = root

    for bit in encoded_text:
        if bit == "0":
            node = node.left
        else:
            node = node.right

        if node.char is not None:
            decoded_text += node.char
            node = root

    return decoded_text

def huffman_decompress(encoded_text, root):
    decoded_text = decode_text(encoded_text, root)
    return decoded_text

if __name__ == "__main__":
    start_time = time.time()

    # Load Huffman encoding and compressed text from file
    compressed_filename = "comprimido.elmejorprofesor"
    try:
        with open(compressed_filename, 'rb') as f:
            compressed = bin(int.from_bytes(np.load(f, allow_pickle=True), byteorder='big'))[2:]
            root = HuffmanNode.from_array(np.load(f, allow_pickle=True))
            file_format = np.load(f, allow_pickle=True).tobytes().decode()
            ENCODING = np.load(f, allow_pickle=True).tobytes().decode()
    except (FileNotFoundError, IOError):
        print(f"Error reading compressed file: {compressed_filename}")
        exit(1)
    except (EOFError, pickle.UnpicklingError):
        print(f"Error unpickling data in file: {compressed_filename}")
        exit(1)

    # Decompress the text
    decoded_text = huffman_decompress(compressed, root)
    decompressed_filename = f"descomprimido-elmejorprofesor.{file_format}"
    try:
        with open(decompressed_filename, 'wb') as f:
            f.write(decoded_text.encode(ENCODING))
    except IOError:
        print(f"Error writing decompressed file: {decompressed_filename}")
        exit(1)

    end_time = time.time()
    print(f"Decompression time: {end_time - start_time:.2f} seconds")

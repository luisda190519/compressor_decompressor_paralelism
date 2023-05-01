from huffman import HuffmanNode
import numpy as np
import time

def decode_text(encoded_text, root):
    decoded_text = ''
    node = root

    for bit in encoded_text:
        if bit == '0':
            node = node.left
        else:
            node = node.right

        if node.char is not None:
            decoded_text += node.char
            node = root

    return decoded_text

def huffman_decompress(encoded_array, root):
    # Convert the NumPy array back to a string of bits
    encoded_text = ''.join([str(bit) for bit in encoded_array])
    decoded_text = decode_text(encoded_text, root)
    return decoded_text

if __name__ == "__main__":
    compressed_filename = "comprimido.elmejorprofesor"
    decompressed_filename = "descomprimido-elmejorprofesor.txt"
    start_time = time.time()

    # Cargar la codificación Huffman y el texto comprimido desde los archivos
    with open(compressed_filename, 'rb') as f:
        compressed = bin(int.from_bytes(np.load(f, allow_pickle=True), byteorder='big'))[2:]
        root = HuffmanNode.from_array(np.load(f, allow_pickle=True))

    # Descomprimir el texto
    decoded_text = huffman_decompress(compressed, root)
    with open(decompressed_filename, 'w') as f:
        f.write(decoded_text)

    end_time = time.time()
    print(f"Decompression time: {end_time - start_time:.2f} seconds")
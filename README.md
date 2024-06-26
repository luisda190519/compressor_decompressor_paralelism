# Huffman Compression and Decompression

This project implements a text compressor and decompressor using the Huffman coding algorithm in Python. It utilizes parallelism for improved performance.

## Features

- Text compression using Huffman coding
- Text decompression
- Support for various file formats and encodings
- Efficient storage using NumPy arrays
- Performance timing for compression and decompression processes

## Requirements

- Python 3.x
- NumPy

## Usage

### Compression

To compress a file:

```bash
  python compresor.py <input_filename>
```

This will create a compressed file named `comprimido.elmejorprofesor`.

### Decompression

To decompress a file:

```bash
  python descompresor.py comprimido.elmejorprofesor
```

This will create a decompressed file named `descomprimido-elmejorprofesor.<original_format>`.

## How it Works

### Compression (compresor.py)

1. Reads the input file
2. Builds a frequency table of characters
3. Constructs a Huffman tree
4. Generates codewords for each character
5. Encodes the text using the generated codewords
6. Stores the compressed data and Huffman tree in a file

### Decompression (descompresor.py)

1. Reads the compressed file
2. Reconstructs the Huffman tree
3. Decodes the compressed text using the Huffman tree
4. Writes the decompressed text to a file

## Performance

The script outputs the time taken for compression and decompression in seconds.


## Contributing

Contributions to improve the algorithm, add parallelism, or enhance the project in any way are welcome. Please feel free to submit pull requests or open issues for discussion.


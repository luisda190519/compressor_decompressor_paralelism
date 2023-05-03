import sys
import os

if __name__ == "__main__":
    filename = sys.argv[1]
    decompressed_filename = "descomprimido-elmejorprofesor.txt"

    original_size = os.path.getsize(filename)
    compressed_size = os.path.getsize(decompressed_filename)
    compression_rate = compressed_size / original_size
    print(f"Original size: {original_size} bytes")
    print(f"Compressed size: {compressed_size} bytes")
    print(f"Compression rate: {compression_rate:.2f}")

    try:
      ENCODING = 'utf-8'
      with open(filename, "r", encoding=ENCODING) as archivo1, open(decompressed_filename, "r", encoding=ENCODING) as archivo2:
          for linea1, linea2 in zip(archivo1, archivo2):
              if linea1 != linea2:
                  print("nok")
                  break
          else:
              print("ok")
    except:
      ENCODING = 'cp1252'
      with open(filename, "r", encoding=ENCODING) as archivo1, open(decompressed_filename, "r", encoding=ENCODING) as archivo2:
        for linea1, linea2 in zip(archivo1, archivo2):
            if linea1 != linea2:
                print("nok")
                break
        else:
            print("ok")

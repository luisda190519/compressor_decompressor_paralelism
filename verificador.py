import sys
import os

if __name__ == "__main__":
    filename = sys.argv[1]
    file_format = filename.split('.')[-1]
    compressed_filename = "comprimido.elmejorprofesor"
    decompressed_filename = "descomprimido-elmejorprofesor.{}".format(file_format)
    
    with open(filename, "rb") as archivo1, open(decompressed_filename, "rb") as archivo2:
        try:
            archivo1 = archivo1.read().decode("cp1252")
            archivo2 = archivo2.read().decode("cp1252")
        except:
            archivo1 = archivo1.read().decode("utf-8")
            archivo2 = archivo2.read().decode("utf-8")
        for linea1, linea2 in zip(archivo1, archivo2):
            if linea1 != linea2:
                print("nok")
                break
        else:
            print("ok")
      

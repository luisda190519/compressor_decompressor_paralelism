import time
import sys

filename = sys.argv[1]
decompressed_filename = "descomprimido-elmejorprofesor.txt"
start_time = time.time()

with open(filename, "r") as archivo1, open(decompressed_filename, "r") as archivo2:
    for linea1, linea2 in zip(archivo1, archivo2):
        if linea1 != linea2:
            print("Los archivos no son idénticos")
            break
    else:
        print("Los archivos son idénticos")

print("Tiempo de ejecución:", time.time() - start_time)
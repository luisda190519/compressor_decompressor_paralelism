import time
import sys

filename = sys.argv[1]
decompressed_filename = "descomprimido-elmejorprofesor.txt"
start_time = time.time()

with open(filename, "r") as archivo1, open(decompressed_filename, "r") as archivo2:
    for linea1, linea2 in zip(archivo1, archivo2):
        if linea1 != linea2:
            print("nok")
            break
    else:
        print("ok")

print("Tiempo de ejecución:", time.time() - start_time)

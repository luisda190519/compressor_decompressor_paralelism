import sys

if __name__ == "__main__":
    filename = sys.argv[1]
    decompressed_filename = "descomprimido-elmejorprofesor.txt"

    with open(filename, "r") as archivo1, open(decompressed_filename, "r") as archivo2:
        for linea1, linea2 in zip(archivo1, archivo2):
            if linea1 != linea2:
                print("nok")
                break
        else:
            print("ok")

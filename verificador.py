import sys

if __name__ == "__main__":
    filename = sys.argv[1]
    decompressed_filename = "descomprimido-elmejorprofesor.txt"

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

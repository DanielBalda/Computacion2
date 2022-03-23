import argparse
import os


class InvalidFileName(Exception):
    pass

parser = argparse.ArgumentParser(description="Copia de un archivos Origen a uno Destino")

parser.add_argument("-i", "--origen", type=str, required=True, help="Archivo Origen")
parser.add_argument("-o", "--destino", type=str, required=True, help="Archivo Destino")
args = parser.parse_args()

try:
    if(not os.path.exists(args.fileA)):
        raise InvalidFileName()
    with open(args.fileA, 'r') as f:
        lines = f.readlines()
except InvalidFileName:
    print("El archivo origen no existe")
    exit()

with open(args.fileB, 'w+') as f:
    f.writelines(lines)

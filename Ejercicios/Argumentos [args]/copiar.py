import argparse
import os


class FileNotExist(Exception):
    pass


parser = argparse.ArgumentParser(description="Copia de un archivos Origen a uno Destino")

parser.add_argument("-i",
                    "--origen",
                    type=str,
                    required=True,
                    help="Archivo Origen")
parser.add_argument("-o",
                    "--destino",
                    type=str,
                    required=True,
                    help="Archivo Destino")
args = parser.parse_args()

try:
    if(not os.path.exists(args.origen)):
        raise FileNotExist()
except FileNotExist:
    print("El archivo origen no existe")
    exit()
origen = os.open(args.origen, os.O_RDONLY)
destino = os.open(args.destino, os.O_WRONLY|os.O_CREAT)
os.write(destino, os.read(origen, os.path.getsize(origen)))
os.close(origen)
os.close(destino)
print("Copia finalizada.")

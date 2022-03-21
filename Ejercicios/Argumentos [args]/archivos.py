import argparse
from ast import arg
from importlib.resources import path
import os


class InvalidFileName(Exception):
    pass

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--fileA", type=str, required=True, help="text file")
parser.add_argument("-o", "--fileB", type=str, required=True, help="text file")
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

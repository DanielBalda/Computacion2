import argparse
import os
from multiprocessing import Pool

def main():
    parser = argparse.ArgumentParser(description="Comandos")
    parser.add_argument("-f",
                        "--file",
                        type=str,
                        required=False,
                        help="file")
    parser.add_argument("-p",
                        "--process",
                        type=int,
                        required=True,
                        help="Number of process")
    parser.add_argument("-c",
                        "--calculate",
                        type=str,
                        required=False,
                        help="Operation")
    args = parser.parse_args()
    pool = Pool(processes=args.process)
    lista = openFile(args.file)
    result = pool.map(funcion_calculo, lista)
    print(result)

def openFile(file):
    matrix=[]
    with open(file, 'r') as f:
        for line in f.readlines():
            matrix.append(list(line.strip().replace(",","").replace(" ", "")))
    return matrix

def funcion_calculo(row):
    result=[]
    for num in row:
        num=int(num)
        result.append(num*num)
    return result


if __name__=="__main__":
    main()
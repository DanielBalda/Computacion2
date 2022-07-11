import argparse
import time
import math
from multiprocessing import Pool
from functools import partial

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
                        help="Operation: 'raiz', 'pot', 'log'")
    args = parser.parse_args()
    pool = Pool(processes=args.process)
    matrix = openFile(args.file)
    result = pool.map(partial(calculate, args.calculate), matrix)
    for row in result:
        print(', '.join(str(number) for number in row))

def openFile(file):
    matrix=[]
    with open(file, 'r') as f:
        for line in f.readlines():
            line = line.strip().split(",")
            matrix.append(line)
    return matrix

def calculate(operation, row):
    time.sleep(.5)
    result=[]
    if(operation == 'raiz'):
        for num in row:
            num=int(num)
            result.append(round(math.sqrt(num), 2))
    if(operation == 'pot'):
        for num in row:
            num=int(num)
            result.append(num*num)
    if(operation == 'log'):
        for num in row:
            num=int(num)
            result.append(round(math.log10(num), 2))
    return result


if __name__=="__main__":
    main()
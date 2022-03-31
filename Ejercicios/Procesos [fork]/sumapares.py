import argparse as ap
import os
import time

def proceso_hijo():
    sumatoria = 0
    for number in range(os.getpid()):
        if number%2 == 0:
            sumatoria += number
    return sumatoria

def main():
    parser = ap.ArgumentParser(description="Generador de procesos")
    parser.add_argument("-n",
                        "--numeros",
                        type=int,
                        required=True,
                        help="Numero de procesos")
    parser.add_argument("-v",
                        "--verbose",
                        help="Activar salida con mensajes",
                        action="store_true")
    args = parser.parse_args()
    for _ in range(args.numeros):
        if(os.fork() == 0):
            print("{} - {}: {}".format(os.getpid(),os.getppid(), proceso_hijo()))
            os._exit(0)
        os.wait() 

if __name__=="__main__":
    main()
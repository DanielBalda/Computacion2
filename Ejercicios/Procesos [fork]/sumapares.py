import argparse as ap
import os

def proceso_hijo(pid):
    sumatoria = 0
    for number in range(pid):
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
            pid = os.getpid()
            if (args.verbose):
                print(f"Starting process {pid}")
            print(f"{pid} - {os.getppid()}: {proceso_hijo(pid)}")
            os._exit(0)
        pidChild, _ = os.wait()
        if (pidChild and args.verbose):
            print(f"Ending process {pidChild}")

if __name__=="__main__":
    main()
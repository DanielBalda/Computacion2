import argparse as ap
import os
import time
    
parser = ap.ArgumentParser(description="Procesos escritores en archivo")

parser.add_argument("-n",
                    "--number",
                    type=int,
                    required=True,
                    help="Numero de procesos a crear")
parser.add_argument("-r",
                    "--recursive",
                    type=int,
                    required=True,
                    help="Cantidad de veces a repetir")
parser.add_argument("-f",
                    "--file",
                    type=str,
                    required=True,
                    help="Ubicacion del archivo a escribir")
parser.add_argument("-v",
                    "--verbose",
                    help="Activar salida con mensajes",
                    action="store_true")
args = parser.parse_args()

outputFile = os.open( args.file, os.O_WRONLY|os.O_TRUNC|os.O_CREAT )
for _ in range(args.number):
    if os.fork() == 0:
        letter=chr(_+65)
        for __ in range(args.recursive):
            if args.verbose:
                print(f"Proceso {os.getpid()} escribiendo letra '{letter}'.")
            os.write(outputFile, bytes(letter, 'utf-8'))
            os.fsync(outputFile)
            time.sleep(1)
        os._exit(0)
    os.wait()
os.close(outputFile)

readFile = os.open(args.file, os.O_RDONLY)
size = os.fstat(readFile).st_size
while size > 0:
    print(os.read(readFile, 1024).decode("utf-8"))
    size-=1024
os.close(readFile)

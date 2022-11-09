import calc
import argparse

def main():
    global args,lines,results

    parser = argparse.ArgumentParser(description="Comandos")
    parser.add_argument("-f","--file",required=True,help="Archivo a procesar")
    parser.add_argument("-c","--calculate",required=True,help="Operacion a realizar")
    args = parser.parse_args()

    lines = []
    results = []

    read_lines(args.file)
    calculate_function(args.calculate)

def read_lines(file):
    with open(file) as f:
        global lines
        for line in f:
            strip_lines = line.strip('')
            listli = strip_lines.split()
            print(listli)
            for i in range(len(listli)):
                listli[i] = int(listli[i])
            m = lines.append(listli)
            
            
def calculate_function(calculate):
    for i in range(len(lines)):
        if calculate == "root":
            resultado = calc.raiz_cuadrada.delay(lines[i])
            resultado = resultado.get()
        
        elif calculate == "pow":
            resultado = calc.potencia.delay(lines[i])
            resultado = resultado.get()
        
        elif args.calculate == "log":
            resultado = calc.logaritmo.delay(lines[i])
            resultado = resultado.get()
    print("Calculo realizado con exito")

if __name__ == "__main__":
    main()
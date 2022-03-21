import sys
import getopt


def tryNumber(ar):
    try:
        return int(ar)
    except ValueError:
        print("Numero Invalido. Solo enteros")
        exit()


def getArg(opt):
    try:
        operator = ''
        numA = ''
        numB = ''
        for op, ar in opt:
            if op == '-o':
                if(ar not in "*/+-"):
                    raise ValueError()
                operator = ar
            elif op == '-n':
                numA = tryNumber(ar)
            else:
                numB = tryNumber(ar)
        return print(eval(str(numA)+operator+str(numB)))
    except ValueError:
        print("Operador Invalido. Solo (*, /, -, +)")


def main():
    opt, _ = getopt.getopt(sys.argv[1:], 'o:n:m:')
    if opt == []:
        return print("Ingrese los argumentos necesarios")
    getArg(opt)


main()

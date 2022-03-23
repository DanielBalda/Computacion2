import sys
import getopt


class InvalidNumber(Exception):
    pass


def getArg(opt):
    try:
        for op, ar in opt:
            if op == '-o':
                if(ar not in "*/+-"):
                    raise ValueError()
                operator = ar
            elif op == '-n':
                if ar.isnumeric():
                    numA = ar
                else:
                    raise InvalidNumber()
            else:
                if ar.isnumeric():
                    numB = ar
                else:
                    raise InvalidNumber()
        return print(eval(str(numA)+operator+str(numB)))
    except ValueError:
        print("Operador Invalido. Solo (*, /, -, +)")
    except InvalidNumber:
        print("Deben ser enteros.")


def main():
    try:
        opt, _ = getopt.getopt(sys.argv[1:], 'o:n:m:')
        if opt == [] or len(opt) < 3:
            return print("Opciones/Argumentos incompletos.")
        getArg(opt)
    except getopt.GetoptError:
        print("Ingrese opciones correctas.")
        exit()


if __name__ == "__main__":
    main()

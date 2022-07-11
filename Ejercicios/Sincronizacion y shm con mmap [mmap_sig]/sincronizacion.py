import mmap, time, os, sys, argparse, signal

def main():
    parser = argparse.ArgumentParser(description="Comandos")
    parser.add_argument("-f",
                        "--file",
                        type=str,
                        required=True,
                        help="Archivo a buscar")
    global file
    file = parser.parse_args().file
    fork_generator()

def fork_generator():
    global list_pid
    list_pid = []
    global mapeo
    mapeo = mmap.mmap(-1, 1024)
    for index in range(2):
        ret = os.fork()
        if ret == 0:
            if index == 0:
                for index in sys.stdin:
                    if index[:3] == "bye":
                        os.kill(os.getpid(), signal.SIGUSR2)
                        print("Muere el padre..")
                        sys.exit(0)
                    mapeo.write(index.encode())
                    os.kill(os.getppid(),signal.SIGUSR1)
            
            else:
                signal.signal(signal.SIGUSR1, handler_hijo)
                signal.signal(signal.SIGUSR2, handler_hijo)
                while True:
                    signal.pause()
        else:
            list_pid.append(ret)
    signal.signal(signal.SIGUSR1, handler_padre)
    signal.signal(signal.SIGUSR2, handler_padre)
    os.wait()

def handler_hijo(s, f):
    if s == signal.SIGUSR1:
        data = mapeo.readline().decode().upper()
        write_file(data)
        print(f"Hijo 2 lee: {data}")
    elif s == signal.SIGUSR2:
        print("Hijo 2 muere")
        sys.exit(0)

def handler_padre(s, f):
    if s == signal.SIGUSR1:
        data = mapeo.readline().decode()
        print(f"Contenido: {data}")
        time.sleep(.5)
        os.kill(list_pid[1],signal.SIGUSR1)
    elif s == signal.SIGUSR2:
        os.kill(list_pid[1], signal.SIGUSR2)
        os.wait()
        sys.exit(0)

def write_file(data):
    f = open(file, "a")
    f.write(data)
    f.close()

if __name__ == "__main__":
    main()
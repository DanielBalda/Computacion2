from multiprocessing import Queue
from threading import Thread
import sys


def thread_1(queue1,queue2):
    print("Hilo 1")
    sys.stdin = open(0)
    print("Ingrese una linea:")
    line = sys.stdin.readline()
    queue1.put(line)
    data_encrypt = queue2.get()
    print(f"Hilo 1 recibe mensaje encriptado:{data_encrypt}")

def thread_2(queue1,queue2):
    data = queue1.get()
    print(f"Hilo 2 recibe mensaje: {data}")
    data_encrypt = encrypt(data)
    print("Hilo 2 almacena mensaje encriptado...")
    queue2.put(data_encrypt)

def encrypt(data): #ROT13 a mano utilizando ASCII
    data_encrypt = ""
    for letter in data.strip():
        letter = ord(letter)
        if letter == 32:
            data_encrypt += "%" #uso '%' para los espacios en blanco
        else:
            if(letter > 109):
                data_encrypt += chr(letter-13)
            else:
                data_encrypt += chr(letter+13)
    return data_encrypt

def main():
    q1 = Queue()
    q2 = Queue()
    t1 = Thread(target = thread_1,args=(q1,q2), daemon = True)
    t2 = Thread(target = thread_2,args=(q1,q2), daemon = True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
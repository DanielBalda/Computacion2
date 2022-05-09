import multiprocessing as mp
import sys

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

def child(r, w, q, nproc):
    if nproc == 1:
        r.close()
        sys.stdin = open(0)
        print("Texto a encriptar:")
        text = sys.stdin.readline()
        w.send(text)
        print(f"Texto Encriptado:\n{q.get()}")
    if nproc == 2:
        w.close()
        q.put(encrypt(r.recv())) #recive el texto, lo encripta y lo coloca en la cola
    w.close()
    r.close()

def main():
    r, w = mp.Pipe()
    q = mp.Queue()
    p1 = mp.Process(target=child, args=(r, w, q, 1))
    p2 = mp.Process(target=child, args=(r, w, q, 2))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__=="__main__":
    main()

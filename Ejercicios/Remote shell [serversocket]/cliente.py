import socket
import sys
import argparse
import sys
    
def client(h,p):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print("Socket creation failed")
        sys.exit()
    
    host, port = h, p
    print("Conectando...")
    s.connect((host,port))
    while True:
        msg = input("Ingrese comando a ejecutar:")
        if msg == "exit server":
            print("Conexion finalizada...")
            s.close()
            exit()
        if msg == "stop server":
            print("Conexion finalizada...")
            s.send('stop server'.encode())
            s.close()
            exit()
        s.send(msg.encode())
        print("Esperando respuesta del server")
        msg = s.recv(1024)
        print("\n"+msg.decode())
    
def main():
    parser = argparse.ArgumentParser(description="Comandos")
    parser.add_argument("-ht","--host",required=True,help="Dirección IP o nombre del servidor al que conectarse")
    parser.add_argument("-p","--port", type=int,required=True,help="Numero de puerto del servidor")
    args = parser.parse_args()
    print(args.host,args.port)
    client(args.host,args.port)

if __name__ == '__main__':
    main()
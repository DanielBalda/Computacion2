import socketserver,subprocess,socket,threading
import signal,os,argparse


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print(self.data)
            pp = subprocess.Popen([self.data], stdout = subprocess.PIPE,stderr = subprocess.PIPE, shell = True)
            out,err = pp.communicate()
            if err:
                self.request.sendall(b"ERROR \n"+err)
                print(err)
            else:
                self.request.sendall(b"OK\n"+out)
                print(out)
            
            print("PID: %d" % os.getpid())

class ProcTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


class ThrTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class ProcTCPServer6(socketserver.ForkingMixIn, socketserver.TCPServer):
    address_family = socket.AF_INET6
    pass

class ThrTCPServer6(socketserver.ThreadingMixIn, socketserver.TCPServer):
    address_family = socket.AF_INET6
    pass

def servicio(d,c):
    if d[0] == socket.AF_INET:
        print("ipv4")
        if c == 'p':
            with ProcTCPServer((HOST, PORT), MyTCPHandler) as server:
                server.serve_forever()
                try:
                    signal.pause()
                except:
                    server.shutdown()
    
        if c == 't':
            with ThrTCPServer((HOST, PORT), MyTCPHandler) as server:
                server.serve_forever()
                try:
                    signal.pause()
                except:
                    server.shutdown()
    
    elif d[0] == socket.AF_INET6:
        print("ipv6")
        if c == 'p':
            with ProcTCPServer6((HOST, PORT), MyTCPHandler) as server:
                server.serve_forever()
                try:
                    signal.pause()
                except:
                    server.shutdown()
    
        if c == 't':
            with ThrTCPServer6((HOST, PORT), MyTCPHandler) as server:
                server.serve_forever()
                try:
                    signal.pause()
                except:
                    server.shutdown()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Comandos")
    parser.add_argument("-p","--port", type=int,required=True,help="Numero de puerto del servidor")
    parser.add_argument("-c","--concurrence", type=str ,required=True,help="P o T dependiendo de un proceso o un hilo")
    args = parser.parse_args()
    HOST, PORT = "localhost", args.port
    print("Server iniciado en: ",HOST,PORT)
    socketserver.TCPServer.allow_reuse_address = True
    direcciones = []

    direcciones = socket.getaddrinfo("localhost", 1234, socket.AF_UNSPEC,socket.SOCK_STREAM)

    hilo = []
    for d in direcciones:
        hilo.append(threading.Thread(target = servicio,args=(d,args.concurrence)))

    for h in hilo:
        h.start()
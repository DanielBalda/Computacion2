import socketserver,subprocess
import signal,os,argparse


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            if not self.data:
                server.shutdown()
                server.close_request()
                exit()
            if self.data.decode() == "stop server":
                print("ACA SE DEBERIA CERRRAR EL SERVER")
                server.shutdown()
                server.close_request()
                exit()
            pp = subprocess.Popen([self.data], stdout = subprocess.PIPE,stderr = subprocess.PIPE, shell = True)
            out,err = pp.communicate()
            if err:
                self.request.sendall(b"## ERROR ##\n"+err)
                print(err)
            else:
                self.request.sendall(b"## OK ##\n"+out)
                print(out)
            
            print("PID: %d" % os.getpid())

class ProcTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

class ThrTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Comandos")
    parser.add_argument("-p","--port", type=int,required=True,help="Puerto a trabajar")
    parser.add_argument("-c","--concurrence", type=str ,required=True,help="P o T -> P = proceso, T = Hilo")
    args = parser.parse_args()
    HOST, PORT = "localhost", args.port
    print("Server iniciado en: ",HOST," - Puerto: ",PORT)
    socketserver.TCPServer.allow_reuse_address = True

    if args.concurrence.lower() == 't':
        with ThrTCPServer((HOST, PORT), MyTCPHandler) as server:
            server.serve_forever()
            try:
                signal.pause()
            except:
                server.shutdown()

    if args.concurrence.lower() == 'p':
        with ProcTCPServer((HOST, PORT), MyTCPHandler) as server:
            server.serve_forever()
            try:
                signal.pause()
            except:
                server.shutdown()

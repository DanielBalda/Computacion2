import argparse as ap
import os, sys
import time

parser = ap.ArgumentParser(description="Inversor de texto")
parser.add_argument("-f",
                    "--file",
                    type=str,
                    required=True,
                    help="File of text")
args = parser.parse_args()

with open(args.file, 'r') as file:
   inverted = ""
   for line in file.readlines():
      r,w = os.pipe()
      pid = os.fork()
      if pid:
         os.close(w)
         r = os.fdopen(r)
         while True:
            line = r.readline()
            if line:
               inverted+=line
            else:
               os.wait()
               print(inverted)
               sys.exit(0)
      else:
         os.close(r)
         w = os.fdopen(w, 'w')
         w.write(f"{line[::-1]}")
         w.close()
         #time.sleep(.1)

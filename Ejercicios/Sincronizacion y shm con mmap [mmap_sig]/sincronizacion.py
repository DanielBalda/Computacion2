import mmap, os, argparse

def main():
    parser = argparse.ArgumentParser(description="Comandos")
    parser.add_argument("-f",
                        "--file",
                        type=str,
                        required=True,
                        help="Archivo a buscar")
    args = parser.parse_args()
    path(args.file)
    
def path(args):
    if os.path.exists(args):
        return
    else:
        os.open(args, os.O_CREAT)

if __name__ == "__main__":
    main()
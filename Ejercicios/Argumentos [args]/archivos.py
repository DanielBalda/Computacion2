import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--fileA", type=str, required=True, help="text file")
parser.add_argument("-o", "--fileB", type=str, required=True, help="text file")
args = parser.parse_args()

print('File %s.' % args.fileA)
print('File %s.' % args.fileB)

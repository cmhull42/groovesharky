import argparse,sys
import youtube_dl

parser = argparse.ArgumentParser(description="blehbleh")
parser.add_argument("files")
parser.add_argument("-o")
print sys.argv
args = parser.parse_args(sys.argv[1:])
# print args.files

print args.o
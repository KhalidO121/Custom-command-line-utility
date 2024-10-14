import argparse
import os


def number_of_bytes(file):
    print(f"  {os.path.getsize(file.name)} {file.name}")


parser = argparse.ArgumentParser()
parser.add_argument("-c", help="number of bytes in a file", action="store_true")
parser.add_argument(
    "file", help="file to be processed", type=argparse.FileType("r", encoding="utf-8")
)

args = parser.parse_args()
if args.c and args.file:
    number_of_bytes(args.file)

import argparse
import os


def number_of_bytes(file):
    print(f"  {os.path.getsize(file.name)} {file.name}")


def number_of_lines(file):
    fh = open(file.name, "r")
    file_lines = fh.readlines()
    print(f"  {len(file_lines)} {file.name}")


def number_of_words(file):
    total_words = 0
    fh = open(file.name, "r")
    file_lines = fh.readlines()
    for line in file_lines:
        total_words += len(line.split())
    print(f"  {total_words} {file.name}")


parser = argparse.ArgumentParser()
parser.add_argument("-c", help="number of bytes in a file", action="store_true")
parser.add_argument("-l", help="number of lines in a file", action="store_true")
parser.add_argument("-w", help="number of words in a file", action="store_true")
parser.add_argument(
    "file", help="file to be processed", type=argparse.FileType("r", encoding="utf-8")
)

args = parser.parse_args()
if args.c and args.file:
    number_of_bytes(args.file)
elif args.l and args.file:
    number_of_lines(args.file)
elif args.w and args.file:
    number_of_words(args.file)

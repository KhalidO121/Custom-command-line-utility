import argparse


def number_of_bytes(file):
    total_bytes = 0
    file_lines_list = file.readlines()
    for line in file_lines_list:
        total_bytes += len(line.encode("utf-8"))
    print(total_bytes)


parser = argparse.ArgumentParser()
parser.add_argument("-c", help="number of bytes in a file", action="store_true")
parser.add_argument(
    "file", help="file to be processed", type=argparse.FileType("r", encoding="utf-8")
)

args = parser.parse_args()
if args.c and args.file:
    number_of_bytes(args.file)

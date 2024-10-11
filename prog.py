import argparse


# Count the number of bytes in a file
def number_of_bytes(file):
    total_bytes = 0
    file_lines_list = file.readlines()
    for line in file_lines_list:
        total_bytes += len(line.encode("utf-8"))
    print(total_bytes)


# Sets up command line tool and arguments
parser = argparse.ArgumentParser()
parser.add_argument("-c", help="number of bytes in a file", action="store_true")
parser.add_argument(
    "file", help="file to be processed", type=argparse.FileType("r", encoding="utf-8")
)

# Capture Command line positional
args = parser.parse_args()
if args.c and args.file:
    result = number_of_bytes(args.file)

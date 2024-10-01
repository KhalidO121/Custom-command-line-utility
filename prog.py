import argparse

# This Block sets up command line tool
parser = argparse.ArgumentParser()
parser.add_argument("-c", help="number of bytes in a file", action="store_true")
parser.add_argument(
    "file", help="file to be processed", type=argparse.FileType("r", encoding="latin-1")
)

# This Block handles file positional argument
args = parser.parse_args()
file = args.file
with open(file.name, "r") as f:
    first_line = f.readline()
    print(first_line)

import argparse
import sys


def number_of_bytes(file):
    with open(file.name, "rb") as f:
        file_content = f.read()
        return len(file_content)


def number_of_lines(file):
    with open(file.name, "r") as f:
        file_lines = f.readlines()
        return len(file_lines)


def number_of_words(file):
    total_words = 0
    with open(file.name, "r") as f:
        file_lines = f.readlines()
        for line in file_lines:
            total_words += len(line.split())
        return total_words


def number_of_characters(file):
    total_characters = 0
    with open(file.name, "r") as f:
        file_lines = f.readlines()
        for line in file_lines:
            total_characters += len(line.replace("\n", "  "))
        return total_characters


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", help="number of bytes in a file", action="store_true")
    parser.add_argument("-l", help="number of lines in a file", action="store_true")
    parser.add_argument("-w", help="number of words in a file", action="store_true")
    parser.add_argument(
        "-m", help="number of characters in a file", action="store_true"
    )
    parser.add_argument(
        "file",
        nargs="?",
        help="file to be processed",
        type=argparse.FileType("r", encoding="utf-8"),
    )

    args = parser.parse_args()
    if args.c and args.file:
        print(f"  {number_of_bytes(args.file)} {args.file.name}")
    elif args.l and args.file:
        print(f"  {number_of_lines(args.file)} {args.file.name}")
    elif args.w and args.file:
        print(f"  {number_of_words(args.file)} {args.file.name}")
    elif args.m and args.file:
        print(f"  {number_of_characters(args.file)} {args.file.name}")
    elif args.file:
        print(
            f"  {number_of_lines(args.file)} {number_of_words(args.file)} {number_of_bytes(args.file)} {args.file.name}"
        )
    elif not sys.stdin.isatty():
        print(sys.stdin.read())


if __name__ == "__main__":
    main()

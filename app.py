import argparse
import sys

from helpers.helpers import (
    number_of_bytes,
    number_of_characters,
    number_of_lines,
    number_of_words,
)


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
    # print(args)
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

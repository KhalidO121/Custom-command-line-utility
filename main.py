import argparse
import sys

from helpers import (
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
        type=str,
    )
    parser.add_argument("PARAMS", nargs="*")

    args = parser.parse_args()
    if not args.file:
        print("error")
    if not sys.stdin.isatty():
        args.PARAMS.extend(sys.stdin.read().splitlines())
    texts = None
    try:
        with open(args.file, "r") as fh:
            texts = fh.read()
    except Exception:
        texts = args.PARAMS
    if args.c:
        print(f"  {number_of_bytes(texts)} {args.file.name}")
    elif args.l:
        print(f"  {number_of_lines(args.file)} {args.file.name}")
    elif args.w:
        print(f"  {number_of_words(args.file)} {args.file.name}")
    elif args.m:
        print(f"  {number_of_characters(args.file)} {args.file.name}")
    elif args.file:
        print(
            f"  {number_of_lines(args.file)} {number_of_words(args.file)} {number_of_bytes(args.file)} {args.file.name}"
        )


if __name__ == "__main__":
    # main()
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file",
        nargs="?",
        help="file to be processed",
        # type=argparse.FileType("r", encoding="utf-8"),
        type=str,
    )
    parser.add_argument("PARAMS", nargs="*")
    args = parser.parse_args()
    if not sys.stdin.isatty():
        args.PARAMS.extend(sys.stdin.read().splitlines())
    print(args)
    texts = None
    try:
        with open(args.file, "r") as fh:
            texts = fh.read()
    except Exception:
        texts = args.PARAMS
    print(texts)

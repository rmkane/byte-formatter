#!/usr/bin/env python3
import argparse

from byte_formatter.formatter import format_size


def _parse_args():
    parser = argparse.ArgumentParser(
        description="Convert a file size to a human-readable format.")
    parser.add_argument("size", type=int, help="The file size in bytes.")
    parser.add_argument(
        "-b",
        "--binary",
        action="store_true",
        help="Use binary (base-1024) units (KiB, MiB, etc.).",
    )
    parser.add_argument(
        "-p",
        "--precision",
        type=int,
        default=1,
        help="The number of decimal places to include in the formatted size.",
    )
    parser.add_argument(
        "-s",
        "--suffix",
        type=str,
        default="",
        help="A suffix to append to the formatted size string.",
    )
    parser.add_argument(
        "-t",
        "--strip-trailing-zeros",
        action="store_true",
        help="Strip trailing zeros from the formatted size.",
    )
    parser.add_argument(
        "-S",
        "--si-units",
        action="store_true",
        help=("Use SI units (kB, MB, etc.) which are also base-1000 but with"
              " different symbols."),
    )
    parser.add_argument(
        "-U",
        "--uppercase-units",
        action="store_true",
        help=(
            "Use uppercase unit symbols (KB, MB). Default if neither -U nor -l"
            " is set."),
    )
    parser.add_argument(
        "-l",
        "--lowercase-units",
        action="store_true",
        help="Use lowercase unit symbols (kb, mb). Overrides -U.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Use verbose unit names (Bytes, Kilobytes, etc.).",
    )
    parser.add_argument(
        "-x",
        "--unix-style",
        action="store_true",
        help="Use single-letter Unix-style unit names (B, K, M, G, T, P).",
    )

    return parser.parse_args()


def main():
    args = _parse_args()

    # Determine whether to use uppercase or lowercase units
    uppercase_units = not args.lowercase_units

    formatted_size = format_size(
        size=args.size,
        binary=args.binary,
        precision=args.precision,
        suffix=args.suffix,
        strip_trailing_zeros=args.strip_trailing_zeros,
        si_units=args.si_units,
        uppercase_units=uppercase_units,
        verbose=args.verbose,
        unix_style=args.unix_style,
    )

    print(formatted_size)


if __name__ == "__main__":
    main()

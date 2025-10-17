import argparse
from app.pricing import calculate_discount
from app.strings import concat_strings
from app.utils import build_grep_command


def main() -> None:
    parser = argparse.ArgumentParser(description="Sample app CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_discount = subparsers.add_parser("discount", help="Calculate discounted price")
    p_discount.add_argument("price", type=float)
    p_discount.add_argument("percent", type=float)

    p_concat = subparsers.add_parser("concat", help="Concatenate strings")
    p_concat.add_argument("items", nargs=argparse.REMAINDER)

    p_grep = subparsers.add_parser("grep-cmd", help="Build grep command")
    p_grep.add_argument("query", type=str)

    args = parser.parse_args()

    if args.command == "discount":
        print(calculate_discount(args.price, args.percent))
    elif args.command == "concat":
        print(concat_strings(args.items))
    elif args.command == "grep-cmd":
        print(build_grep_command(args.query))


if __name__ == "__main__":
    main()

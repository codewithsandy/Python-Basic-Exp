import argparse
import sys

def calc(args):
    if args.o=='add':
        return args.x + args.y
    if args.o=='mul':
        return args.x * args.y
    if args.o=='sub':
        return args.x - args.y
    if args.o=='div':
        return args.x / args.y
    else:
        return "Something Wrong"
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0, help="Enter First Number........This is utility for calculations.....plz contact sandy........")
    parser.add_argument('--y', type=float, default=1.0, help="Enter First Number........This is utility for calculations.....plz contact sandy........")
    parser.add_argument('--o', type=float, default="add", help="........This is utility for calculations.....plz contact sandy........")
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

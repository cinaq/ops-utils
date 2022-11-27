#!/usr/bin/env python3
from datetime import datetime
import argparse
import fileinput

description = """
Accepts a list of ISO timestamps via STDIN and prints the delta between each timestamp. 
 
Example: 
 
echo \"2022-11-26 16:54:30.313\\n2022-11-26 16:54:30.321\" | ./delta-iso-timestamps.py

"""

def print_summary(deltas):
    print("# == Summary ==")
    print("# Count", len(deltas))
    print("# Min", min(deltas), "ms")
    print("# Average", sum(deltas) / len(deltas), "ms")
    print("# Max", max(deltas), "ms")
    print("# Total", sum(deltas), "ms")

def main(args):
    previous = None
    deltas = []

    for line in fileinput.input(files=args.files):
        try:
            current = datetime.fromisoformat(line.strip())
        except ValueError as e:
            print(e)
            continue
        if not previous:
            previous = current
            continue
        delta_ms = (current - previous).microseconds / 1000
        deltas.append(delta_ms)
        print(previous, current, delta_ms)
        previous = current

    if args.summary:
        print_summary(deltas)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument('files', metavar='FILE', nargs='*', help='files to read, if empty, stdin is used')
    parser.add_argument('--summary', action='store_true')
    parser.add_argument('--no-summary', dest='summary', action='store_false')
    parser.set_defaults(feature=True)
    args = parser.parse_args()
    main(args)

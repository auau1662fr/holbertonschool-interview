#!/usr/bin/python3
import sys

total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

line_count = 0


def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))


try:
    for line in sys.stdin:
        line_count += 1

        try:
            parts = line.split()
            status = parts[-2]
            size = int(parts[-1])

            total_size += size

            if status in status_codes:
                status_codes[status] += 1
        except (IndexError, ValueError):
            pass

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()

#!/usr/bin/python3
import sys

total_size = 0
line_count = 0
status_codes = {}

valid_codes = ['200', '301', '400', '401',
               '403', '404', '405', '500']


def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


try:
    for line in sys.stdin:
        line_count += 1

        try:
            parts = line.split()

            status = parts[-2]
            size = int(parts[-1])

            total_size += size

            if status in valid_codes:
                status_codes[status] = (
                    status_codes.get(status, 0) + 1
                )

        except (ValueError, IndexError):
            pass

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    raise

print_stats()

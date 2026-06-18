#!/usr/bin/python3
"""Module for log parsing"""
import sys
import re


def print_stats(total_size, status_codes):
    """Print the statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    total_size = 0
    status_codes = {}
    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    line_count = 0
    pattern = (r'^\S+ - \[.+\] "GET /projects/260 HTTP/1\.1" '
               r'(\d+) (\d+)$')

    try:
        for line in sys.stdin:
            line = line.strip()
            match = re.match(pattern, line)

            if not match:
                continue

            status_code = match.group(1)
            file_size = int(match.group(2))

            total_size += file_size
            if status_code in valid_codes:
                status_codes[status_code] = status_codes.get(
                    status_code, 0) + 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)

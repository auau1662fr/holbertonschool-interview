#!/usr/bin/python3
"""Module for log parsing"""
import sys


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

    try:
        for line in sys.stdin:
            line = line.strip()
            parts = line.split()

            if len(parts) < 7:
                continue

            try:
                status_code = parts[-2]
                file_size = int(parts[-1])
            except (ValueError, IndexError):
                continue

            if (parts[5] != '"GET' or parts[6] != "/projects/260"
                    or parts[7] != 'HTTP/1.1"'):
                continue

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

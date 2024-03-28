#!/usr/bin/python3
import sys
import re
import signal

# Initialize variables
total_size = 0
status_counts = {}
line_count = 0


# Function to handle keyboard interruptions
def signal_handler(sig, frame):
    print_statistics()
    sys.exit(0)


# Function to print statistics
def print_statistics():
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin
for line in sys.stdin:
    line_count += 1
    # Parse the line
    match = re.match(
            r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.+)\] "GET /projects/260 HTTP/1.1" '
            r'(\d{3}) (\d+)',
            line.strip()
            )
    if match:
        total_size += int(match.group(4))
        status_code = int(match.group(3))
        if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
            if status_code not in status_counts:
                status_counts[status_code] = 0
            status_counts[status_code] += 1
    # Print statistics after every 10 lines
    if line_count % 10 == 0:
        print_statistics()

# Ensure the script prints statistics on exit
print_statistics()

#!/usr/bin/env python3
"""
Simple log parsing helper: filter log lines by level.
"""

import sys, re

def parse_log(file_path, level=None):
    """Yield lines from file matching an optional level."""
    pattern = re.compile(r'^\[(?P<lvl>\w+)\]')
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            m = pattern.match(line)
            if m and (level is None or m.group('lvl').upper() == level.upper()):
                yield line.rstrip('\n')

def main():
    if len(sys.argv) < 2:
        print("Usage: python log_helper.py <file> [-s LEVEL]")
        sys.exit(1)
    file_path = sys.argv[1]
    level = None
    if len(sys.argv) >= 4 and sys.argv[2] == '-s':
        level = sys.argv[3]
    for line in parse_log(file_path, level):
        print(line)

if __name__ == "__main__":
    main()
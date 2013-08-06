#!/usr/bin/env python

"""
csv_filter: filter a csv file by one or more other csv files

@author: mitzip
@contact: http://github.com/mitzip/csv_filter
@license: Public Domain
@version: 1.0
@todo: add argument to toggle case-sensitivity
"""

import sys
import csv
import argparse

# Define accepted command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--filter', type=file, required=True,
                    help='CSV file to be filtered')
parser.add_argument('--by', type=file, required=True, action='append',
                    help='CSV file to filter by')
parser.add_argument('--output', nargs='?',
                    type=argparse.FileType('w'), default=sys.stdout,
                    help='Filtered output CSV filename, omit for stdout')
parser.add_argument('--filter-col', default=3, type=int,
                    help='Column in CSV to filter to match, default 3')
parser.add_argument('--by-col', default=0, type=int,
                    help='Column in CSV to filter by to match, default 0')
args = parser.parse_args()

# Open CSV file to be filtered read-only
filter_csv = csv.reader(args.filter)

# Open output CSV file as writable, or stdout
filtered_csv = csv.writer(args.output)

# Open each CSV file to filter by read-only and add to a unique
# set of field values for rows you do NOT want in filtered output.
to_remove = set()
for by_file in args.by:
    by_csv = csv.reader(by_file)
    next(by_csv)
    to_remove.update({row[args.by_col].lower() for row in by_csv if row})

# Check each row in CSV you want filtered for field values in to_remove set
for row in filter_csv:
    if row and row[args.filter_col].lower() not in to_remove:
        filtered_csv.writerow(row)

# CSV Filter

CSV Filter was written to remove rows from a CSV file that have fields in common with 1 or more other CSV files.

# Syntax Example

	csv_filter --filter newsletter_subscribers.csv --filter-col 3 --by newsletter_opt-outs.csv --by newsletter_bounces.csv --by-col 0 --output newsletter_subscribers_current.csv

## Description

The syntax example will make a unique list (a set) of all values of column 0 (the first column) from each row in each file specified with "--by". 
If the column value, specified in the "--filter-col" argument, in any row in the "filter file" matches any value in the "by" list, the row will be removed.

# License

csv_filter is free software released to the public domain. For more information, please refer to <http://unlicense.org/>

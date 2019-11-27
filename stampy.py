"""A simple script for generating a timestamp of the current time."""

import argparse
import datetime


parser = argparse.ArgumentParser()
parser.add_argument(
    "format", 
    help="An optional string using  strftime-compatible formatting characters", 
    nargs="?"
)

args = parser.parse_args()

if args.format is not None:
    fmt = args.format
else:
    fmt = "%Y%m%d%H%M%S"

print(datetime.datetime.now().strftime(fmt))
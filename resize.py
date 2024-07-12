#!/usr/bin/env python3
import re
import subprocess
import sys

if len(sys.argv) < 4:
    print("Too few arguments.")
    exit(1)

original_remarks_filename = sys.argv[1]
resized_remarks_filename = sys.argv[2]
papersize_filename = sys.argv[3]

with open(papersize_filename) as f:
    papersize = f.readlines()[0].rstrip("\n")

pdfjam_cmdline = [
    "pdfjam",
    "--no-tidy",
    "--outfile", resized_remarks_filename,
    "--papersize", papersize,
    original_remarks_filename]

output = subprocess.check_call(pdfjam_cmdline)

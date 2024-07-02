#!/usr/bin/env python3
import re
import subprocess
import sys

if len(sys.argv) < 3:
    print("Too few arguments.")
    exit(1)

original_pdf_filename = sys.argv[1]
tsv_filename = sys.argv[2]

with open(tsv_filename) as f:
    first = True
    for newline in iter(f.readline, ""):
        if first:
            first = False
            continue
        line = newline.rstrip("\r\n")
        items = line.split("\t")
        result_filename = items[14]
        start_page_physical = int(items[26])
        end_page_physical = int(items[27])

        cmdline = [
            "pdftk",
            "A={}".format(original_pdf_filename),
            "cat",
            "A{}-{}".format(start_page_physical, end_page_physical),
            "output",
            result_filename]
        print(cmdline)
        output = subprocess.check_output(cmdline)

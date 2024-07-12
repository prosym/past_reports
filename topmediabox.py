#!/usr/bin/env python3
from pypdf import PdfReader
import sys

if len(sys.argv) < 2:
    print("Too few arguments.")
    exit(1)

original_pdf_filename = sys.argv[1]

reader = PdfReader(original_pdf_filename)
# print("{} page(s)".format(len(reader.pages)))

sizes = {}
for page in reader.pages:
    box = page.mediabox
    size = "{{{}pt,{}pt}}".format(box.width, box.height)
    if size in sizes:
        sizes[size] = sizes[size] + 1
    else:
        sizes[size] = 1

print(sorted(sizes.items(), key=lambda x:x[1], reverse=True)[0][0])

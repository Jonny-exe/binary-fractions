#!/usr/bin/python3
import re

file = open("binary_fractions/binary.py", "r").read()
m = re.search(r'"""[\s\S]*?"""', file)
if m.group(0) != "":
    new_file = open("README.md", "w")
    new_file.write(m.group(0).strip('"'))
    print("New README.md was generated.")
else:
    print("FAILED: No new README.md was generated.")

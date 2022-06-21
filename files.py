

import argparse as ap

parser = ap.ArgumentParser()

parser.add_argument("--file", required=True)

arguments = parser.parse_args()


file = open(arguments.file, "r") 

for y in file:
    print(y)

file.close()

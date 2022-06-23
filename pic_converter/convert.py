
import argparse
import glob
import os
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument("--input", help = "input folder", required = True)
parser.add_argument("--output", help = "output folder", required = True)
arguments = parser.parse_args()

input_files = glob.glob(arguments.input + '/*.jpg')
output_folder = arguments.output

if_folder_exists = os.path.exists(output_folder)

if not if_folder_exists:
    os.makedirs(output_folder)

print("Your input folder: ", input_files)

for file in input_files:
    f = Image.open(file).convert('L')
    f.save(output_folder + "/grey_" + os.path.basename(file))


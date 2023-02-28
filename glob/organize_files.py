import glob
import os

os.chdir("./glob exercise files")

all_card_files = glob.glob("*card*.py")
all_color_files = glob.glob("*colour*.py")

all_card_files.extend(glob.glob("*q1*.py"))
all_color_files.extend(glob.glob("*q2*.py"))

print(all_card_files)
print(all_color_files)
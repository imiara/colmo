import colmo
import sys
import os

if len(sys.argv) >= 2:
    dir = sys.argv[1]
else:
    dir = r''

if len(sys.argv) >= 3:
    base_file = sys.argv[2]
else:
    base_file = 'base.txt'

if len(sys.argv) >= 4:
    in_pattern = sys.argv[3]
else:
    in_pattern = '*.NEW'

if len(sys.argv) >= 5:
    outfile = sys.argv[4]
else:
    outfile = 'NEW_PRICE_LIST.txt'

colmo.read_write(dir, base_file, in_pattern, outfile)

os.system("pause")

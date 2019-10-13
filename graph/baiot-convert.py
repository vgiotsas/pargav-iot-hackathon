#!/usr/bin/env python3

import re
import csv
import sys
from datetime import datetime

start_ts = 1500875430


def convert():
    i = 0
    ts = start_ts
    reader = csv.reader(sys.stdin)
    bwup = conn = connport = 0
    for csvline in reader:
        if i == 0:
            i += 1
            continue # skip header
        try:
            bwup += float(csvline[15])
            conn += float(csvline[30])
            connport += float(csvline[80])
        except:
            #l = len(csvline)
            #print(f"Error on line {i+1}: {l}")
            pass
        if i%120 == 0:
            print( f"{ts},{bwup},0,{conn},{conn/connport},0")
            bwup = conn = connport = 0
            ts += 60
        i += 1


if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(convert())


#!/usr/bin/env python3

import random

start_ts = 1500875430
ts_increment = 60
data_points = 1000
bw_up_base = random.randint(0, 100)
bw_dn_base = random.randint(0, 1000)

i = 0
for ts in range(start_ts, start_ts+data_points*ts_increment, ts_increment):
    bw_up = bw_up_base + random.randint(0, 10)
    bw_dn = bw_dn_base + random.randint(0, 100)
    conns = random.randint(0, 10)
    ips = random.randint(0, 10)
    ports = random.randint(0, 10)
    if 500 < i < 515 or 600<i<615:
        bw_up += 200
        bw_dn += 300
    print( f"{ts},{bw_up},{bw_dn},{conns},{ports},{ips}" )
    i = i+1

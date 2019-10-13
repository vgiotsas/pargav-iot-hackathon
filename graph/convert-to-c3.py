#!/usr/bin/env python3

import argparse
import csv
import re
import sys
from datetime import datetime

ts_every = 1
timefmt = '%Y-%m-%d %H:%M'

xs = ['x']
bw_ups = ['bwup']
bw_dns = ['bwdn']
conns = ['conns']
targets = ['targets']
ports = ['ports']


def convert():
    parser = argparse.ArgumentParser()
    parser.add_argument("out")
    args = parser.parse_args()

    i = 0
    reader = csv.reader(sys.stdin)
    for (ts, bw_up, bw_dn, conn, target, port) in reader:
        try:
            if i%ts_every == 0:
                xs.append(datetime.utcfromtimestamp(int(ts)).strftime(timefmt))
            else:
                xs.append('')
            bw_ups.append(float(bw_up))
            bw_dns.append(float(bw_dn))
            conns.append(float(conn))
            targets.append(float(target))
            ports.append(float(port))
        except:
            pass
        i += 1

    make_output(args.out+'-bw.js', chart='chart_bw_'+args.out, data1=bw_ups, data2=bw_dns)
    make_output(args.out+'-conn.js', chart='chart_conn_'+args.out, data1=conns)
    make_output(args.out+'-target.js', chart='chart_target_'+args.out, data1=targets)
    make_output(args.out+'-port.js', chart='chart_port_'+args.out, data1=ports)


def make_output(filename, data1, data2=None, chart='chart'):
    with open(filename, 'w') as out:
        print("var %s = c3.generate({ bindto: '#%s', data: { x: 'x', xFormat: '%s', columns: [" % (chart, chart, timefmt), file=out)
        print(f"{xs},", file=out)
        if data2:
            print(f"{data1},", file=out)
            print(f"{data2}", file=out)
        else:
            print(f"{data1}", file=out)
        print("] }, axis: { x: { type: 'timeseries', tick: { format: '%s' } } } } );" % timefmt, file=out)


if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(convert())


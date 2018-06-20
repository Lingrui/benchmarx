#!/usr/bin/env python3
import os
import sys
import subprocess as sp

if len(sys.argv) != 2:
    print("Usage: %s result_file" % sys.argv[0])
    sys.exit(0)

result_file = sys.argv[1]

ROOT = os.path.abspath(os.path.dirname(__file__))

kapp = os.path.abspath(os.path.join(ROOT, 'kapp.pl'))

gt = os.path.abspath(os.path.join(ROOT, '../data/mura/train_labeled_studies.csv'))

lookup = {}
with open(gt, 'r') as f:
    for l in f:
        k, v = l.strip().split(',')
        lookup[k] = v

C = 0
with open(result_file, 'r') as f, \
    open('temp_gt', 'w') as of:
    for l in f:
        k, v = l.strip().split(',')
        assert k in lookup
        of.write('%s,%s\n' % (k, lookup[k]))
        C += 1
        pass
    pass

print('evaluating %s lines' % C)
sp.check_call('%s temp_gt %s' % (kapp, result_file), shell=True)

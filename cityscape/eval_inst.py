#!/usr/bin/env python3
import os
import sys
import subprocess as sp

if len(sys.argv) != 2:
    print("Usage: %s result_dir" % sys.argv[0])
    sys.exit(0)

result_dir = sys.argv[1]

if not os.path.isdir(os.path.join(result_dir, 'data')):
    print("Submission files should be in 'data' under result_dir.")
    sys.exit(0)


ROOT = os.path.abspath(os.path.dirname(__file__))

eval_bin = os.path.abspath(os.path.join(ROOT, '../3rd/cityscapeScripts/cityscapescripts/evaluation/evalInstanceLevelSemanticLabeling.py'))

gt_dir = os.path.abspath(os.path.join(ROOT, '../data/cityscape/'))


sp.check_call('%s %s %s' % (eval_bin, gt_dir, result_dir), shell=True)


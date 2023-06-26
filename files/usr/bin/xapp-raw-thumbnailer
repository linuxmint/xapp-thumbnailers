#!/usr/bin/python3

import os
import subprocess
import sys

import XappThumbnailers
t = XappThumbnailers.Thumbnailer()

try:
    output = subprocess.check_output([
            'dcraw', '-c', '-e', '-w', t.args.input,
        ])
except subprocess.CalledProcessError as e:
    print(e)
    sys.exit(1)

t.save_bytes(output)
sys.exit(0)

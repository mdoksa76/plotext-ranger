#! /usr/bin/python3

import plotext as plt
import sys
import os

path=sys.argv[1]

plt.play_gif(path)
os.system("""bash -c 'read -s -n 1 -p "Press any key to continue..."'""")

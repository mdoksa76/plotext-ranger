#! /usr/bin/python3

import plotext as plt
import sys
import os
import time

path=sys.argv[1]

plt.image_plot(path)
plt.show()
os.system("""bash -c 'read -s -n 1 -p "Press any key to continue..."'""")

# plotext-ranger
Plotext usage in ranger file manager for viewing graphics files.

Python scripts plotext-ranger-img.py and plotext-ranger-gif.py .py are python scripts for showing graphics files in ranger file manager. They depend on python module plotext.

Install plotext with:
  "pip install plotext" or
  "pip3 install plotext"
  
Put python scripts in some map and export path of that map.
  
Add ranger config file rifle.conf to ~/.config/ranger/rifle.conf

Why I did this?
I have Orange Pi Zero with only 2 GB micro sd card. There is not possible to have desktop environment so I needed something for .jpg, .png and .gif.
I used asciiview and cacaview and than I found piccolomo/plotext repository. In many cases plotext is better solution for terminal view of graphics files.

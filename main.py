#!/usr/bin/python3
import envsetup as point
import tkinter as tk
import time
import os
import sys

### Start Init Proccess ###
print("PointService RC.2 Ver.1 Rev.rpi3-raspad0")
global root
root = tk.Tk()
root.title("PointService Rc.2 Ver.1 Rev.rpi3-raspad0")

### Main Proccess ###
point.asknumber()
# if not Valid == True:
#     time.sleep(10)
#     exit()

# point.numbervalidcheck()
# if not Valid == True:
#     time.sleep(10)
#     exit()
point.pwcheck()
point.record()
root.mainloop()

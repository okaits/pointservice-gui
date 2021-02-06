#!/usr/bin/python3

### Start Config ###

global os
global sys
global time
global tkinter

import os
import sys
import time
import tkinter as tk

def loadingmessage(sltime):
    LoadMessage = tk.Label(text=u'loading...')
    LoadMessage.pack()
    time.sleep(sltime)
    LoadMessage.destroy()

def readnumberbox(self):
    global num
    num = str(NumberBox.get())
 #   global Valid
 #   if not num.isdigit() == True:
 #       print("Not number.")
 #       Valid=False
 #   elif num.isdigit() == True:
 #       print("Valid.")
 #       return num
 #       Valid=True

def readlptsbox(self):
    global lpts
    if not "pwboxfin" in globals():
        print("No.")
        exit()
    lpts = str(LPTSBox.get())
    os.environ["SEND"] = num
    os.environ["SEND1"] = lpts
    os.system("/bin/bash -c " + os.environ["HOME"] + "/PointService-rc2/rec.sh")
    exit()

def readpasswordbox(self):
    pw = str(PassWordBox.get())
    global pwboxfin
    if not pw == "School2020":
        print("No.")
        exit()
    pwboxfin=True

def asknumber():
    NumberInfoLabel = tk.Label(text=u'Insert Number')
    global NumberBox
    NumberBox = tk.Entry()
    AcceptButton = tk.Button(text=u'Next')
    AcceptButton.bind("<Button-1>",readnumberbox)
    NumberInfoLabel.pack()
    NumberBox.pack()
    AcceptButton.pack()

#def numbervalidcheck():
#    loadingmessage(0.1)
#    if int(num) < int(37):
#        print("Valid.")
#        Valid=True
#    else:
#        print("Not valid.")
#        Valid=False

def pwcheck():
    PassWordInfoLabel = tk.Label(text=u'Insert Password')
    global PassWordBox
    PassWordBox = tk.Entry()
    PassWordAcceptButton = tk.Button(text=u'Confirm')
    PassWordAcceptButton.bind("<Button-1>",readpasswordbox)
    PassWordInfoLabel.pack()
    PassWordBox.pack()
    PassWordAcceptButton.pack()

def record(): # Need: /home/pi/PointService-rc2/rec.sh (P:$HOME/PointService-rc2/rec.sh) (R: record) (B: False(none))
    loadingmessage(3)
    LPTSInfoLabel = tk.Label(text=u'Insert Loss Points')
    global LPTSBox
    LPTSBox = tk.Entry()
    LPTSButton = tk.Button(text=u'Proccess')
    LPTSButton.bind("<Button-1>",readlptsbox)
    LPTSInfoLabel.pack()
    LPTSBox.pack()
    LPTSButton.pack()

def recordvoice():
   loadingmessage(5)
   print("Disabled.")

### End Config ###

#!/usr/bin/env python3

import sys
import os

sys.path.insert(1, os.getcwd() + '/lib/')

from shared import *
from end import *
from start import *

ENCRYPTED = 'encrypted'
PLAINTEXT = 'plaintext'
CWD = os.getcwd()

try:
    if(exists(CWD + '/' + ENCRYPTED)):
        print("Exists encrypted")
        start(PLAINTEXT)
    elif(exists(CWD + '/' + PLAINTEXT)):
        print("Exists plain")
        if(len(open(CWD + '/' + PLAINTEXT).readlines()) <= 0):
                print("Empty file...")
                print("Exiting...")
                exit()
        end(PLAINTEXT)
    else:
        print("No plaintext file")
        print("No encrypted file")
        print("Creating empty plaintext file...")
        os.system('touch plaintext')
        print("Your journal is ready for writing")
except KeyboardInterrupt as e:
	print("\nExiting...")


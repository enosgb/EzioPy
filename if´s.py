from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import tkinter as tk
import os


if(os.popen('quser '+'073933'+' /server:rdsh1.unifeso.lan')):
    print('teste true')
else:
    print('teste false')
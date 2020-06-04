#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  guihangman.py
#  
#  Copyright 2020 kevinnls <kevin.nl.samuel@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from tkinter import *
import json
from stick import stickman as stickman
from string import ascii_lowercase as letters
from random import choice
from clear import *
from hangman import *

window = Tk()
window.geometry('1080x720')
top = LabelFrame().pack()
Label(top,text = "Hangman",anchor="nw").pack()
Label(top,text = "wins:").pack()
wins = StringVar()
wins = '0'
v = Label(top, textvariable=wins).pack()
Label(top,text = "losses:").pack()
l = Label(top, text = "0").pack()
#l['text']=5

window.mainloop()

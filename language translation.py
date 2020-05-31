# -*- coding: utf-8 -*-
"""
Created on Sun May 31 14:17:16 2020

@author: Aaditree Jaisswal
"""

import goslate

text = input()

gs = goslate.Goslate()

list = input("Choose Language :")
translatedText = gs.translate(text,list)

print(translatedText)
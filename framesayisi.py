import os
from re import S
import cv2
import glob
import numpy as np
from moviepy.editor import *
import time
import pandas as pd
import pickle

fn='C:/Users/DELL/Desktop/Ornek/output6.avi'
cap = cv2.VideoCapture(fn)

if not cap.isOpened(): 
    print("could not open :",fn)
    exit
    
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv2.CAP_PROP_FPS)

print("Length is ",length," Widht and Height (",width,",",height,") FPS ",fps)

cap = cv2.VideoCapture(fn)
property_id = int(cv2.CAP_PROP_FRAME_COUNT) 
length = int(cv2.VideoCapture.get(cap, property_id))
print( length )

objects = []
with (open("renk.pickle", "rb")) as openfile:
    while True:
        try:
            objects.append(pickle.load(openfile))
        except EOFError:
            break


print(objects)   
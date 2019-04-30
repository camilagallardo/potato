import sys
import pygame
import time
import math

def new_speed (score):
    initial_speed, factor = -6, 0
    if 0 <= score < 100:
        factor = 0
    elif 100 <= score < 1000:
        factor = 0.05
    else:
        factor = 0.1
    return initial_speed - factor





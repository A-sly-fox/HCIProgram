import numpy as np

MIN_CYCLE_NUM = 5
OFFSET_NUM = 0

# TODO: give a legal init f
f_init = [   8,  2, 19, 22,  0, 24, 18, 17,  4, 13,
             7, 16,  9, 14, 23,  5,  6, 20, 11, 10, 
             3, 25, 15, 12,  1, 21
         ]    

# KeyGroup divides keys into 5 groups and record their indexes
# LetterGroup shows the letters in each groups
KeyGroup = [    [ 0,  4,  8, 13, 17], 
                [ 9, 10, 16, 20, 21], 
                [ 5,  6, 12, 14, 18, 24], 
                [ 1,  2,  3, 23], 
                [ 7, 11, 15, 19, 22, 25]]
LetterGroup = [ [ 8,  0,  4, 14, 20], 
                [13,  7,  6,  3, 25], 
                [24, 18,  9, 23, 11, 1], 
                [ 2, 19, 22, 12], 
                [17, 16,  5, 10, 15, 21]]
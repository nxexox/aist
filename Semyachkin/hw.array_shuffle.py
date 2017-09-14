#!/usr/bin/python
import random

arr = range(50,70)
shuffle = []


while len(shuffle) != len(arr):
  item = arr[random.randint(0, len(arr) - 1)]

  if item not in shuffle:
    if len(shuffle) == 0:
        shuffle.append(item)

    elif shuffle[-1] > item:
        shuffle.append(item)
    
print(shuffle)



class Test(object):
    pass
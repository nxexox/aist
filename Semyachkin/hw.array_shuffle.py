#!/usr/bin/python
import random

arr = range(50,70)
shuffle = []


while len(shuffle) != len(arr):
  item = arr[random.randint(0, len(arr) - 1)]

  if item not in shuffle:
    shuffle.append(item)

print(shuffle)
#!/usr/bin/python
import random

arr = range(20, 0, -1)
random.shuffle(arr)
length = len(arr)

def heapify(length, index):
  left = 2 * index
  right = 2 * index + 1
  largest = index

  if left <= length and arr[left] > arr[largest]:
    largest = left

  if right <= length and arr[right] > arr[largest]:
    largest = right

  if largest != index:
    tmp = arr[index]
    arr[index] = arr[largest]
    arr[largest] = tmp

    heapify(length, largest)

for i in range((length >> 1) + 1)[::-1]:
  heapify(length - 1, i)

for i in range(length - 1, 0, -1):
  tmp = arr[0]
  arr[0] = arr[i]
  arr[i] = tmp
  length -= 1
  
  heapify(length - 1, 0)

print arr
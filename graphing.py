import re
# Testing out numpy
# import numpy as np

# a = np.array([[1,2,3],[4,5,6]])
# print(a)
# print(a.shape)

# Actually gathering the data
path = './data.csv'
file = open(file=path,mode='r')
num = 0
for line in file:
    # Only need the numbered data here instead of title information
    if re.findall('^[0-9]',line):
        print(type(line))
        print(line)
        # raw_info = line.split(',')
        # print(type(raw_info))
        # print(raw_info)
        num += 1
print(f'Found {num} lines of information.')

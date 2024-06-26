# Might need these later on
# import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Testing out numpy
# a = np.array([[1,2,3],[4,5,6]])
# print(a)
# print(a.shape)

# Grabbing the data from csv file
# info = pd.read_csv('data.csv', header=4)
data = pd.read_csv('data.csv', header=4).values
print(type(data))
print(data)

# Figuring out what each of the information means:
# Date
# data[r][0] = Date in YYYYMM.0 format for r
print(type(data[0][0]))
print(data[0][0])
# This will result the format to be YYYY.MM for each r
# could help split it out year and month from each other to label the x axis for dates.
print(data[0][0]/100)
# Anomaly Temperature
# data[r][1] = Anomaly Temperature in Celcius at the date in r
print(type(data[0][1]))
print(data[0][1])

# Testing out Pandas DataFrame class
df = pd.DataFrame(data)
print(type(df))
print(df)
# df[c][r]
print(type(df[0][0]))
print(df[0][0],df[1][0])

# Testing out Matplotlib
x = np.linspace(0,2*np.pi,100)
y = np.cos(x)

fig,ax = plt.subplots()
ax.plot(x,y,color='blue')

plt.show()

# Gathering the data - OLD - Need below to help figure out how to make a hash to save the data
# path = './data.csv'
# file = open(file=path,mode='r')
# data = []
# # num = 0
# for line in file:
#     # Only need the numbered data here instead of title information
#     if re.findall('^[0-9]',line):
#         # print(type(line))
#         # print(line)
#         raw_info = line.split(',')
#         # print(raw_info)
#         info = {}
#         # date is formated as YYYYMM
#         info['date'] = int(raw_info[0])
#         # anomaly temperature in Celcius
#         anomaly_raw = raw_info[1].split('\n')
#         info['anomaly_temp'] = float(anomaly_raw[0])
#         # print(info)
#         # print(f'Fahrenheit Temperature Anomaly = {(info["anomaly_temp"]*(9/5))+32}')
#         # num += 1
#         data.append(info)
# # print(f'Found {num} lines of information.')
# print(data)
# Calculation from Celcius to Fahrenheit is:
# F = (C * (9/5)) + 32

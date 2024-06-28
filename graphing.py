# Might need these later on
# import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# try:
#     temp_data = np.load('temp_data.npy')
# except:
#     temp_data = None

# Grabbing the data from csv file
data = pd.read_csv('data.csv', header=4).values
# print(type(data))
# print(data)

# Figuring out what each of the information means:
# The size and shape of the array
# print(f'Shape of data = {data.shape}')
# print(f'Number of data information = {data.size}')
# print(f'Number of data points = {data.shape[0]}')
# Date
# print(type(data[0][0]))
# print(f'Date in YYYYMM.0 format = {data[0][0]}')
# print(f'Date in YYYY.MM format = {data[0][0]/100}')
# Anomaly Temperature
# print(type(data[0][1]))
# print(f'Anomaly Temperature in Celcius = {data[0][1]}')
# print(f'Anomaly Temperature in Fahrenheit = {(data[0][1]*(9/5))+32}')

# Testing out Pandas DataFrame class
# df = pd.DataFrame(data)
# print(type(df))
# print(df)
# # df[c][r]
# print(type(df[0][0]))
# print(df[0][0],df[1][0])

# Setting up axis to graph
x = np.empty(data.shape[0])
y = np.empty(data.shape[0])

for i in range(data.shape[0]):
    x[i] = data[i][0]
    y[i] = data[i][1]

# print(x)
# print(y)

# Graphing
plt.style.use('bmh')
fig,ax = plt.subplots()
# ax.plot(x,y,color='blue')
ax.scatter(x,y,s=15,color='black')
ax.set_title('Global Temperature', fontsize=24)
ax.set_xlabel('Date (YYYYMM)', fontsize=12)
ax.set_ylabel('Anomaly Temperature in Celcius', fontsize=12)

# Specific points - Add in more mathematical calulations than these:
# Cold average?
ax.axhline(y=-0.5, color='blue')
# Warm average?
ax.axhline(y=0.5, color='red')
# 1979 is when it starts to appear with global warming
ax.axvline(x=197900, color='green')

plt.show()
# plt.savefig('global_temperature.png')

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

# np.save('temp_data',data)

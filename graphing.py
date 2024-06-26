import re
# Testing out numpy
# import numpy as np

# a = np.array([[1,2,3],[4,5,6]])
# print(a)
# print(a.shape)
# Testing out pandas
import pandas as pd

# info = pd.read_csv('data.csv', header=4)
info = pd.read_csv('data.csv', header=4).values
# print(info)
df = pd.DataFrame(info)
# print(type(df))
print(df)
# df[c - The date in YYYYMM.0][r - Celcius Temperature Anomaly]
print(df[0][0],df[1][0])

# Actually gathering the data
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

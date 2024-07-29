# Might need these later on
# import re
import numpy as np # type: ignore
import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore


# try:
#     temp_data = np.load('temp_data.npy')
# except:
#     temp_data = None

# Grabbing the data from csv file
data = pd.read_csv('data.csv', header=4).values
# print(type(data))
# print(data)
# print(data.shape)

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

# Special values based off of negative or not
# cold_temps = np.empty(data.shape)
# hot_temps = np.empty(data.shape)

# Gets the last date where we see the spike in global warming
last_norm_date_raw = 0

for i in range(data.shape[0]):
    x[i] = data[i][0]
    y[i] = data[i][1]
    if data[i][1] == 0:
        last_norm_date_raw = data[i][0]

# We still need to keep the raw version to plot
last_norm_date_str = str(last_norm_date_raw/100)
last_norm_date_arr = last_norm_date_str.split('.')
last_norm_date = {
    'year': last_norm_date_arr[0],
    'month': last_norm_date_arr[1]
}

# Graphing
plt.style.use('bmh')
fig,ax = plt.subplots()
# ax.plot(x,y,color='blue')
ax.scatter(x,y,s=15,color='black')
ax.set_title('Global Temperature', fontsize=24)
ax.set_xlabel('Date (YYYYMM)', fontsize=12)
ax.set_ylabel('Anomaly Temperature in Celcius', fontsize=12)
# Graphing the raw data
# plt.show()
# plt.savefig('global_temperature_raw.png')

# Specific points - Need to add in labels to these
# Calculation from Celcius to Fahrenheit is: F = (C * (9/5)) + 32
ax.axhline(y=0, color='grey')
# Last normal temperature before the appearance of global warming
print(f'Last Normal Temperature date is {last_norm_date["month"]} of {last_norm_date["year"]}')
ax.axvline(x=last_norm_date_raw, color='yellow')
# Average before the last normal temp
norm_ave = np.average(y,weights=(x<last_norm_date_raw))
print(f'Normal average temp before global warming effects = {norm_ave} Celcius or {(norm_ave*(9/5))+32} Fahrenheit')
ax.axhline(y=norm_ave, color='green')
# Hottest Temp
max_temp = np.max(y)
print(f'Hottest Temperature = {max_temp} Celcius or {(max_temp*(9/5))+32} Fahrenheit')
ax.axhline(y=max_temp, color='red')
# Coldest Temp
min_temp = np.min(y)
print(f'Coldest Temperature = {min_temp} Celcius or {(min_temp*(9/5))+32} Fahrenheit')
ax.axhline(y=min_temp, color='purple')
# Hot Average
actual_hot_ave = np.average(y,weights=(y>0))
print(f'Average Warm Temperature = {actual_hot_ave} Celcius or {(actual_hot_ave*(9/5))+32} Fahrenheit')
ax.axhline(y=actual_hot_ave, color='orange')
# Cold Average
actual_cold_ave = np.average(y,weights=(y<0))
print(f'Average Cool Temperature = {actual_cold_ave} Celcius or {(actual_cold_ave*(9/5))+32} Fahrenheit')
ax.axhline(y=actual_cold_ave, color='blue')

plt.show()
# plt.savefig('global_temperature.png')

# np.save('temp_data',data)

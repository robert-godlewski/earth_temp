# This will actually make the graph that we need
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore


# Calculation from Celcius to Fahrenheit is: F = (C * (9/5)) + 32
def celciusToFahrenheit(temp: float) -> float:
    return (temp*(9/5))+32

# Grabbing the data from a saved numpy array otherwise will not work
try:
    data = np.load('temp_data.npy')
    # Setting up axis to graph
    x = np.empty(data.shape[0])
    y = np.empty(data.shape[0])

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

    # Specific points
    ax.axhline(y=0, color='red',label='Current Temp. Baseline at 0.')
    # Last normal temperature before the appearance of global warming
    date_msg = f'Last Normal Temperature Date is {last_norm_date["month"]} of {last_norm_date["year"]}.'
    ax.axvline(x=last_norm_date_raw, color='yellow', label=date_msg)
    # Average before the last normal temp
    norm_ave = np.average(y,weights=(x<last_norm_date_raw))
    # temperatureMessage('Normal average temp before global warming effects',norm_ave)
    ax.axhline(y=norm_ave, color='blue', label=f'Baseline Temp. before {last_norm_date["year"]} is at {round(norm_ave,2)}.')
    # Below is not needed for now
    # Hottest Temp
    # max_temp = np.max(y)
    # ax.axhline(y=max_temp, color='red')
    # Coldest Temp
    # min_temp = np.min(y)
    # ax.axhline(y=min_temp, color='purple')
    # Hot Average
    # actual_hot_ave = np.average(y,weights=(y>0))
    # ax.axhline(y=actual_hot_ave, color='orange')
    # Cold Average
    # actual_cold_ave = np.average(y,weights=(y<0))
    # ax.axhline(y=actual_cold_ave, color='blue')
    ax.legend(loc='upper left', prop={'size':6})

    plt.savefig('global_temperature.png')
    plt.show()

except:
    print('Not able to actually graph.  Try uploading first.')

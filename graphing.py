# This will actually make the graph that we need
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore


def celciusToFahrenheit(temp: float) -> float:
    return (temp*(9/5))+32

def temperatureMessage(msg: str, temp: float) -> None:
    temp_f = celciusToFahrenheit(temp)
    print(f'{msg} = {temp} Celcius or {temp_f} Fahrenheit.')

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

    # Specific points - Need to add in labels to these
    # Calculation from Celcius to Fahrenheit is: F = (C * (9/5)) + 32
    ax.axhline(y=0, color='grey')
    # Last normal temperature before the appearance of global warming
    print(f'Last Normal Temperature date is {last_norm_date["month"]} of {last_norm_date["year"]}')
    ax.axvline(x=last_norm_date_raw, color='yellow')
    # Average before the last normal temp
    norm_ave = np.average(y,weights=(x<last_norm_date_raw))
    temperatureMessage('Normal average temp before global warming effects',norm_ave)
    ax.axhline(y=norm_ave, color='green')
    # Hottest Temp
    max_temp = np.max(y)
    temperatureMessage('Hottest Temperature',max_temp)
    ax.axhline(y=max_temp, color='red')
    # Coldest Temp
    min_temp = np.min(y)
    temperatureMessage('Coldest Temperature',min_temp)
    ax.axhline(y=min_temp, color='purple')
    # Hot Average
    actual_hot_ave = np.average(y,weights=(y>0))
    temperatureMessage('Average Warm Temperature',actual_hot_ave)
    ax.axhline(y=actual_hot_ave, color='orange')
    # Cold Average
    actual_cold_ave = np.average(y,weights=(y<0))
    temperatureMessage('Average Cool Temperature',actual_cold_ave)
    ax.axhline(y=actual_cold_ave, color='blue')

    plt.show()
    # plt.savefig('global_temperature.png')

except:
    print('Not able to actually graph.  Try uploading first.')

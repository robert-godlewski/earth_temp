# This will just load and save the data as a numpy array file.
import numpy as np # type: ignore
import pandas as pd # type: ignore


try:
    old_data = np.load('temp_data.npy')
except:
    old_data = None
    print('There is no original temp_data.npy!')

try:
    # The first 4 lines within the data file is just random information that we don't need.
    header = 4

    if old_data:
        old_size = old_data.size
        data = pd.read_csv('data.csv',header=old_size+header).values
    else:
        data = pd.read_csv('data.csv',header=header).values

    # Figuring out what the data means
    # print(type(data))
    # print(data)
    # print(f'Shape of data = {data.shape}')
    # print(f'Number of data points = {data.shape[0]}')

    # Testing out Pandas DataFrame class
    # df = pd.DataFrame(data)
    # print(type(df))
    # print(df)
    # # df[c][r]
    # print(type(df[0][0]))
    # print(df[0][0],df[1][0])

    np.save('temp_data',data)
    print('Saved new data.')
except:
    print('There is no data.csv to mine the necessary information!')

import BAC0
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import lib.sd_util

PI_ADDR = '192.168.92.5'
EMULATOR_ADDR = '127.0.0.1' # BASemulator20
NET_ADDR = '192.168.92.68'
UDP_PORT = 47808
SUBNET_MASK = '/24'
INTERVAL_S = 30
TIME_FORMAT = "%Y-%b-%d %H:%M:%S"
TIME_LENGTH = 240 

# Estbalish connection with BACnet netowrk
bacnet = BAC0.lite(ip=PI_ADDR + SUBNET_MASK, port=UDP_PORT)

# Create a Python object for a BACnet device
mycontroller = BAC0.device(NET_ADDR, 2749,  bacnet)

# Initialize arrays 
time_date = []
temp = []

# Monitors and add temperature data to array
for i in range(TIME_LENGTH):
    temp.append(bacnet.read('192.168.92.68 analogInput 1 presentValue'))
    print(bacnet.read('192.168.92.68 analogInput 1 presentValue'))
    time_date.append(time.strftime(TIME_FORMAT))
    time.sleep(INTERVAL_S)

df = pd.DataFrame({'time': time_date, 'temperature': temp})

# Saves a graph 
lib.sd_util.graph(df)

# saves dataframe to csv file
lib.sd_util.save(df)


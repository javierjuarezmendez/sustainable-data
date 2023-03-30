import BAC0
import time
import pandas as pd
import matplotlib.pyplot as plt

# Estbalish connection with BACnet netowrk
bacnet = BAC0.connect(ip='192.168.1.247/24', port=47808)

# Create a Python object for a BACnet device
mycontroller = BAC0.device('192.168.92.68', 2749,  bacnet)

time_date = []
temp = []

for i in range(10):
    temp.append(bacnet.read('192.168.92.68 analogInput 1 presentValue'))
    time_date.append(time.strftime("%Y-%b-%d %H:%M:%S"))
    time.sleep(1)

df = pd.DataFrame({'time': time_date, 'temperature': temp})

df.plot()
plt.show()

# Print a specific data point using a label
# print(mycontroller['Thermistor'])

# Tuple of a desired property
# prop = ('analogInput', 1, 'presentValue' )

# Read specified property
# mycontroller.read_property(prop)

# Prints all device controller properties
# print(mycontroller.bacnet_properties)

# Print historical data of the data point
# print(mycontroller['Thermistor'].history)


trend = BAC0.TrendLog(1, mycontroller)
"""
mycontroller['Thermistor'].chart()
bacnet.add_chart(controller['Thermistor'])
trendlog_object.chart()
"""

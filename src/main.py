import BAC0
import time

# Estbalish connection with BACnet netowrk
bacnet = BAC0.connect(ip='192.168.1.247/24', port=47808)

# Establish connection with BACnet devices
print(bacnet.whois())

# List all available BACnet devices
# print(bacnet.devices)

# Create a Python object for a BACnet device
mycontroller = BAC0.device('192.168.92.68', 2749,  bacnet)

# List all available point of the device
# print(mycontroller.points)

# Read data directly from the network
print(bacnet.read('192.168.92.68 analogInput 1 presentValue'))

print(mycontroller['Thermistor'].history)

# Debugging
# time.sleep(22)

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

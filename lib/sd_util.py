import pandas as pd
import matplotlib.pyplot as plt

# function: save()
# desc:     saves a pandas dataframe to a basic csv format
# input:    pandas dataframe
# output:   none
def save(df):
    print("Saving to .csv format ...")
    df.to_csv(index=False)

def read(fname):
    df = pd.read_csv(fname)
    return df

def graph(df):
    df.plot()
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title('Temp over Time')
    plt.savefig('graph.png')

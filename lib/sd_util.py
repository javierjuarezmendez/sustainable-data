import pandas as pd
import BAC0
import matplotlib.pyplot as plt

# function: save()
# desc:     saves a pandas dataframe to a basic csv format
# input:    pandas dataframe
# output:   none
def save(df):
    print("Saving to .csv format ...")
    df.to_csv(index=False)

# function: read()
# desc:     
# input:
# ouptut:
def read(fname):
    df = pd.read_csv(fname)
    return df

# function: sd_read()
# desc:     
# input:
# ouptut:
# def sd_write(fname, df):

#    break


# function: graph()
# desc:     takes a time over temp data in a pandas DataFrame and graphs it 
# input:    pandas DataFrame with time and temp
# ouptut:   no return, plots a graph and saves the figure
def graph(df):
    df.plot()
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.title('Temp over Time')
    plt.savefig('graph.png')

# function: live_graph()
# desc:     
# input:
# ouptut:
def live_graph(df):
    df2 = df[0:0]

    plt.ion()
    fig, ax = plt.subplots()

    i = 0
    while i < len(df):
        df2 = pd.concat([df2, df[i:i+1]])
        ax.clear()
        df2.plot(x="x", y="y", ax=ax)
        plt.draw()
        # plt.pause(0.2)
        i+=1

    plt.show() 



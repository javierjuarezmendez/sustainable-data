import pandas as pd
import matplotlib.pyplot as plt
import lib.sd_util

# constants
FNAME = 'tests/tests.csv'

# main entry
def main():
    df = lib.sd_util.read(FNAME)
    lib.sd_util.graph(df)
    # print(df.head())
    # df.plot()
    # plt.savefig('tests/tests.png')
    
def bacnet_test():


# running main
if __name__ == '__main__':
    main()

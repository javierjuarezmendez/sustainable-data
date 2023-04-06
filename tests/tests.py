import pandas as pd
import matplotlib.pyplot as plt

# constants
FNAME = 'tests.csv'

# main entry
def main():

    # 
    df = pd.read_csv(FNAME)
    print(df.head())

# running main
if __name__ == '__main__':
    main()

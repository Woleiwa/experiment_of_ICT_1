import numpy as np
import pandas as pd
import warnings

if __name__ == "__main__":

    warnings.filterwarnings('ignore')
    df = pd.read_csv('test.csv')
    print(df.sort_values(by=['score', 'attempts'],
               ascending=[False, False]))


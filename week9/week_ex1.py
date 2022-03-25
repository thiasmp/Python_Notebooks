import requests
import numpy as np
import pandas as pd
import zipfile


#Import the data into a Pandas dataframe.
#1 Programatically download the data from the above link.
Data = 'https://think.cs.vt.edu/corgis/datasets/csv/cars/cars.csv'

if __name__ == "__main__":
#Import the data into a Pandas dataframe.
    df = pd.read_csv(Data)
#Show the head of the Pandas dataframe.
#print(df.head())

#2
#mask_emission = pd.Series(df = df['Identification.Make'].values,index=df['Honda'])
print(df.loc[df['Identification.Make']== 'Honda'])



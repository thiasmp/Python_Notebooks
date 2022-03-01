import requests
import numpy as np
import pandas as pd
import zipfile


if __name__ == "__main__":
    data = pd.read_csv("API_EN.ATM.CO2E.KT_DS2_en_csv_v2_1345584.csv", skiprows=4)
    columns_names = data.columns
    countries = data["Country Name"]

    # 1
    country_emission = pd.Series(data=data["2014"].values, index=countries)
    #print(country_emission)

    # 2
    ex2 = country_emission.sort_values(ascending=False)
    print(ex2[:10])

    # 3

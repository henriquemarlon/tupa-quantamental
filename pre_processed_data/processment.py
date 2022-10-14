from logging import raiseExceptions
import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler

path  = os.path.dirname(os.path.realpath(__file__)) 

def price_fixing(region = "SUDESTE"):

    #checks if dataframe has been properly created
    try:
        # loads csv
        df = pd.read_csv(path +r"\df.csv")

    #error signal
    except:
        
        return  Exception

    #creates price column
    df['price'] =df[f"{region}"]
    df = df.drop(columns= ["SUDESTE","SUL","NORTE","NORDESTE","ANO"])

    #makes the start date the index
    # df.set_index("DATA_INICIO")
    
    #transform data from string to float
    df["price"] =df["price"].apply(lambda x: float(x.replace(",",".")))

    #creates column retorno
    df["retorno"] = 0   

    #fills retorno with a proper value
    df["retorno"] = df["price"].diff().div(df["price"])
    df.loc[0,"retorno"] = 0

    ss = StandardScaler()
    df["price"] = ss.fit_transform(df[["price"]])
    df["retorno"] = ss.fit_transform(df[["retorno"]])

    return df

def iee():
    base_path = os.path.dirname(os.path.realpath(__file__)).replace("\pre_processed_data","")
    
    df = pd.read_csv(base_path+r"\raw_data\IEE B3\iee.csv",sep =";")
    date = {
        "jan": "01",
        "feb": "02",       
        "mar": "03",
        "apr": "04",
        "may": "05",
        "jun": "06",
        "ju": "06",
        "jul": "07",
        "aug": "08",
        "sep": "09",
        "oct": "10",
        "nov": "11",
        "dec": "12",
    }
    # print(df.describe())
    # print(df.dtypes)
    
    df["date"] = df["date"].apply(lambda x : x.replace(x[0:3],date[x[0:3].lower()]))
    
    

    print(df)

iee()


    




    
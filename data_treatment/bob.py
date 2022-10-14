import os
from pandas import pandas as pd
import numpy as np

#file path relative to the computer
base_path = os.path.dirname(os.path.realpath(__file__)).replace("\data_treatment","")
raw_data_path = r"\raw_data\Preço de Liquidação das Diferenças(pld)"
pre_processed_data_path = r"\pre_processed_data"

def fn():       # 1.Get file names from directory
    file_list=os.listdir(base_path + raw_data_path)
    print (file_list)
    return file_list

def file_merge(file_list):

    #creates a csv with the first file
    lista = pd.read_csv(base_path + raw_data_path + f'\{file_list[0]}',sep=";").drop(columns = ["MES","SEMANA"])

    # goes over every file name
    for item in file_list:
        if not item == "read_me.txt":
            df = pd.read_csv(base_path + raw_data_path + f'\{item}',sep=";").drop(columns = ["MES","SEMANA"])
            #joins files
            lista = pd.concat([lista,df])

    return lista.drop_duplicates()

def main():
    
    file_merge(fn()).to_csv(base_path +pre_processed_data_path + r"\df.csv", index=False)

main()



import pandas as pd


df = pd.read_csv(r'C:\Users\Usuario\OneDrive\Documentos\GitHub\Nova pasta\Itau-quant-machine-learning-energy-prices\data\dados.csv')

print(df.max(),df.min())

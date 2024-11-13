import pandas as pd
import os


DATASET = os.path.join('datos','prueba.csv')

df = pd.read_csv(DATASET)

print(df)




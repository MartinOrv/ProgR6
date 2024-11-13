import pandas as pd
import os
#from preprocess.missings import get_num_missings_col

import preprocess.missings as msg

DATASET = os.path.join('datos','prueba.csv')

df = pd.read_csv(DATASET)

print(msg.get.num_missings_col(df))
print(df)




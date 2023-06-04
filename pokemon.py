import pandas as pd
import numpy as np

poke_df = pd.read_csv('Pokemon.csv', encoding='utf-8')

poke_df = poke_df.sample(random_state=1,
                         frac=1).reset_index(drop=True)

#print (poke_df.head(10))

gens = np.unique(poke_df['Generation'])

print(gens)

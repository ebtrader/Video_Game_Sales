import pandas as pd
import numpy as np

vg_df = pd.read_csv('vgsales.csv', encoding='latin-1')
selection1 = vg_df[['Name', 'Platform', 'Year', 'Genre', 'Publisher']].iloc[1:10]
selection = vg_df[['Name', 'Platform', 'Year', 'Genre', 'Publisher']].head(10)
#print (vg_df.head(10))
#print (selection)

genres = np.unique(vg_df['Genre'])
#print (genres)

from sklearn.preprocessing import LabelEncoder

gle = LabelEncoder()

genre_labels = gle.fit_transform(vg_df['Genre'])
#genre_mappings = {index: label for index, label in
#                  enumerate(gle.classes_)}
#print (genre_mappings)

vg_df['GenreLabel'] = genre_labels

vg_gen_labels = vg_df[['Name', 'Platform', 'Year', 'Genre', 'GenreLabel']].head(10)

print (vg_gen_labels)


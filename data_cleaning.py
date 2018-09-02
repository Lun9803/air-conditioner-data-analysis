import pandas as pd
import numpy as np

file_name = 'airconditioner.csv'
data = pd.read_csv(file_name)
# drop the columns that are not needed for this research
data.drop(['Sold_in', 'Submit_ID', 'ExpDate', 'GrandDate', 'SubmitStatus'], axis=1, inplace=True)
data.drop(['Availability Status', 'Product Website', 'Product Class'], axis=1, inplace=True)
data.drop(['Representative Brand URL', 'Star Image Large', 'Star Image Small'], axis=1, inplace=True)
# drop the column which has more than 200 Nan value
data.dropna(axis=1, thresh=len(data)-200, inplace=True)

data.to_csv('AC_cleaned.csv', encoding='utf-8')

import pandas as pd
import numpy as np
from sklearn.utils import shuffle


data1 = pd.read_csv('amazon_light_review.csv')
data2  = pd.read_csv('amazon_light_review2.csv')

data = [data1,data2]
data = pd.concat(data)

data =shuffle(data,random_state=44)

print(data.head())

data.to_csv('amazon-review.csv',index=False)
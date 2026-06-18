import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import csv

np.random.seed(42)

data = {
    'name': np.random.choice(['Gangadhar','Bhupinder','Katappa','Mogembo','Gabbar','Shakha','Sambha','Thanos','Modi','Hidimba',
                'Putna','Surpankha','None'],25),

    'age': np.random.randint(18,24,25).astype(float),
    
    'city': np.random.choice(['Nusantara','Melbourne','Seoul','Manila','Bangkok','Hanoi','Beijing','Sydney','Canberra','None'],25),

    'math_marks': np.random.randint(30,100,25).astype(float),
    'chemistry_marks': np.random.randint(30,100,25).astype(float),
    'hindi_marks': np.random.randint(30,100,25).astype(float),
    'english_marks': np.random.randint(30,100,25).astype(float),
    'physics_marks': np.random.randint(30,100,25).astype(float)
}

df = pd.DataFrame(data)

df.loc[np.random.choice(df.index,5), 'name'] = np.nan
df.loc[np.random.choice(df.index,3), 'age'] = np.nan
df.loc[np.random.choice(df.index, 2), 'city'] = np.nan
df.loc[np.random.choice(df.index, 4), 'math_marks'] = np.nan
df.loc[np.random.choice(df.index, 2), 'chemistry_marks'] = np.nan
df.loc[np.random.choice(df.index, 3), 'english_marks'] = np.nan

df.to_csv('ML mini project/students_25.csv', index=False)
df2 = pd.read_csv('ML mini project/students_25.csv')

print('Missing Values\n')
print(df2.isnull().sum())
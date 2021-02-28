import pandas as pd

titanic_df = pd.read_csv("C:/Users/user/Desktop/github/Python/titanic/train.csv")
print(titanic_df.head(3))

titanic_df_test = pd.read_csv("C:/Users/user/Desktop/github/Python/titanic/test.csv")
print(titanic_df_test.head(3))

#print(titanic_df.info())

print(titanic_df['Pclass'].value_counts())
import pandas as pd

# write your code here
general_df = pd.read_csv(r"test\\general.csv")
prenatal_df = pd.read_csv(r"test\\prenatal.csv")
sports_df = pd.read_csv(r"test\\sports.csv")

print(general_df.head(20))
print(prenatal_df.head(20))
print(sports_df.head(20))

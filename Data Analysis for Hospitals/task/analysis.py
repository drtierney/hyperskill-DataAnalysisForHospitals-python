import pandas as pd


general_df = pd.read_csv(r"test\\general.csv")
prenatal_df = pd.read_csv(r"test\\prenatal.csv")
sports_df = pd.read_csv(r"test\\sports.csv")

prenatal_df.rename(columns={"HOSPITAL": "hospital", "Sex": "gender"}, inplace=True)
sports_df.rename(columns={"Hospital": "hospital", "Male/female": "gender"}, inplace=True)

merged_df = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)
merged_df.drop(columns=["Unnamed: 0"], inplace=True)

print(merged_df.head(20))

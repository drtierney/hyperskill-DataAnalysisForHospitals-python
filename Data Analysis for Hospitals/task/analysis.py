import pandas as pd
import numpy as np

general_df = pd.read_csv(r"test\\general.csv")
prenatal_df = pd.read_csv(r"test\\prenatal.csv")
sports_df = pd.read_csv(r"test\\sports.csv")

prenatal_df.rename(columns={"HOSPITAL": "hospital", "Sex": "gender"}, inplace=True)
sports_df.rename(columns={"Hospital": "hospital", "Male/female": "gender"}, inplace=True)

merged_df = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)
merged_df.drop(columns=["Unnamed: 0"], inplace=True)
merged_df.dropna(how="all", inplace=True)

merged_df["gender"] = merged_df["gender"].replace(["man", "male"], "m")
merged_df["gender"] = merged_df["gender"].replace(["woman", "female", np.nan], "f")

merged_df.fillna(0, inplace=True)

# Which hospital has the highest number of patients?
q1_df = merged_df["hospital"]
q1_answer = q1_df.value_counts().keys().tolist()[0]
print(f"The answer to the 1st question is {q1_answer}")

# What share of the patients in the general hospital suffers from stomach-related issues?
# Round the result to the third decimal place.
q2_df = merged_df[merged_df["hospital"] == "general"]
q2_answer = len(q2_df.query('diagnosis == "stomach"')) / len(q2_df)
print(f"The answer to the 2nd question is {round(q2_answer, 3)}")

# What share of the patients in the sports hospital suffers from dislocation-related issues?
# Round the result to the third decimal place.
q3_df = merged_df.query('hospital == "sports"')
q3_answer = len(q3_df.loc[q3_df["diagnosis"] == "dislocation"]) / len(q3_df)
print(f"The answer to the 3rd question is {round(q3_answer, 3)}")

# What is the difference in the median ages of the patients in the general and sports hospitals?
q4_gen_median = merged_df.query('hospital == "general"').age.median()
q4_spo_median = merged_df[merged_df["hospital"] == "sports"]["age"].median()
q4_answer = max(q4_gen_median, q4_spo_median) - min(q4_gen_median, q4_spo_median)
print(f"The answer to the 4th question is {q4_answer}")

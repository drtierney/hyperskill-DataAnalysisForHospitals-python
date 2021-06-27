import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

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

# PART 4 QUESTIONS
# Which hospital has the highest number of patients?
p4_q1_df = merged_df["hospital"]
p4_q1_answer = p4_q1_df.value_counts().keys().tolist()[0]
# print(f"The answer to the 1st question is {p4_q1_answer}")

# What share of the patients in the general hospital suffers from stomach-related issues?
# Round the result to the third decimal place.
p4_q2_df = merged_df[merged_df["hospital"] == "general"]
p4_q2_answer = len(p4_q2_df.query('diagnosis == "stomach"')) / len(p4_q2_df)
# print(f"The answer to the 2nd question is {round(p4_q2_answer, 3)}")

# What share of the patients in the sports hospital suffers from dislocation-related issues?
# Round the result to the third decimal place.
p4_q3_df = merged_df.query('hospital == "sports"')
p4_q3_answer = len(p4_q3_df.loc[p4_q3_df["diagnosis"] == "dislocation"]) / len(p4_q3_df)
# print(f"The answer to the 3rd question is {round(p4_q3_answer, 3)}")

# What is the difference in the median ages of the patients in the general and sports hospitals?
p4_q4_gen_median = merged_df.query('hospital == "general"').age.median()
p4_q4_spo_median = merged_df[merged_df["hospital"] == "sports"]["age"].median()
p4_q4_answer = max(p4_q4_gen_median, p4_q4_spo_median) - min(p4_q4_gen_median, p4_q4_spo_median)
# print(f"The answer to the 4th question is {p4_q4_answer}")

# PART 5 QUESTIONS
# Which hospital has the highest number of patients? Create a histogram.
merged_df["hospital"].value_counts().plot(kind="bar", title="Patient Count Per Hospital Type")
plt.show()

print("The answer to the 1st question: general")

# What is the most common diagnosis among patients in all hospitals? Create a pie chart.
merged_df["diagnosis"].value_counts().plot(kind="pie", title="Count per Diagnosis")
plt.show()

print("The answer to the 2nd question: pregnancy")

# Build a violin plot of growth distribution by hospitals.
# Try to answer the question: what is the main reason for the gap in values?
# No special form is required to answer this question.
sns.violinplot(data=merged_df, x="hospital", y="height")
plt.show()

print("The answer to the 3rd question: It's because different units of measure have been used between the different hospital categories")

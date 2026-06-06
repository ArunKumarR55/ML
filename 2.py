import pandas as pd

data = pd.read_csv("data2.csv")

concepts = data.iloc[:, :-1].values
target = data.iloc[:, -1].values

hypothesis = concepts[0]

for i in range(len(concepts)):
    if target[i] == "Yes":
        for j in range(len(hypothesis)):
            if hypothesis[j] != concepts[i][j]:
                hypothesis[j] = "?"

print("Most Specific Hypothesis:")
print(hypothesis)
import pandas as pd
df = pd.read_csv("IPC_whole - IPC_whole.csv")
print(df)
questions = df["4"]
print(questions[49])

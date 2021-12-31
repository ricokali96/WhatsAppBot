import pandas as pd

data = {
  "firstname": ["Sally", "Mary", "John"],
  "age": [50, 40, 30]
}

df = pd.DataFrame(data)

for i in range(0, 3):
    for j in range(0, 2):
        print(df.iloc[i][j])
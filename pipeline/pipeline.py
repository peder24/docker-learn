import sys
import pandas as pd 
print("arguments", sys.argv)

df = pd.DataFrame({"day 1": [1, 2], "day 2": [3, 4]})
print(df.head())

day = int(sys.argv[1])
df.to_parquet(f"output_day_{day}.parquet")
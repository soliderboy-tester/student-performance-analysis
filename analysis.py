import pandas as pd
df=pd.read_csv("data.csv")

df["Average"]=df[["Math","Science","English"]].mean(axis=1)
print(df)
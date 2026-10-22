import pandas as pd

data={
    "Marks":[80,90,None,70,None]
}

df=pd.DataFrame(data)

df["Marks"]=df["Marks"].fillna(df["Marks"].mean())

print(df)

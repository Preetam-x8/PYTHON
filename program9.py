import pandas as pd
data={
    "Name":["Rahul","Anjali","Kiran"],
    "Marks":[75,90,80]
}

df=pd.DataFrame(data)

print("Sorted Data:")
print(df.sort_values("Marks"))

print("\nFiltered Data:")
print(df[df["Marks"]>75])

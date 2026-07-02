import pandas as pd
#print(pd.__version__)
#dragons={1:"Bulbasaur",2:"Ivysaur",3:"Venusaur",4:"charmander",5:"charmeleon",6:"charizard"}
#series=pd.Series(dragons)
#print(series)
"""
dt={
    "name":["x", "y", "z"],
    "age": [30,23, 34]
}
df=pd.DataFrame(dt, index=["Employee 1","Employee 2","Employee 3"])

#print(df["age"]) ---- important for working with coloumn
df["job"]=["cook","N/A","ceo"]
new_entry= pd.DataFrame([{"name":"a","age":30,"job":"Md"},{"name":"b","age":39,"job":"Gm"}],index=["Employee 4","Employee 5"])
df=pd.concat([df,new_entry])


print(df)
"""

df=pd.read_csv("data_employee.csv",index_col="Name")
# select by colm
#print(df["Name"].to_string())
#print(df.to_string())
#print(df[["Name","Height"]].to_string())
print(df.loc["Pikachu" ,["Height","Weight"]])
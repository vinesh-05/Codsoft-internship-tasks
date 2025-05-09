import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv("IMDb Movies India.csv",encoding="ISO-8859-1")
# print(df.head())
# print(df.shape)
# print(df.describe())
# .print(df.isnull().sum())
# print(df.duplicated().sum())
# print(df.info())
df['Duration']=df["Duration"].str.replace("min","").str.strip()
df["Duration"]=pd.to_numeric(df["Duration"],errors="coerce")
# print(df.info())
df["Votes"]=pd.to_numeric(df["Votes"],errors="coerce")
# print(df.info())
df['Year']=df['Year'].str.replace('(',"").str.strip()
df['Year']=df['Year'].str.replace(')',"").str.strip()
df['Year']=pd.to_numeric(df["Year"],errors='coerce')
# print(df.info())
# print(df)
df['Year']=df['Year'].fillna(df["Year"].median())
# print(df.isnull().sum())
df["Duration"]=df["Duration"].fillna(df["Duration"].median())
# print(df.isnull().sum())
# print(df)
df["Rating"]=df["Rating"].fillna(df["Rating"].mean())
df["Votes"]=df["Votes"].fillna(df["Votes"].mean())
# print(df.isnull().sum())
# print(df["Votes"])
# print(df['Rating']
# print(df.isnull().sum())
le=LabelEncoder()
df["Genre"]=le.fit_transform(df["Genre"])
df['Director']=le.fit_transform(df["Director"])
df["Actor 1"]=le.fit_transform(df["Actor 1"])
df["Actor 2"]=le.fit_transform(df["Actor 2"])
df["Actor 3"]=le.fit_transform(df["Actor 3"])
# print(df)
x=df.drop(columns=["Name","Rating"])
y=df["Rating"]
# print(x)
# print(y)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=RandomForestRegressor(n_estimators=100,random_state=42)
model.fit(x_train,y_train)
pred=model.predict(x_test)
mae=mean_absolute_error(y_test,pred)
mse=mean_squared_error(y_test,pred)
r2=r2_score(y_test,pred)
print(mae)
print(mse)
print(r2)

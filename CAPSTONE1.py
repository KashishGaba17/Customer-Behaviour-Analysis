import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\HP\Downloads\customer_shopping_behavior.csv")
print(df.head())
print(df.describe())
print(df.info())
print(df.isnull().sum())
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(" ","_")


df["review_rating"]=df.groupby("category")["review_rating"].transform(lambda x:x.fillna(x.median()))
print(df.isnull().sum())

df=df.rename(columns={"purchase_amount_(usd)":"purchase_amount"})
print(df.columns)

bins = [0, 18, 35, 50, 65, 100]
labels = ["Child", "Young Adult", "Adult", "Middle Age", "Senior"]
df["Age_Group"] = pd.cut(df["age"], bins=bins, labels=labels, right=False)
print(df)

frequency_mapping={
    "Fortnightly":14,
    "Weekly":7,
    "Monthly":30,
    "Quarterly":90,
    "Bi-Weekly":14,
    "Annually":365,
    "Every 3 Months":90
}

df["purchase_freq_days"]=df["frequency_of_purchases"].map(frequency_mapping)
print(df)

print((df["discount_applied"]==df["promo_code_used"]).all())
df.drop("promo_code_used",axis=1,inplace=True)
print(df.columns)

from sqlalchemy import create_engine

# MySQL connection
from sqlalchemy import create_engine
from urllib.parse import quote_plus

username = "root"
password = quote_plus("Kashdata17@")  # IMPORTANT
host = "127.0.0.1"                    # also important
port = "3306"
database = "customer_behavior"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

from sqlalchemy import create_engine
from urllib.parse import quote_plus

username = "root"
password = quote_plus("kashdata17@")
host = "127.0.0.1"
port = "3306"
database = "customer_behaviour"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

# test connection
engine.connect()
print("Connected successfully!")

table_name = "customer"   # choose any table name
df.to_sql(table_name, engine, if_exists="replace", index=False)
import numpy as np
import pandas as pd
from scipy import stats
from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest
import matplotlib.pyplot as plt

cdd = pd.read_csv("./G308CDD_DAHP_OnlineRetail.csv", encoding="ISO-8859-1")
print(cdd.head(10))

print("Do lon cua bang [frame]:", cdd.shape)

cdd_null_percent = cdd.isnull().sum() / len(cdd) * 100
print("Phần trăm các cột bị null:")
print(cdd_null_percent.sort_values(ascending=0))

plt.bar(cdd_null_percent.index, cdd_null_percent.values)
plt.xticks(rotation=90)  # dùng để quay nhãn của trục x đi một góc 90 độ
plt.ylabel("% giá trị null")
plt.show()

cdd = cdd.drop(columns=["CustomerID"])
print("Shape: ", cdd.shape)

print(cdd["Country"].unique())

cdd_label = preprocessing.LabelEncoder()
cdd["Country"] = cdd_label.fit_transform(cdd["Country"])
print(cdd.head())

cdd["Description"] = cdd["Description"].fillna(0)
cdd.isnull().sum()

cdd["Description"].value_counts().head()

cdd["Year"] = pd.DatetimeIndex(cdd["InvoiceDate"]).year
cdd["Month"] = pd.DatetimeIndex(cdd["InvoiceDate"]).month
cdd["Day"] = pd.DatetimeIndex(cdd["InvoiceDate"]).day
cdd.tail()

cdd["InvoiceDate"] = pd.to_datetime(cdd["InvoiceDate"])
cdd.head()

z = np.abs(stats.zscore(cdd._get_numeric_data()))
print("MA TRAN Z-SCORE\n")
print(z)
print(cdd.tail())

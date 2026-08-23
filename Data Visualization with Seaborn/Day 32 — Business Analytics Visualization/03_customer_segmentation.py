# 03_customer_segmentation.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("business_sales.csv")

# --------------------------------------------

# CUSTOMER TYPE ANALYSIS

# --------------------------------------------

cust_sales = df.groupby("customer_type")["sales"].sum().reset_index()

sns.barplot(
data=cust_sales,
x="customer_type",
y="sales"
)

plt.title("Sales by Customer Type")
plt.show()

# --------------------------------------------

# INSIGHT:

# - new vs returning customers

# --------------------------------------------

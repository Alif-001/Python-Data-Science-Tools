# � Day 27 — Pandas + Seaborn Workflow

---

# 🎯 Objective

- Pandas + Seaborn একসাথে ব্যবহার করা শেখা
- Real CSV dataset analysis করা
- Groupby visualization বোঝা
- Complete EDA workflow তৈরি করা
- Business-style insight generation শেখা

---

# 📚 Topics Covered

- DataFrame-based visualization
- Groupby analysis + plotting
- Multi-variable EDA
- Time-based visualization
- Full EDA pipeline
- Real dataset analysis (`tips` + CSV)

---

# 📁 Project Structure

```bash id="day27-structure"
day-27/
│── 01_dataframe_basic_plot.py
│── 02_groupby_visualization.py
│── 03_multi_variable_eda.py
│── 04_time_based_eda.py
│── 05_advanced_group_analysis.py
│── 06_real_world_eda_pipeline.py
│── 07_tips_dataset_workflow.py
│── sales_eda.csv
│── README.md
```

---

# 📊 Dataset

## 📌 File Name: `sales_eda.csv`

## 📌 Description

এই dataset এ region, product, sales এবং profit data দেওয়া আছে, যা real-world business analysis শেখার জন্য ব্যবহার করা হয়েছে।

---

## 📌 Columns

- `date` → transaction date
- `region` → sales region (North, South, East, West)
- `product` → product category (A, B, C)
- `sales` → total sales amount
- `profit` → profit value

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_dataframe_basic_plot.py

## 🔹 Purpose

- Direct DataFrame visualization বোঝা
- Simple barplot তৈরি করা

## 🧾 Code

```python id="d27-1"
sns.barplot(data=df, x="region", y="sales")
```

## 🧠 Explanation

- DataFrame সরাসরি Seaborn এ ব্যবহার করা যায়
- Region-wise sales compare করা হয়েছে
- Quick insight visualization

---

# 📄 2. 02_groupby_visualization.py

## 🔹 Purpose

- Groupby analysis শেখা
- Aggregated data visualize করা

## 🧾 Code

```python id="d27-2"
grouped = df.groupby("product")["sales"].mean().reset_index()
sns.barplot(data=grouped, x="product", y="sales")
```

## 🧠 Explanation

- আগে summary তৈরি করা হয়েছে
- তারপর plot করা হয়েছে
- Data aggregation = better insight

---

# 📄 3. 03_multi_variable_eda.py

## 🔹 Purpose

- Multi-variable relationship analysis

## 🧾 Code

```python id="d27-3"
sns.scatterplot(data=df, x="sales", y="profit", hue="region")
```

## 🧠 Explanation

- Sales vs Profit relationship
- Region-based grouping
- Pattern detection সহজ হয়

---

# 📄 4. 04_time_based_eda.py

## 🔹 Purpose

- Time series analysis শেখা

## 🧾 Code

```python id="d27-4"
df["date"] = pd.to_datetime(df["date"])
sns.lineplot(data=df, x="date", y="sales", marker="o")
```

## 🧠 Explanation

- Time-based trend analysis
- Growth pattern বোঝা যায়
- Date conversion required

---

# 📄 5. 05_advanced_group_analysis.py

## 🔹 Purpose

- Multi-dimensional grouping analysis

## 🧾 Code

```python id="d27-5"
sns.barplot(data=df, x="region", y="profit", hue="product")
```

## 🧠 Explanation

- Region + Product combined analysis
- Deeper segmentation insight
- Business-level reporting

---

# 📄 6. 06_real_world_eda_pipeline.py

## 🔹 Purpose

- Full EDA pipeline তৈরি করা

## 🧾 Code

```python id="d27-6"
grouped = df.groupby("region")["sales"].mean().reset_index()
sns.barplot(data=grouped, x="region", y="sales")
```

## 🧠 Explanation

- Step 1 → overview
- Step 2 → grouping
- Step 3 → visualization
- Complete analysis flow

---

# 📄 7. 07_tips_dataset_workflow.py

## 🔹 Purpose

- Built-in dataset full workflow

## 🧾 Code

```python id="d27-7"
sns.barplot(data=tips, x="day", y="total_bill")
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")
sns.histplot(data=tips, x="total_bill", kde=True)
```

## 🧠 Explanation

- Distribution + relationship + category analysis
- Full EDA in one dataset

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- DataFrame visualization করা হয়েছে
- Groupby analysis করা হয়েছে
- Multi-variable relationship দেখা হয়েছে
- Time-based trend analysis করা হয়েছে
- Full EDA pipeline তৈরি করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Pandas + Seaborn together powerful workflow তৈরি করে
- Groupby analysis = better insights
- Multi-variable plots pattern reveal করে
- Time-based analysis trend বোঝায়

---

# 🚀 What I Learned

- Real-world EDA workflow
- Groupby visualization technique
- Multi-variable analysis
- Business insight generation
- Pandas + Seaborn integration

---

# 🧠 Key Concepts (Quick Revision)

- DataFrame plotting = direct visualization
- Groupby = data summarization
- hue = category comparison
- lineplot = time series analysis
- EDA = load → analyze → visualize → insight

---

# 📝 Notes

## 📌 Mistakes

- groupby না করলে noisy data plot হতে পারে
- date format না convert করলে time series break হয়

## 📌 Optimization Tips

- Always summarize before plotting
- Use hue for deeper insight
- Combine Pandas + Seaborn for EDA

---

# 📌 Next Day Preview

## 📅 Day 28 — Seaborn + Matplotlib Integration

- Advanced customization
- Fine-tuning plots
- Combined visualization control
- Publication-style plotting

---

# ⭐ Bonus

## 🔥 Improvements Ideas

- Sales dashboard project বানানো
- Automated EDA report system
- Multi-file dataset analysis

---

## 🧪 Practice Ideas

- Region-wise deeper analysis করো
- Product performance compare করো
- Full EDA report নিজে build করো

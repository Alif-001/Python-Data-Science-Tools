# 📅 Day 30 — Missing Data Visualization

---

# 🎯 Objective

- Missing values কীভাবে identify করতে হয় তা শেখা
- Missing data pattern visualize করা শেখা
- Data quality analysis বোঝা
- Cleaning strategy choose করা শেখা
- Real-world EDA workflow তৈরি করা

---

# 📚 Topics Covered

- Missing values detection
- Missing data heatmap
- Missing pattern analysis
- Missing percentage calculation
- Drop vs fill strategy
- Data quality dashboard
- Missing data storytelling

---

# 📁 Project Structure

```bash id="day30-structure"
day-30/
│── 01_basic_missing_check.py
│── 02_missing_heatmap.py
│── 03_missing_pattern_analysis.py
│── 04_cleaning_strategy_demo.py
│── 05_column_wise_missing_visual.py
│── 06_real_world_missing_analysis.py
│── 07_business_data_quality_dashboard.py
│── 08_final_missing_data_story.py
│── student_missing.csv
│── README.md
```

---

# 📊 Dataset

## 📌 File Name: `student_missing.csv`

## 📌 Description

এই dataset এ intentionally missing values রাখা হয়েছে, যাতে data cleaning এবং missing data visualization practice করা যায়।

---

## 📌 Columns

- `name` → student name
- `math` → mathematics score
- `physics` → physics score
- `chemistry` → chemistry score
- `english` → english score

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_basic_missing_check.py

## 🔹 Purpose

- কোন column এ কত missing value আছে তা বের করা
- Basic missing value inspection করা

## 🧾 Code

```python id="d30-1"
import pandas as pd

df = pd.read_csv("student_missing.csv")

print("Missing values per column:")
print(df.isnull().sum())
```

## 🧠 Explanation

- `pd.read_csv()` → dataset load করে
- `df.isnull()` → missing value খুঁজে
- `sum()` → প্রতিটি column এ কয়টা missing আছে তা দেখায়

---

# 📄 2. 02_missing_heatmap.py

## 🔹 Purpose

- Missing values visually দেখানো
- Pattern বোঝার জন্য heatmap ব্যবহার করা

## 🧾 Code

```python id="d30-2"
sns.heatmap(
    df.isnull(),
    cbar=False,
    cmap="viridis"
)
```

## 🧠 Explanation

- `df.isnull()` → boolean matrix তৈরি করে
- Heatmap missing pattern visually দেখায়
- কোথায় data missing বেশি তা সহজে বোঝা যায়

---

# 📄 3. 03_missing_pattern_analysis.py

## 🔹 Purpose

- কোন column এ missing বেশি তা compare করা
- Pattern analysis করা

## 🧾 Code

```python id="d30-3"
missing_counts = df.isnull().sum()

sns.barplot(
    x=missing_counts.index,
    y=missing_counts.values
)
```

## 🧠 Explanation

- প্রতিটি feature এ missing count বের করা হয়েছে
- Barplot দিয়ে তুলনা করা হয়েছে
- সবচেয়ে incomplete column identify করা যায়

---

# 📄 4. 04_cleaning_strategy_demo.py

## 🔹 Purpose

- Missing value handle করার strategy শেখা
- Drop vs fill comparison বোঝা

## 🧾 Code

```python id="d30-4"
df_drop = df.dropna()
df_fill = df.fillna(df.mean(numeric_only=True))
```

## 🧠 Explanation

- `dropna()` → missing row remove করে
- `fillna()` → missing value fill করে
- দুইটি strategy এর trade-off বোঝা যায়

---

# 📄 5. 05_column_wise_missing_visual.py

## 🔹 Purpose

- Missing percentage calculate করা
- Column-level data quality বোঝা

## 🧾 Code

```python id="d30-5"
missing_ratio = df.isnull().mean() * 100

sns.barplot(
    x=missing_ratio.index,
    y=missing_ratio.values
)
```

## 🧠 Explanation

- Count এর চেয়ে percentage অনেক বেশি meaningful
- কোন column কত % incomplete তা clear হয়
- Data quality compare করা সহজ হয়

---

# 📄 6. 06_real_world_missing_analysis.py

## 🔹 Purpose

- Missing data analysis combined view এ করা
- Real EDA approach শেখা

## 🧾 Code

```python id="d30-6"
sns.heatmap(df.isnull(), cbar=False, cmap="coolwarm")
missing = df.isnull().sum()
sns.barplot(x=missing.index, y=missing.values)
```

## 🧠 Explanation

- Heatmap + barplot একসাথে analysis দেয়
- Visual + numeric summary পাওয়া যায়
- Better EDA workflow তৈরি হয়

---

# 📄 7. 07_business_data_quality_dashboard.py

## 🔹 Purpose

- Dashboard-style data quality report তৈরি করা
- Multiple views এক figure এ দেখা

## 🧾 Code

```python id="d30-7"
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.heatmap(df.isnull(), cbar=False, ax=axes[0])
sns.barplot(x=missing.index, y=missing.values, ax=axes[1])
```

## 🧠 Explanation

- এক figure এ দুইটা insight দেখানো হয়েছে
- Business reporting style তৈরি হয়
- Fast data review possible হয়

---

# 📄 8. 08_final_missing_data_story.py

## 🔹 Purpose

- Final storytelling visualization তৈরি করা
- Missing data quality visually highlight করা

## 🧾 Code

```python id="d30-8"
sns.heatmap(
    df.isnull(),
    cmap="YlOrRd",
    cbar=False
)
```

## 🧠 Explanation

- Missing values highlight করা হয়েছে
- Dataset quality instantly visible
- Clean vs dirty data easily identify করা যায়

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Missing values detect করা হয়েছে
- Heatmap তৈরি করা হয়েছে
- Missing count analysis করা হয়েছে
- Percentage calculation করা হয়েছে
- Cleaning strategy compare করা হয়েছে
- Dashboard-style quality report তৈরি করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Missing values easily detect করা যায়
- Heatmap pattern visually clear করে
- Percentage-based analysis বেশি useful
- Drop vs fill strategy situation অনুযায়ী choose করতে হয়

---

# 🚀 What I Learned

- Missing value detection
- Data quality analysis
- Heatmap visualization
- Cleaning strategy comparison
- Real-world EDA workflow

---

# 🧠 Key Concepts (Quick Revision)

- `isnull()` → missing value detect করে
- `sum()` → missing count দেয়
- `mean() * 100` → missing percentage
- `heatmap()` → missing pattern দেখায়
- `dropna()` → remove missing data
- `fillna()` → missing data replace করে

---

# 📝 Notes

## 📌 Mistakes

- Missing values ignore করলে wrong analysis হয়
- `dropna()` বেশি ব্যবহার করলে data loss হতে পারে
- Percentage না দেখে count দেখলে ভুল ধারণা হতে পারে

## 📌 Optimization Tips

- Always inspect missing data first
- Use heatmap for fast pattern detection
- Decide strategy based on data importance

---

# 📌 Next Day Preview

## 📅 Day 31 — Exploratory Data Analysis (EDA)

- Complete EDA workflow
- Correlation analysis
- Outlier detection
- Distribution analysis

---

# ⭐ Bonus

## 🔥 Improvements Ideas

- Real business dataset এ missing analysis করা
- Missing value imputation techniques explore করা
- Data quality report automate করা

---

## 🧪 Practice Ideas

- Different missing patterns তৈরি করে test করো
- Count vs percentage compare করো
- `dropna()` এবং `fillna()` result compare করো

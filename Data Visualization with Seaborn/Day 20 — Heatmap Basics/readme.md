# 📅 Day 20 — Heatmap Basics

---

# 🎯 Objective

- Matrix visualization কীভাবে কাজ করে তা শেখা
- `sns.heatmap()` ব্যবহার করে structured data analyze করা
- Correlation heatmap বোঝা
- `annot=True`, `cmap`, `mask`, `fmt` ব্যবহার করা
- Feature relationship visually discover করা

---

# 📚 Topics Covered

- `sns.heatmap()`
- Matrix visualization
- Correlation heatmap
- Annotation
- Colormap
- Custom formatting
- Masking upper triangle
- Business-style correlation analysis

---

# 📁 Project Structure

```bash id="day20"
day-20/
│── 01_basic_heatmap.py
│── 02_annotated_heatmap.py
│── 03_colormap_heatmap.py
│── 04_masked_heatmap.py
│── 05_custom_format_heatmap.py
│── 06_real_dataset_heatmap.py
│── 07_business_insight_heatmap.py
│── README.md
```

---

# 📊 Dataset

- **File Name:** Built-in Dataset (`tips`)
- **Description:** Restaurant tipping dataset যেখানে `total_bill`, `tip`, `sex`, `smoker`, `day`, `time`, `size` ইত্যাদি numeric + categorical information আছে
- **Columns:**
  - `total_bill` → মোট bill amount
  - `tip` → tip amount
  - `size` → group size
  - অন্যান্য categorical columns → analysis support করে

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_basic_heatmap.py

## 🔹 Purpose

- Basic heatmap তৈরি করা
- Correlation matrix visualize করা

## 🧾 Code

```python id="hm1"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

corr = tips.corr(numeric_only=True)

sns.heatmap(corr)

plt.title("Basic Correlation Heatmap")
plt.show()
```

## 🧠 Explanation

- `tips.corr(numeric_only=True)`
  - numeric columns-এর correlation matrix তৈরি করে

- `sns.heatmap(corr)`
  - matrix কে color-based visualization এ দেখায়

- color intensity relation strength বোঝায়

---

# 📄 2. 02_annotated_heatmap.py

## 🔹 Purpose

- Cell-এর ভিতরে exact values দেখানো

## 🧾 Code

```python id="hm2"
sns.heatmap(
    corr,
    annot=True
)
```

## 🧠 Explanation

- `annot=True`
  - প্রতিটি cell-এর ভিতরে number দেখায়

- exact correlation value directly read করা যায়
- insight আরও clear হয়

---

# 📄 3. 03_colormap_heatmap.py

## 🔹 Purpose

- Heatmap-এর color control করা

## 🧾 Code

```python id="hm3"
sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)
```

## 🧠 Explanation

- `cmap="coolwarm"`
  - blue-red color scale ব্যবহার করে

- positive/negative relation visually easy to understand হয়
- color choice analysis quality improve করে

---

# 📄 4. 04_masked_heatmap.py

## 🔹 Purpose

- Duplicate half hide করা
- Cleaner heatmap তৈরি করা

## 🧾 Code

```python id="hm4"
import numpy as np

mask = np.triu(np.ones_like(corr, dtype=bool))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    mask=mask
)
```

## 🧠 Explanation

- `np.triu()`
  - upper triangle mask তৈরি করে

- same correlation দুইবার দেখানো এড়ানো যায়
- lower triangle only display হয়

---

# 📄 5. 05_custom_format_heatmap.py

## 🔹 Purpose

- Formatting improve করা

## 🧾 Code

```python id="hm5"
sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    linewidths=0.5
)
```

## 🧠 Explanation

- `fmt=".2f"`
  - two decimal places show করে

- `linewidths=0.5`
  - cell borders clearly দেখা যায়

- readable and professional heatmap তৈরি হয়

---

# 📄 6. 06_real_dataset_heatmap.py

## 🔹 Purpose

- Small custom dataset দিয়ে real-world style correlation দেখানো

## 🧾 Code

```python id="hm6"
import pandas as pd

data = {
    "Math": [80, 90, 70, 60, 85],
    "Physics": [78, 88, 72, 65, 80],
    "Chemistry": [82, 91, 68, 70, 86]
}

df = pd.DataFrame(data)
corr = df.corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="YlGnBu"
)
```

## 🧠 Explanation

- custom dataframe বানিয়ে correlation দেখা হয়েছে
- subject score relationship analyze করা যায়
- educational dataset type insight পাওয়া যায়

---

# 📄 7. 07_business_insight_heatmap.py

## 🔹 Purpose

- business-style correlation insight বের করা

## 🧾 Code

```python id="hm7"
sns.heatmap(
    corr,
    annot=True,
    cmap="vlag",
    center=0
)
```

## 🧠 Explanation

- `center=0`
  - zero কে middle reference point ধরে

- negative vs positive relation visually balanced হয়
- business decision making এ useful insight দেয়

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Numeric columns থেকে correlation matrix বানানো হয়েছে
- Matrix heatmap হিসেবে visualize করা হয়েছে
- Annotation এবং color map add করা হয়েছে
- Mask ব্যবহার করে cleaner view তৈরি করা হয়েছে
- Real-world style structured data analysis করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Heatmap correlation বোঝার জন্য খুব powerful
- `annot=True` exact values দেখায়
- `cmap` visualization improve করে
- mask ব্যবহার করলে duplicate data hide হয়
- feature relationships সহজে detect করা যায়

---

# 🚀 What I Learned

- Matrix visualization concept
- Correlation analysis
- Color-based data interpretation
- Heatmap formatting and masking
- Feature relationship mapping

---

# 🧠 Key Concepts (Quick Revision)

- `heatmap()` → matrix visualization
- correlation matrix → feature relation table
- `annot=True` → values show করে
- `cmap` → color scale control করে
- `mask` → duplicate half hide করে
- `fmt` → number formatting করে

---

# 📝 Notes

## 📌 Common Mistakes

- numeric_only না ব্যবহার করা
- color scale confusing রাখা
- duplicate matrix full দেখানো

## 📌 Optimization Tips

- correlation heatmap-এর জন্য always numeric data use করো
- large matrix এ mask use করো
- clear colormap choose করো

---

# 📌 Next Day Preview

## 📅 Day 21 — Advanced Heatmap

আগামী দিনে শিখবো:

- masking techniques
- triangular heatmap
- custom color scaling
- large matrix visualization
- real-world correlation analysis

---

# ⭐ Bonus (Optional)

## 🔥 Improvement Ideas

- different datasets এ correlation heatmap try করো
- subject score analysis করো
- strong positive/negative relations identify করো

---

## 🧪 Practice Ideas

- `tips` dataset-এর correlation heatmap বানাও
- custom numeric dataframe দিয়ে heatmap try করো
- masked vs unmasked compare করো
- different `cmap` compare করো

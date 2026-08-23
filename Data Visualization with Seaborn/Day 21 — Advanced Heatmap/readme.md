# 📅 Day 21 — Advanced Heatmap

---

# 🎯 Objective

- Heatmap কে advanced data science tool হিসেবে ব্যবহার করা শেখা
- Masking technique দিয়ে clean visualization তৈরি করা
- Triangular correlation heatmap তৈরি করা
- Custom scaling এবং color control বোঝা
- Large dataset correlation analysis করা
- Real-world ML feature selection intuition develop করা

---

# 📚 Topics Covered

- Masking techniques
- Triangular heatmap
- Custom color scaling (`vmin`, `vmax`, `center`)
- Large matrix visualization
- Feature correlation analysis
- ML-style feature selection
- Business insight heatmaps

---

# 📁 Project Structure

```bash id="day21"
day-21/
│── 01_triangular_heatmap.py
│── 02_custom_color_scaling.py
│── 03_large_matrix_simulation.py
│── 04_masked_and_sorted_heatmap.py
│── 05_real_world_ml_heatmap.py
│── 06_business_insight_heatmap.py
│── 07_clean_professional_heatmap.py
│── README.md
```

---

# 📊 Dataset

- **File Name:** Built-in Dataset (`tips`) + Synthetic Dataset
- **Description:**
  - `tips` dataset → restaurant tipping behavior analysis
  - synthetic dataset → large feature correlation simulation

- **Columns:**
  - `total_bill` → total bill amount
  - `tip` → tip amount
  - `size` → number of people
  - synthetic features (`A–F`) → random numeric features for ML simulation

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_triangular_heatmap.py

## 🔹 Purpose

- Upper triangle hide করে clean correlation matrix দেখানো
- ML-style professional visualization তৈরি করা

## 🧾 Code

```python id="h21_1"
mask = np.triu(np.ones_like(corr, dtype=bool))

sns.heatmap(
    corr,
    mask=mask,
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)
```

## 🧠 Explanation

- `np.triu()` → upper triangle hide করে
- duplicate correlation remove করা হয়
- ML reports-এ standard format

---

# 📄 2. 02_custom_color_scaling.py

## 🔹 Purpose

- Correlation scale control করা
- Balanced visualization তৈরি করা

## 🧾 Code

```python id="h21_2"
sns.heatmap(
    corr,
    annot=True,
    cmap="RdBu",
    vmin=-1,
    vmax=1,
    center=0
)
```

## 🧠 Explanation

- `vmin`, `vmax` → fixed scale
- `center=0` → neutral reference point
- positive/negative correlation clear বোঝা যায়

---

# 📄 3. 03_large_matrix_simulation.py

## 🔹 Purpose

- Large dataset heatmap simulation
- Real ML dataset behavior বোঝা

## 🧾 Code

```python id="h21_3"
df = pd.DataFrame({
    "A": np.random.rand(100),
    "B": np.random.rand(100) * 2,
    "C": np.random.rand(100) * 3,
    "D": np.random.rand(100) * 4,
    "E": np.random.rand(100) * 5,
    "F": np.random.rand(100) * 6,
})

corr = df.corr()
```

## 🧠 Explanation

- synthetic dataset তৈরি করা হয়েছে
- multi-feature correlation analysis করা হয়েছে
- real-world ML dataset structure simulate করা হয়েছে

---

# 📄 4. 04_masked_and_sorted_heatmap.py

## 🔹 Purpose

- Correlation sorting + masking একসাথে ব্যবহার করা

## 🧾 Code

```python id="h21_4"
mask = np.triu(np.ones_like(corr, dtype=bool))

sns.heatmap(
    corr,
    mask=mask,
    annot=True,
    cmap="coolwarm"
)
```

## 🧠 Explanation

- mask duplicate data hide করে
- sorting concept feature importance বোঝাতে সাহায্য করে
- strongest relationships identify করা যায়

---

# 📄 5. 05_real_world_ml_heatmap.py

## 🔹 Purpose

- ML feature selection intuition তৈরি করা

## 🧾 Code

```python id="h21_5"
sns.heatmap(
    corr,
    annot=True,
    cmap="Spectral",
    center=0,
    linewidths=0.5
)
```

## 🧠 Explanation

- feature correlation analysis করা হয়
- redundant features identify করা যায়
- ML model optimization help করে

---

# 📄 6. 06_business_insight_heatmap.py

## 🔹 Purpose

- Business decision-making insight তৈরি করা

## 🧾 Code

```python id="h21_6"
sns.heatmap(
    corr,
    annot=True,
    cmap="YlGnBu",
    center=0
)
```

## 🧠 Explanation

- business-driven correlation analysis
- revenue influencing factors identify করা যায়
- strategic decision support করে

---

# 📄 7. 07_clean_professional_heatmap.py

## 🔹 Purpose

- Final professional-grade heatmap তৈরি করা

## 🧾 Code

```python id="h21_7"
sns.heatmap(
    corr,
    mask=mask,
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    center=0,
    linewidths=0.5
)
```

## 🧠 Explanation

- clean + professional ML visualization
- standardized reporting format
- production-level heatmap style

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Correlation matrix তৈরি করা হয়েছে
- Masking applied করা হয়েছে
- Color scaling customize করা হয়েছে
- Large dataset simulation করা হয়েছে
- Final professional visualization তৈরি করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Heatmap advanced ML tool হিসেবে ব্যবহার করা যায়
- Masking visualization cleaner করে
- Scaling ensures fair comparison
- Large matrix analysis possible
- Feature relationships easily discover করা যায়

---

# 🚀 What I Learned

- Advanced heatmap techniques
- Masking and triangular matrix concept
- Feature correlation interpretation
- ML feature selection intuition
- Business analytics visualization

---

# 🧠 Key Concepts (Quick Revision)

- `heatmap()` → matrix visualization
- `mask` → duplicate hide করা
- `vmin/vmax` → scale control
- `center=0` → neutral reference
- correlation → feature relationship measure

---

# 📝 Notes

## 📌 Common Mistakes

- scale control না করা
- mask না ব্যবহার করা
- too many features একসাথে plot করা

## 📌 Optimization Tips

- large dataset এ mask ব্যবহার করো
- proper colormap choose করো
- feature selection আগে correlation check করো

---

# 📌 Next Day Preview

## 📅 Day 22 — Cluster Map

আগামী দিনে শিখবো:

- hierarchical clustering visualization
- `sns.clustermap()`
- dendrogram understanding
- feature grouping automatically
- advanced pattern discovery

---

# ⭐ Bonus (Optional)

## 🔥 Improvements Ideas

- ML dataset এ feature correlation analyze করো
- business KPI correlation check করো
- different colormaps compare করো

---

## 🧪 Practice Ideas

- `tips` dataset heatmap recreate করো
- synthetic large dataset বানাও
- masked vs full heatmap compare করো
- strongest correlation features identify করো

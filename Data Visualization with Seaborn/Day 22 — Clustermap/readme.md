# 📅 Day 22 — Clustermap

---

# 🎯 Objective

- `sns.clustermap()` বোঝা
- Hierarchical clustering শেখা
- Dendrogram কিভাবে কাজ করে তা বোঝা
- Data similarity based grouping বুঝা
- Real-world segmentation ধারণা শেখা

---

# 📚 Topics Covered

- `sns.clustermap()`
- Hierarchical clustering
- Dendrogram
- Row clustering
- Column clustering
- Distance metrics
- Data standardization
- Feature similarity analysis

---

# 📁 Project Structure

```bash
day-22/
│── 01_basic_clustermap.py
│── 02_clustermap_standardized.py
│── 03_dendrogram_understanding.py
│── 04_row_column_clustering.py
│── 05_custom_metric_clustermap.py
│── 06_large_synthetic_clustermap.py
│── 07_real_world_segmentation.py
│── README.md
```

---

# 📊 Dataset

## 📌 File Name: iris (built-in) + synthetic datasets

## 📌 Description

এই project এ দুই ধরনের dataset ব্যবহার করা হয়েছে:

- **Iris dataset** → built-in dataset (flower features)
- **Synthetic dataset** → random generated data
- **Customer-like dataset** → segmentation simulation

---

## 📌 Columns

### 🌸 Iris Dataset

- `sepal_length` → flower sepal length
- `sepal_width` → flower sepal width
- `petal_length` → flower petal length
- `petal_width` → flower petal width
- `species` → flower type (removed for clustering)

### 📊 Synthetic / Customer Data

- `Feature_A` → random feature 1
- `Feature_B` → random feature 2
- `Feature_C` → random feature 3
- `Spending` → customer spending
- `Visits` → customer visits
- `Engagement` → engagement level

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_basic_clustermap.py

## 🔹 Purpose

- Basic clustermap তৈরি করা
- Default hierarchical clustering বোঝা

## 🧾 Code

```python
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset("iris")
data = iris.drop("species", axis=1)

sns.clustermap(data)
plt.title("Basic Clustermap")
plt.show()
```

## 🧠 Explanation

- `sns.load_dataset("iris")` → dataset load করা হয়েছে
- `drop("species")` → categorical column remove করা হয়েছে
- `sns.clustermap()` → automatic clustering করে
- dendrogram দেখায় similar data group

---

# 📄 2. 02_clustermap_standardized.py

## 🔹 Purpose

- Data scaling শেখা
- Standardized clustering বোঝা

## 🧾 Code

```python
data_scaled = (data - data.mean()) / data.std()

sns.clustermap(data_scaled, cmap="coolwarm")
plt.show()
```

## 🧠 Explanation

- Mean = 0, Std = 1 করা হয়েছে
- Large value bias remove করা হয়েছে
- Better clustering result পাওয়া যায়

---

# 📄 3. 03_dendrogram_understanding.py

## 🔹 Purpose

- Dendrogram structure বোঝা
- Hierarchical tree visualization শেখা

## 🧾 Code

```python
sns.clustermap(
    data,
    method="ward",
    cmap="viridis"
)
plt.show()
```

## 🧠 Explanation

- `method="ward"` → variance minimize করে clustering
- Tree structure → similarity relationship দেখায়

---

# 📄 4. 04_row_column_clustering.py

## 🔹 Purpose

- Row ও Column clustering বোঝা

## 🧾 Code

```python
sns.clustermap(
    data,
    row_cluster=True,
    col_cluster=True,
    cmap="coolwarm"
)
plt.show()
```

## 🧠 Explanation

- Rows = samples grouping
- Columns = feature grouping
- দুটোই reorder হয় pattern অনুযায়ী

---

# 📄 5. 05_custom_metric_clustermap.py

## 🔹 Purpose

- Distance metric control শেখা

## 🧾 Code

```python
sns.clustermap(
    data,
    metric="euclidean",
    cmap="Spectral"
)
plt.show()
```

## 🧠 Explanation

- Euclidean distance ব্যবহার করা হয়েছে
- Different metric → different clustering behavior

---

# 📄 6. 06_large_synthetic_clustermap.py

## 🔹 Purpose

- Large dataset simulation
- Real-world clustering behavior বোঝা

## 🧾 Code

```python
df_scaled = (df - df.mean()) / df.std()

sns.clustermap(df_scaled, cmap="coolwarm")
plt.show()
```

## 🧠 Explanation

- Multiple random features তৈরি করা হয়েছে
- Scaling applied করা হয়েছে
- Real dataset-like pattern simulation

---

# 📄 7. 07_real_world_segmentation.py

## 🔹 Purpose

- Customer segmentation simulation

## 🧾 Code

```python
data_scaled = (data - data.mean()) / data.std()

sns.clustermap(
    data_scaled,
    cmap="YlGnBu"
)
plt.show()
```

## 🧠 Explanation

- Customers grouped by behavior
- Spending + visits + engagement clustering

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Missing categorical data remove করা হয়েছে
- Data scaling করা হয়েছে
- Clustermap তৈরি করা হয়েছে
- Dendrogram visualize করা হয়েছে
- Similar patterns group করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Similar data automatically group হয়
- Scaling clustering quality improve করে
- Dendrogram relationship clearly দেখায়
- Real-world segmentation possible

---

# 🚀 What I Learned

- Hierarchical clustering concept
- `sns.clustermap()` usage
- Data standardization importance
- Dendrogram interpretation
- Pattern discovery in data

---

# 🧠 Key Concepts (Quick Revision)

- Clustermap = heatmap + clustering
- Dendrogram = tree of similarity
- Scaling is important
- Euclidean distance commonly used
- Useful for segmentation problems

---

# 📝 Notes

## 📌 Mistakes

- Scaling না করলে wrong clustering হয়
- Large dataset without normalization misleading হতে পারে

## 📌 Optimization Tips

- Always standardize data before clustermap
- Use appropriate color palettes for clarity

---

# 📌 Next Day Preview

## 📅 Day 23 — Time Series Visualization

- Time-based line plots
- Trend analysis
- Rolling averages
- Seasonal patterns

---

# ⭐ Bonus

## 🔥 Improvements Ideas

- Real customer dataset apply করা
- Financial data clustering try করা
- Gene expression dataset experiment করা

---

## 🧪 Practice Ideas

- Iris dataset ছাড়া অন্য dataset try করো
- Different `metric` values compare করো
- Scaling vs non-scaling result compare করো

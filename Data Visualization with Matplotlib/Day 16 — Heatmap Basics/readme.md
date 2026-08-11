# 📅 Day 16 — Heatmap Basics

## 🎯 Objective

- আজকে Heatmap visualization শিখবো
- Matrix data visualize করা শিখবো
- Correlation matrix বুঝতে শিখবো
- Color intensity mapping ব্যবহার করা শিখবো
- Real dataset থেকে correlation analysis করা শিখবো
- Data relationships visually interpret করা শিখবো

---

## 📚 Topics Covered

- Heatmap visualization
- Matrix plotting
- Correlation matrix
- Color intensity mapping
- Real-world data visualization

---

## 📁 Project Structure

```bash id="hm_day16"
day-16/
│── 01_basic_heatmap.py
│── 02_matrix_plotting.py
│── 03_correlation_heatmap_basic.py
│── 04_color_intensity_mapping.py
│── 05_heatmap_labels.py
│── 06_real_correlation_heatmap.py
│── student_scores.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** student_scores.csv
- **Description:** Students subject-wise marks dataset used for correlation heatmap analysis

### Columns:

- student → Student name
- math → Math score
- science → Science score
- english → English score

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. main.py

### 🔹 Purpose

- Heatmap concept introduction
- Matrix visualization idea বোঝা

### 🧾 Code

```python id="hm_main"
print("Day 16 - Heatmap Basics 🔥")
```

### 🧠 Explanation

- Heatmap = color-based matrix visualization
- Data intensity বোঝা সহজ হয়

---

## 📄 2. analysis.py

### 🔹 Purpose

- Correlation analysis helper

### 🧾 Code

```python id="hm_analysis"
def get_correlation(data):
    return "Correlation analysis done"
```

### 🧠 Explanation

- Data relationship analyze করার base function
- Future enhancement (statistics module) support করে

---

## 📄 3. utils.py

### 🔹 Purpose

- Helper functions

### 🧾 Code

```python id="hm_utils"
def normalize_matrix(matrix):
    return matrix
```

### 🧠 Explanation

- Matrix processing helper
- Data standardization support করে

---

## 📄 4. 01_basic_heatmap.py

### 🔹 Purpose

- Simple heatmap তৈরি করা

### 🧾 Code

```python id="hm1"
plt.imshow(data, cmap="hot")
plt.colorbar()
```

### 🧠 Explanation

- Matrix data color-based visualize করা হয়
- `hot` colormap intensity show করে

---

## 📄 5. 02_matrix_plotting.py

### 🔹 Purpose

- Matrix visualization বুঝা

### 🧾 Code

```python id="hm2"
plt.imshow(matrix, cmap="Blues")
```

### 🧠 Explanation

- Matrix directly heatmap আকারে দেখানো হয়
- Data pattern easily দেখা যায়

---

## 📄 6. 03_correlation_heatmap_basic.py

### 🔹 Purpose

- Correlation visualization

### 🧾 Code

```python id="hm3"
plt.imshow(corr, cmap="coolwarm")
```

### 🧠 Explanation

- Variables এর relationship দেখায়
- Positive/negative correlation বুঝা যায়

---

## 📄 7. 04_color_intensity_mapping.py

### 🔹 Purpose

- Value intensity mapping

### 🧾 Code

```python id="hm4"
plt.imshow(data, cmap="viridis")
```

### 🧠 Explanation

- High value = brighter/darker color
- Data magnitude visually বোঝা যায়

---

## 📄 8. 05_heatmap_labels.py

### 🔹 Purpose

- Heatmap with labels

### 🧾 Code

```python id="hm5"
plt.xticks(range(len(subjects)), subjects)
plt.yticks(range(len(students)), students)
```

### 🧠 Explanation

- Rows এবং columns readable করা হয়
- Student vs subject comparison সহজ হয়

---

## 📄 9. 06_real_correlation_heatmap.py

### 🔹 Purpose

- Real dataset correlation analysis

### 🧾 Code

```python id="hm6"
import numpy as np

data = np.array([math, science, english])

corr_matrix = np.corrcoef(data)

plt.imshow(corr_matrix, cmap="coolwarm")
plt.colorbar()
```

### 🧠 Explanation

- Real student marks থেকে correlation বের করা হয়েছে
- Subjects এর relationship visualize করা হয়েছে
- Math, Science, English dependency বোঝা যায়

---

## ⚙️ Implementation Flow

- Heatmap concept শেখা হয়েছে
- Matrix visualization করা হয়েছে
- Correlation matrix তৈরি করা হয়েছে
- Color intensity mapping করা হয়েছে
- Labels সহ heatmap তৈরি করা হয়েছে
- Real dataset analysis করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Heatmap data patterns clearly দেখায়
- Correlation relationships সহজে বোঝা যায়
- Matrix visualization powerful tool
- Color intensity = data magnitude
- Real dataset analysis insight দেয়

---

## 🚀 What I Learned

- Heatmap concept (`imshow`)
- Matrix visualization technique
- Correlation matrix idea
- Color mapping system
- Real data relationship analysis

---

## 🧠 Key Concepts (Quick Revision)

- `imshow()` → heatmap visualization
- `cmap` → color style
- `colorbar()` → scale indicator
- correlation → relationship between variables
- matrix → grid of values

---

## 📝 Notes

- Small datasets heatmap clearer হয়
- Correlation always causation না
- Proper scaling important
- Color selection visualization impact করে
- Too many values = cluttered heatmap

---

## 📌 Next Day Preview

- Colormaps deep dive
- Advanced color schemes
- Data normalization visualization
- Custom heatmap design
- Professional dashboard styling

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Student performance heatmap dashboard
- Automatic correlation detector
- Business KPI heatmap system
- Interactive matrix explorer

### 🧪 Practice Ideas

- Exam result correlation system
- Stock market correlation analysis
- Weather pattern heatmap
- Product rating matrix visualization

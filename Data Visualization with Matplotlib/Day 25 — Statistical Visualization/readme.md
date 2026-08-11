# 📅 Day 25 — Statistical Visualization

## 🎯 Objective

- আজকে statistical data visualization শিখবো
- Mean, median এবং standard deviation visualize করা শিখবো
- Distribution compare করা শিখবো
- Statistical insight graph-এর মাধ্যমে বোঝানো শিখবো
- Real dataset দিয়ে student performance analysis করা শিখবো

---

## 📚 Topics Covered

- Mean line
- Median line
- Standard deviation visualization
- Distribution comparison
- Statistical annotation

---

## 📁 Project Structure

```bash
day-25/
│── 01_mean_line_visualization.py
│── 02_median_line_visualization.py
│── 03_standard_deviation_visualization.py
│── 04_distribution_comparison.py
│── 05_statistical_annotation.py
│── 06_boxplot_statistics.py
│── 07_real_statistical_analysis.py
│── student_marks.csv
│── README.md
```

---

## 📊 Dataset

### 📄 File Name: `student_marks.csv`

- **Description:** Student exam marks dataset used for statistical analysis

### Columns:

- `student` → Student name
- `math` → Math marks
- `science` → Science marks
- `english` → English marks

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `main.py` (Concept Entry)

### 🔹 Purpose

- Statistical visualization introduction
- Mean/median concept understanding

### 🧾 Code

```python id="st1"
print("Day 25 - Statistical Visualization 📊")
```

### 🧠 Explanation

- Statistics helps summarize data
- Visualization makes patterns easier to understand

---

## 📄 2. `analysis.py`

### 🔹 Purpose

- Basic statistical calculations

### 🧾 Code

```python id="st2"
import numpy as np

def get_stats(data):
    return {
        "mean": np.mean(data),
        "median": np.median(data),
        "std": np.std(data)
    }
```

### 🧠 Explanation

- Mean → average value
- Median → middle value
- Std → data spread

---

## 📄 3. `utils.py`

### 🔹 Purpose

- reusable statistical helper functions

### 🧾 Code

```python id="st3"
def normalize(data):
    return (data - min(data)) / (max(data) - min(data))
```

### 🧠 Explanation

- Data scaling সহজ করে
- 0–1 range-এ convert করে

---

## 📄 4. `01_mean_line_visualization.py`

### 🔹 Purpose

- Mean value visualize করা

### 🧠 Explanation

- `np.mean()` দিয়ে average বের করা হয়েছে
- `plt.axhline()` দিয়ে mean line draw করা হয়েছে
- Data trend vs average compare করা হয়েছে

---

## 📄 5. `02_median_line_visualization.py`

### 🔹 Purpose

- Median visualization

### 🧠 Explanation

- Outlier থাকলেও median stable থাকে
- Green dashed line দিয়ে median show করা হয়েছে
- Real-world robust statistic concept বোঝানো হয়েছে

---

## 📄 6. `03_standard_deviation_visualization.py`

### 🔹 Purpose

- data spread visualization

### 🧠 Explanation

- mean ± std range দেখানো হয়েছে
- data variability বোঝানো হয়েছে
- consistency vs variation analysis করা হয়েছে

---

## 📄 7. `04_distribution_comparison.py`

### 🔹 Purpose

- Two group distribution compare করা

### 🧠 Explanation

- histogram দিয়ে group A vs B compare করা হয়েছে
- alpha blending overlap visualization দিয়েছে
- A/B testing concept বুঝানো হয়েছে

---

## 📄 8. `05_statistical_annotation.py`

### 🔹 Purpose

- statistical values highlight করা

### 🧠 Explanation

- mean line draw করা হয়েছে
- `plt.annotate()` দিয়ে mean explain করা হয়েছে
- arrow দিয়ে important point highlight করা হয়েছে

---

## 📄 9. `06_boxplot_statistics.py`

### 🔹 Purpose

- boxplot ব্যবহার করে statistical summary দেখা

### 🧠 Explanation

- median, quartiles, outliers visualize করা হয়েছে
- data spread compactভাবে দেখানো হয়েছে
- descriptive statistics representation

---

## 📄 10. `07_real_statistical_analysis.py`

### 🔹 Purpose

- real dataset statistical analysis

### 🧠 Explanation

- student marks থেকে average বের করা হয়েছে
- mean এবং median line add করা হয়েছে
- performance comparison visualization করা হয়েছে
- real-world academic analysis simulation

---

## ⚙️ Implementation Flow

- dataset তৈরি করা হয়েছে
- mean, median, std calculate করা হয়েছে
- distribution compare করা হয়েছে
- boxplot দিয়ে data spread দেখা হয়েছে
- real dataset analysis করা হয়েছে
- statistical insights visualize করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Mean overall average trend দেখায়
- Median outlier-resistant central value
- Standard deviation data spread বোঝায়
- Histogram distribution comparison সহজ করে
- Boxplot compact statistical summary দেয়

---

## 🚀 What I Learned

- mean, median, std concept visualization
- data distribution analysis
- boxplot interpretation
- statistical annotation usage
- real dataset analysis workflow

---

## 🧠 Key Concepts (Quick Revision)

- `np.mean()` → average
- `np.median()` → middle value
- `np.std()` → spread
- `plt.axhline()` → horizontal reference line
- `plt.boxplot()` → statistical summary
- histogram → distribution view

---

## 📝 Notes

- outlier mean heavily affect করে
- median more stable metric
- std shows variability
- visualization makes stats intuitive

---

## 📌 Next Day Preview

- Heatmap basics
- Correlation matrix
- Color intensity visualization
- Data relationship mapping

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- automatic grade classification system
- performance ranking dashboard
- outlier detection visualization
- student comparison tool

### 🧪 Practice Ideas

- class performance analyze করো
- two group A/B test visualization করো
- top student highlight system বানাও
- dataset normalize করে compare করো

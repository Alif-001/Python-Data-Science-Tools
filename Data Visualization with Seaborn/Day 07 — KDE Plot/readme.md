# 📅 Day 7 — KDE Plot

---

# 🎯 Objective

- `sns.kdeplot()` ব্যবহার শেখা
- Density estimation বোঝা
- Smooth distribution curve visualize করা
- `fill=True` ব্যবহার শেখা
- Multiple KDE comparison করা
- Bandwidth concept বোঝা
- KDE vs Histogram difference analyze করা

---

# 📚 Topics Covered

- `sns.kdeplot()`
- Density estimation
- Smooth distribution
- `fill=True`
- Multiple KDE plots
- Bandwidth understanding

---

# 📁 Project Structure

```bash id="a7v9p2"
day-7/
│── 01_basic_kdeplot.py
│── 02_density_understanding.py
│── 03_filled_kde.py
│── 04_multiple_kde.py
│── 05_filled_multiple_kde.py
│── 06_bandwidth_understanding.py
│── 07_kde_vs_hist.py
│── README.md
```

---

# 📊 Dataset

## 📌 Dataset Name: `tips`

- **Source:** Built-in Seaborn Dataset
- **Loaded Using:** `sns.load_dataset("tips")`

---

## 📌 Description

Restaurant tipping dataset যেখানে customer bill, tip amount, smoker status এবং gender related information রয়েছে।

---

## 📌 Columns

- `total_bill` → মোট bill amount
- `tip` → tip amount
- `sex` → customer gender
- `smoker` → smoker/non-smoker
- `day` → week day
- `time` → lunch/dinner
- `size` → group size

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_basic_kdeplot.py

## 🔹 Purpose

- Basic KDE plot তৈরি করা
- Smooth distribution visualization শেখা

---

## 🧾 Code

```python id="m8r4tz"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.kdeplot(
    data=tips,
    x="total_bill"
)

plt.title("KDE Plot of Total Bill")

plt.show()
```

---

## 🧠 Explanation

- `sns.kdeplot()`
  - Smooth density curve তৈরি করে

- `x="total_bill"`
  - Bill distribution analyze করে

- Histogram এর smooth version visualize করা হয়

---

## 📌 Key Idea

- KDE = smooth distribution curve

---

# 📄 2. 02_density_understanding.py

## 🔹 Purpose

- Density estimation concept বোঝা
- Data concentration analyze করা

---

## 🧾 Code

```python id="v2x6jq"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.kdeplot(
    data=tips,
    x="tip"
)

plt.title("Tip Distribution (Density)")

plt.show()
```

---

## 🧠 Explanation

- KDE দেখায়:
  - কোথায় data বেশি concentrated

- High peak:
  - অনেক values ঐ range এ রয়েছে

- Low area:
  - কম values রয়েছে

---

## 📌 Key Idea

- KDE = probability density visualization

---

# 📄 3. 03_filled_kde.py

## 🔹 Purpose

- Filled KDE plot তৈরি করা
- Better visual understanding তৈরি করা

---

## 🧾 Code

```python id="n4f7yd"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.kdeplot(
    data=tips,
    x="total_bill",
    fill=True
)

plt.title("Filled KDE Plot")

plt.show()
```

---

## 🧠 Explanation

- `fill=True`
  - Curve এর নিচের area fill করে

- Visualization আরও readable হয়

- Smooth histogram feel পাওয়া যায়

---

## 📌 Key Idea

- Filled KDE visually বেশি attractive ও understandable

---

# 📄 4. 04_multiple_kde.py

## 🔹 Purpose

- Multiple KDE comparison করা
- `hue` ব্যবহার শেখা

---

## 🧾 Code

```python id="s6q8wl"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.kdeplot(
    data=tips,
    x="total_bill",
    hue="sex",
    fill=False
)

plt.title("KDE Comparison: Male vs Female")

plt.show()
```

---

## 🧠 Explanation

- `hue="sex"`
  - Male/Female আলাদা curve এ দেখায়

- Different distributions compare করা যায়

---

## 📌 Key Idea

- Multiple KDE = group distribution comparison

---

# 📄 5. 05_filled_multiple_kde.py

## 🔹 Purpose

- Filled group KDE visualization তৈরি করা
- Transparency ব্যবহার শেখা

---

## 🧾 Code

```python id="k5t1mc"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.kdeplot(
    data=tips,
    x="total_bill",
    hue="smoker",
    fill=True,
    alpha=0.5
)

plt.title("Smoker vs Non-Smoker KDE")

plt.show()
```

---

## 🧠 Explanation

- `fill=True`
  - Filled KDE তৈরি করে

- `alpha=0.5`
  - Transparency control করে

- Overlapping areas সহজে দেখা যায়

---

## 📌 Key Idea

- Transparency overlap comparison সহজ করে

---

# 📄 6. 06_bandwidth_understanding.py

## 🔹 Purpose

- Bandwidth concept বোঝা
- Curve smoothness control করা

---

## 🧾 Code

```python id="z1u4rb"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.kdeplot(
    data=tips,
    x="total_bill",
    bw_adjust=0.3
)

plt.title("Low Bandwidth (Sharp Curve)")

plt.show()

sns.kdeplot(
    data=tips,
    x="total_bill",
    bw_adjust=2
)

plt.title("High Bandwidth (Smooth Curve)")

plt.show()
```

---

## 🧠 Explanation

- `bw_adjust=0.3`
  - কম smoothing করে
  - More detailed curve

- `bw_adjust=2`
  - বেশি smoothing করে
  - Smooth curve তৈরি করে

---

## 📌 Key Idea

- Low bandwidth → detailed but noisy
- High bandwidth → smooth but less detailed

---

# 📄 7. 07_kde_vs_hist.py

## 🔹 Purpose

- KDE ও Histogram compare করা
- Distribution understanding improve করা

---

## 🧾 Code

```python id="q9w2xh"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.histplot(
    data=tips,
    x="total_bill",
    kde=True
)

plt.title("Histogram + KDE Together")

plt.show()
```

---

## 🧠 Explanation

- Histogram:
  - Raw frequency দেখায়

- KDE:
  - Smooth distribution shape দেখায়

- দুইটি একসাথে ব্যবহার করলে better understanding পাওয়া যায়

---

## 📌 Key Idea

- Histogram + KDE = complete distribution understanding

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Basic KDE plot তৈরি করা হয়েছে
- Density estimation analyze করা হয়েছে
- Filled KDE visualization তৈরি করা হয়েছে
- Multiple KDE comparison করা হয়েছে
- Transparency apply করা হয়েছে
- Bandwidth tuning করা হয়েছে
- Histogram ও KDE compare করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- KDE smooth distribution understanding improve করে
- Density curves data concentration বুঝতে সাহায্য করে
- Filled KDE visually বেশি clear
- Multiple KDE group comparison সহজ করে
- Bandwidth curve smoothness control করে
- Histogram + KDE combination powerful visualization তৈরি করে

---

# 🚀 What I Learned

- `sns.kdeplot()`
- Density estimation
- Smooth distribution analysis
- Filled KDE visualization
- Multiple KDE comparison
- Transparency control
- Bandwidth adjustment
- KDE vs Histogram analysis

---

# 🧠 Key Concepts (Quick Revision)

- KDE → Kernel Density Estimation
- Density → probability concentration
- `fill=True` → filled curve
- `alpha` → transparency control
- `hue` → group comparison
- `bw_adjust` → smoothness control

---

# 📝 Notes

## 📌 Common Mistakes

- Very low bandwidth ব্যবহার করা
- Too much smoothing করা
- Small dataset এ misleading KDE তৈরি হওয়া
- Histogram ছাড়া শুধু KDE interpret করা

---

## 📌 Optimization Tips

- Histogram + KDE একসাথে ব্যবহার করো
- Group comparison এ `hue` ব্যবহার করো
- Overlap এ `alpha` ব্যবহার করো
- Balanced bandwidth নির্বাচন করো

---

# 📌 Next Day Preview

## 📅 Day 8 — Distribution Plot Family

আগামী দিনে শিখবো:

- `sns.displot()`
- Histogram + KDE
- Figure-level distribution plots
- Faceted distributions
- Distribution comparison

---

# ⭐ Bonus (Optional)

## 🔥 Improvement Ideas

- Customer spending density analysis করা
- Salary distribution KDE visualization তৈরি করা
- Stock market price density analyze করা
- Multi-category KDE dashboard তৈরি করা

---

## 🧪 Practice Ideas

- `penguins` dataset এ KDE plot তৈরি করো
- Different `bw_adjust` values compare করো
- Filled vs non-filled KDE compare করো
- Histogram + KDE combinations তৈরি করো

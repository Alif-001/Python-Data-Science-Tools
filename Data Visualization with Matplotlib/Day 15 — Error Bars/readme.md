# 📅 Day 15 — Error Bars

## 🎯 Objective

- আজকে Error Bar concept শিখবো
- Data uncertainty এবং variation বুঝতে শিখবো
- Standard deviation visualize করা শিখবো
- Confidence interval ধারণা শিখবো
- Scientific plotting system ব্যবহার করা শিখবো
- Real experiment data analyze করা শিখবো

---

## 📚 Topics Covered

- Error bar basics
- Standard deviation
- Confidence interval concept
- Error visualization
- Scientific plotting

---

## 📁 Project Structure

```bash id="day15"
day-15/
│── 01_basic_error_bar.py
│── 02_standard_deviation.py
│── 03_confidence_interval.py
│── 04_error_visualization.py
│── 05_scientific_plotting.py
│── 06_real_error_bar.py
│── experiment_data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** experiment_data.csv
- **Description:** Experimental trial data with measurement values and uncertainty (error)

### Columns:

- trial → Experiment trial number
- value → Measured value
- error → Measurement uncertainty

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. main.py

### 🔹 Purpose

- Error bar concept introduction
- Uncertainty visualization idea বোঝা

### 🧾 Code

```python id="main15"
print("Day 15 - Error Bars 📊")
```

### 🧠 Explanation

- Error bar = data uncertainty visualization
- Real-world measurements কখনো exact হয় না

---

## 📄 2. analysis.py

### 🔹 Purpose

- Error statistics analysis

### 🧾 Code

```python id="analysis15"
def avg_error(errors):
    return sum(errors) / len(errors)
```

### 🧠 Explanation

- Average error calculate করে
- Data reliability বুঝতে সাহায্য করে

---

## 📄 3. utils.py

### 🔹 Purpose

- Helper functions

### 🧾 Code

```python id="utils15"
def format_value(v):
    return round(v, 2)
```

### 🧠 Explanation

- Value clean format করে
- Visualization consistent রাখে

---

## 📄 4. 01_basic_error_bar.py

### 🔹 Purpose

- Basic error bar visualization

### 🧾 Code

```python id="eb1"
plt.errorbar(x, y, yerr=error, fmt='o', capsize=5)
```

### 🧠 Explanation

- `yerr` → error values show করে
- `capsize` → error bar line endings control করে
- Data uncertainty visualize করা হয়

---

## 📄 5. 02_standard_deviation.py

### 🔹 Purpose

- Standard deviation visualization

### 🧾 Code

```python id="eb2"
std = np.std(y)
plt.errorbar(x, y, yerr=std)
```

### 🧠 Explanation

- Data spread around mean দেখায়
- Consistent error apply করা হয়

---

## 📄 6. 03_confidence_interval.py

### 🔹 Purpose

- Confidence interval visualization

### 🧾 Code

```python id="eb3"
ci = 2
plt.errorbar(x, y, yerr=ci)
```

### 🧠 Explanation

- True value range estimate করা হয়
- Statistical uncertainty represent করে

---

## 📄 7. 04_error_visualization.py

### 🔹 Purpose

- Real-world measurement error visualize করা

### 🧾 Code

```python id="eb4"
plt.errorbar(time, temperature, yerr=error)
```

### 🧠 Explanation

- Temperature measurement variability দেখানো হয়
- Time-based experiment analysis করা হয়

---

## 📄 8. 05_scientific_plotting.py

### 🔹 Purpose

- Scientific experiment plotting

### 🧾 Code

```python id="eb5"
plt.errorbar(x, y, yerr=error, fmt='o-')
```

### 🧠 Explanation

- Research-level plotting style
- Line + error combined visualization

---

## 📄 9. 06_real_error_bar.py

### 🔹 Purpose

- Real experimental dataset analysis

### 🧾 Code

```python id="eb6"
import csv

with open("experiment_data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        trial.append(int(row["trial"]))
        value.append(int(row["value"]))
        error.append(float(row["error"]))

plt.errorbar(trial, value, yerr=error)
```

### 🧠 Explanation

- CSV থেকে experimental data load করা হয়েছে
- Trial-wise measurement + error visualize করা হয়েছে
- Real-world uncertainty analysis করা হয়েছে

---

## ⚙️ Implementation Flow

- Error bar concept শেখা হয়েছে
- Standard deviation visualize করা হয়েছে
- Confidence interval বোঝা হয়েছে
- Scientific plotting করা হয়েছে
- Real experimental data analyze করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Error bar data uncertainty দেখায়
- Standard deviation data spread বুঝায়
- Confidence interval range estimate করে
- Scientific plots research-level visualization দেয়
- Real experiment data analysis সহজ হয়

---

## 🚀 What I Learned

- Error bar concept (`yerr`)
- Standard deviation usage
- Confidence interval idea
- Scientific plotting style
- Real experimental analysis

---

## 🧠 Key Concepts (Quick Revision)

- `errorbar()` → main function
- `yerr` → uncertainty value
- `std` → data spread
- `confidence interval` → range estimate
- `capsize` → error bar styling

---

## 📝 Notes

- Error bars always approximate value show করে
- Too large error = unreliable data
- Scientific plots should be clean and readable
- Proper scaling important
- Overlapping error bars avoid করা উচিত

---

## 📌 Next Day Preview

- Heatmap visualization
- Matrix data plotting
- Correlation analysis
- Color intensity mapping
- Data relationships visualization

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Auto error calculator system
- Scientific report generator
- Experiment analysis dashboard
- Smart uncertainty detector

### 🧪 Practice Ideas

- Lab experiment result analyzer
- Temperature variation study
- Stock price uncertainty visualization
- Survey result confidence analysis

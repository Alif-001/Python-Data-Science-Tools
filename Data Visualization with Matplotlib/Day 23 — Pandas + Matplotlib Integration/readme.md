# 📅 Day 23 — Pandas + Matplotlib Integration

## 🎯 Objective

- আজকে Pandas DataFrame থেকে সরাসরি plot করা শিখবো
- CSV data workflow practice করবো
- Index-based plotting এবং multi-column comparison শিখবো
- Real-world data cleaning + visualization pipeline বুঝবো

---

## 📚 Topics Covered

- Plot directly from DataFrame
- Index plotting
- Grouped plotting
- CSV visualization workflow

---

## 📁 Project Structure

```bash
day-23/
│── 01_dataframe_plot_basic.py
│── 02_index_plotting.py
│── 03_multi_column_plot.py
│── 04_grouped_plotting.py
│── 05_csv_workflow_basic.py
│── 06_cleaning_and_plotting.py
│── sales_data.csv
│── sales_data_dirty.csv
│── README.md
```

---

## 📊 Dataset

### 📄 File Name: `sales_data.csv`

- **Description:** Clean daily sales dataset used for time series plotting

#### Columns:

- `date` → Sales date
- `sales` → Sales amount

---

### 📄 File Name: `sales_data_dirty.csv`

- **Description:** Dirty dataset with missing values for cleaning practice

#### Columns:

- `date` → Sales date
- `sales` → Sales amount (some missing values present)

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `main.py` (Concept Entry)

### 🔹 Purpose

- Pandas + Matplotlib integration concept বোঝা
- DataFrame-based plotting idea introduce করা

### 🧾 Code

```python
print("Day 23 - Pandas + Matplotlib Integration 📊")
```

### 🧠 Explanation

- Pandas DataFrame directly visualization support করে
- Manual list extraction ছাড়াই plot করা যায়

---

## 📄 2. `analysis.py`

### 🔹 Purpose

- Data understanding and inspection

### 🧾 Code

```python
def summarize_data(df):
    return df.describe()
```

### 🧠 Explanation

- Dataset summary generate করে
- Basic statistical overview দেয়

---

## 📄 3. `utils.py`

### 🔹 Purpose

- Helper functions for data processing

### 🧾 Code

```python
def clean_column(col):
    return col.fillna(method="ffill")
```

### 🧠 Explanation

- Missing values fill করতে সাহায্য করে
- Reusable cleaning logic

---

## 📄 4. `01_dataframe_plot_basic.py`

### 🔹 Purpose

- Basic DataFrame plotting শেখা

### 🧠 Explanation

- Dictionary থেকে DataFrame তৈরি করা হয়েছে
- `df.plot(x="day", y="sales")` ব্যবহার করা হয়েছে
- Pandas internally Matplotlib use করে plotting করে

---

## 📄 5. `02_index_plotting.py`

### 🔹 Purpose

- Index-based plotting শেখা

### 🧠 Explanation

- DataFrame index automatically X-axis হিসেবে use হয়
- `df.plot()` দিলে index-based chart তৈরি হয়
- Simple dataset visualization বোঝায়

---

## 📄 6. `03_multi_column_plot.py`

### 🔹 Purpose

- Multiple columns একসাথে plot করা

### 🧠 Explanation

- Sales এবং profit একসাথে compare করা হয়েছে
- `y=["sales", "profit"]` দিয়ে multi-line chart তৈরি হয়েছে
- Business comparison visualization সহজ হয়

---

## 📄 7. `04_grouped_plotting.py`

### 🔹 Purpose

- Category-based comparison plot করা

### 🧠 Explanation

- Product A vs Product B sales compare করা হয়েছে
- Multiple series একসাথে plot করা হয়েছে
- Group analysis visualization তৈরি হয়েছে

---

## 📄 8. `05_csv_workflow_basic.py`

### 🔹 Purpose

- Real CSV workflow শেখা

### 🧠 Explanation

- `pd.read_csv()` দিয়ে data load করা হয়েছে
- `df.head()` দিয়ে preview দেখা হয়েছে
- Direct DataFrame plotting করা হয়েছে
- Real-world data pipeline বুঝানো হয়েছে

---

## 📄 9. `06_cleaning_and_plotting.py`

### 🔹 Purpose

- Dirty data cleaning + visualization

### 🧠 Explanation

- Missing values dataset load করা হয়েছে
- `pd.to_datetime()` দিয়ে date format fix করা হয়েছে
- `fillna(method="ffill")` দিয়ে missing value handle করা হয়েছে
- Clean data plot করা হয়েছে

---

## ⚙️ Implementation Flow

- DataFrame তৈরি/লোড করা হয়েছে
- Basic plotting শেখা হয়েছে
- Multi-column comparison করা হয়েছে
- CSV workflow practice করা হয়েছে
- Dirty data clean করে visualize করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Pandas plotting খুব fast এবং easy
- Index automatically X-axis হিসেবে কাজ করে
- Multiple columns compare করা সহজ
- Real CSV workflow industry standard
- Data cleaning visualization quality improve করে

---

## 🚀 What I Learned

- DataFrame plotting system
- Index-based visualization
- Multi-series comparison
- CSV workflow handling
- Basic data cleaning before plotting

---

## 🧠 Key Concepts (Quick Revision)

- `df.plot()` → direct plotting
- `x=` → X-axis define করে
- `y=` → Y-axis column select করে
- index → automatic X-axis
- `read_csv()` → real dataset load
- `fillna()` → missing data fix

---

## 📝 Notes

- Clean data না হলে plot misleading হতে পারে
- Multi-column plot খুব powerful for comparison
- Pandas plotting internally Matplotlib use করে
- Large dataset optimize করা দরকার

---

## 📌 Next Day Preview

- NumPy + Matplotlib integration
- Mathematical function plotting
- Simulation-based graphs
- Scientific visualization basics

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Auto dashboard generator from CSV
- Multiple dataset comparison tool
- Real-time CSV plotting system
- Smart cleaning pipeline

### 🧪 Practice Ideas

- Sales vs profit dashboard বানাও
- Dirty dataset clean করে plot করো
- Multi-product comparison chart তৈরি করো
- Monthly report visualization বানাও

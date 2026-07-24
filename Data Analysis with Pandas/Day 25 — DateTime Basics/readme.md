# 📅 Day 25 — DateTime Basics

---

## 🎯 Objective

- Pandas এ date/time data handle করা শেখা
- string date কে real datetime format এ convert করা
- year, month, day extract করা
- time-based analysis (trend, grouping) করা
- real-world HR/date analytics practice করা

---

## 📚 Topics Covered

- `pd.to_datetime()`
- `.dt.year`
- `.dt.month`
- `.dt.day`
- datetime feature extraction
- time-based grouping
- sorting by date

---

## 📁 Project Structure

```id="d25proj"
day-25/
│── 01_to_datetime.py
│── 02_extract_year.py
│── 03_extract_month.py
│── 04_extract_day.py
│── 05_all_datetime_features.py
│── 06_real_world_datetime.py
│── data.csv
│── README.md
```

---

## 📊 Dataset

### 📄 File Name: data.csv

- **Description:** Employee join date based dataset

- **Columns:**
  - Name → employee name
  - JoinDate → joining date (string format initially)
  - Salary → monthly salary

👉 Note: `JoinDate` প্রথমে string ছিল, পরে datetime এ convert করা হয়েছে

---

# 💻 Code Breakdown (File by File)

---

## 📄 1. main.py (Concept Entry File)

### 🔹 Purpose

- datetime learning module start করা

### 🧾 Code

```python id="dt25main"
print("Day 25 - DateTime Basics Learning")
```

### 🧠 Explanation

- simple entry file
- project initialization indicator

---

## 📄 2. 01_to_datetime.py

### 🔹 Purpose

- string date → datetime object convert করা

### 🧾 Code

```python id="dt25a"
df['JoinDate'] = pd.to_datetime(df['JoinDate'])
```

### 🧠 Explanation

- আগে date ছিল string format
- এখন proper datetime object
- time-based operations possible হয়

---

## 📄 3. 02_extract_year.py

### 🔹 Purpose

- year extract করা

### 🧾 Code

```python id="dt25b"
df['Year'] = df['JoinDate'].dt.year
```

### 🧠 Explanation

- `.dt.year` → শুধু year part বের করে
- yearly analysis possible হয়

---

## 📄 4. 03_extract_month.py

### 🔹 Purpose

- month extract করা

### 🧾 Code

```python id="dt25c"
df['Month'] = df['JoinDate'].dt.month
```

### 🧠 Explanation

- `.dt.month` → month number (1–12)
- seasonal analysis করা যায়

---

## 📄 5. 04_extract_day.py

### 🔹 Purpose

- day extract করা

### 🧾 Code

```python id="dt25d"
df['Day'] = df['JoinDate'].dt.day
```

### 🧠 Explanation

- `.dt.day` → date of month (1–31)
- fine-grained date analysis

---

## 📄 6. 05_all_datetime_features.py

### 🔹 Purpose

- multiple datetime feature extraction

### 🧾 Code

```python id="dt25e"
df['Year'] = df['JoinDate'].dt.year
df['Month'] = df['JoinDate'].dt.month
df['Day'] = df['JoinDate'].dt.day
```

### 🧠 Explanation

- একসাথে full date breakdown করা যায়
- feature engineering step শুরু হয়

---

## 📄 7. 06_real_world_datetime.py

### 🔹 Purpose

- real-world time-based analysis

### 🧾 Code

```python id="dt25f"
df['Year'] = df['JoinDate'].dt.year
yearly_salary = df.groupby('Year')['Salary'].mean()
latest = df.sort_values(by='JoinDate', ascending=False)
```

### 🧠 Explanation

- yearly salary trend analysis
- latest employees sorting
- HR analytics workflow

---

## ⚙️ Implementation Flow

- dataset load করা হয়েছে
- string date → datetime convert করা হয়েছে
- year/month/day extract করা হয়েছে
- grouping করা হয়েছে
- sorting applied করা হয়েছে
- insights generate করা হয়েছে

---

## 📈 Output / Result

- proper datetime format তৈরি হয়েছে
- yearly salary trend পাওয়া গেছে
- latest employees list তৈরি হয়েছে
- time-based analysis possible হয়েছে

---

## 🚀 What I Learned

- datetime = time-based analysis backbone
- string date usable না → convert করতে হয়
- `.dt` accessor = date feature extraction tool
- grouping by time = powerful business insight
- sorting by date = real-world reporting

---

## 🧠 Key Concepts (Quick Revision)

- `to_datetime()` → string → datetime
- `.dt.year` → year extract
- `.dt.month` → month extract
- `.dt.day` → day extract
- `groupby(time)` → trend analysis
- `sort_values(date)` → timeline sorting

---

## 📝 Notes

- date format error = common real-world issue
- always convert before analysis
- datetime = analytics + ML feature engineering core

---

## 📌 Next Day Preview

👉 Day 26 — Time Difference

- timedelta concept
- date subtraction
- duration calculation
- employee experience analysis

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- employee experience calculator
- hiring trend dashboard

### 🧪 Practice Ideas

- join date থেকে experience calculate করো
- monthly hiring trend বের করো

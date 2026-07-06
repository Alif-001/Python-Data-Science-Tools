# 📅 Day 18 — Iteration + Final Integration 🚀

---

## 🎯 Objective

- NumPy iteration concept (nditer) ভালোভাবে বোঝা
- axis-wise iteration practice করা
- performance difference (loop vs NumPy) দেখা
- full data workflow (create → filter → reshape → analyze → summarize) build করা
- real-world data science style pipeline practice করা

---

## 📚 Topics Covered

- nditer (element-wise iteration)
- axis-wise iteration (row / column)
- performance comparison (loop vs vectorization)
- boolean filtering
- reshape concept
- full workflow integration

---

## 📁 Project Structure

```bash
day-18/
│── 01_nditer_basic.py
│── 02_nditer_3d.py
│── 03_axis_iteration.py
│── 04_performance_iteration.py
│── 05_full_workflow.py
│── 06_real_world_pipeline.py
│── README.md
```

---

## 📊 Dataset

- File Name: data.csv
- Description: এই project এ কোনো fixed dataset ব্যবহার করা হয়নি। সবকিছু NumPy generated data এবং simulated values দিয়ে করা হয়েছে।
- Columns:
  - column1 → simulated numerical values
  - column2 → N/A

---

## 💻 Code Breakdown (File by File)

---

### 📄 1. 01_nditer_basic.py

#### 🔹 Purpose

- 2D array-এর সব element একে একে iterate করা

#### 🧾 Code

```python id="d18m1"
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

for x in np.nditer(arr):
    print(x)
```

#### 🧠 Explanation

- Line 1 → NumPy import করা হয়েছে
- Line 3-6 → 2D array তৈরি
- Line 8 → প্রতিটি element iterate করা হচ্ছে
- Logic → পুরো array flatten-like ভাবে traverse হয়

---

### 📄 2. 02_nditer_3d.py

#### 🔹 Purpose

- 3D array iteration শেখা

#### 🧾 Code

```python id="d18m2"
import numpy as np

arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

for x in np.nditer(arr):
    print(x)
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3-6 → 3D array তৈরি
- Line 8 → সব element flatten হয়ে iterate হয়
- Logic → nditer multi-dimensional structure handle করে

---

### 📄 3. 03_axis_iteration.py

#### 🔹 Purpose

- row-wise এবং column-wise iteration বোঝা

#### 🧾 Code

```python id="d18m3"
import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Row-wise:")
for row in arr:
    print(row)

print("Column-wise:")
for col in arr.T:
    print(col)
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3-6 → matrix তৈরি
- Line 8-10 → row-wise iteration
- Line 13-15 → transpose ব্যবহার করে column-wise iteration
- Logic → `.T` rows ↔ columns swap করে

---

### 📄 4. 04_performance_iteration.py

#### 🔹 Purpose

- Python loop vs NumPy performance compare করা

#### 🧾 Code

```python id="d18m4"
import numpy as np
import time

arr = np.arange(1, 1000000)

start = time.time()

result = []
for x in arr:
    result.append(x * 2)

end = time.time()

print("Loop time:", end - start)

start = time.time()

result_np = arr * 2

end = time.time()

print("NumPy time:", end - start)
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 2 → time module import
- Line 4 → large array তৈরি
- Line 6-12 → Python loop timing
- Line 14-18 → NumPy vectorization timing
- Logic → NumPy C backend ব্যবহার করে, তাই অনেক faster

---

### 📄 5. 05_full_workflow.py

#### 🔹 Purpose

- full data workflow practice (real analysis flow)

#### 🧾 Code

```python id="d18m5"
import numpy as np

marks = np.array([45, 60, 75, 30, 90, 50, 80])

print("Original Data:", marks)

passed = marks[marks >= 50]
failed = marks[marks < 50]

print("Passed:", passed)
print("Failed:", failed)

reshaped = marks.reshape(7, 1)

print("Reshaped:")
print(reshaped)

print("Mean:", np.mean(marks))
print("Max:", np.max(marks))
print("Min:", np.min(marks))
print("Std:", np.std(marks))

print("\nSUMMARY:")
print("Total Students:", len(marks))
print("Passed Students:", len(passed))
print("Failed Students:", len(failed))
print("Average Score:", np.mean(marks))
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3 → marks data তৈরি
- Line 5-8 → filtering (pass/fail)
- Line 10-12 → reshape করা
- Line 14-17 → statistics
- Line 19-22 → summary output
- Logic → end-to-end mini analysis pipeline

---

### 📄 6. 06_real_world_pipeline.py

#### 🔹 Purpose

- real-world data science pipeline simulation

#### 🧾 Code

```python id="d18m6"
import numpy as np

data = np.random.randint(0, 100, 20)

print("Data:", data)

clean = data[data >= 40]

print("Clean Data:", clean)

normalized = clean / 100

print("Normalized:", normalized)

print("Mean:", np.mean(clean))
print("Max:", np.max(clean))
print("Min:", np.min(clean))

print("\nINSIGHT:")
print("Total:", len(data))
print("Valid:", len(clean))
print("Failure Rate:", (len(data) - len(clean)) / len(data))
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3 → random dataset তৈরি
- Line 5 → filtering (clean data)
- Line 8 → normalization
- Line 11-13 → statistics
- Line 15-18 → business insight
- Logic → real ML/data pipeline structure simulate করা

---

## ⚙️ Implementation Flow

- random / manual dataset তৈরি করা হয়েছে
- nditer দিয়ে element-wise iteration করা হয়েছে
- row-wise এবং column-wise traversal শেখা হয়েছে
- loop vs vectorization performance comparison করা হয়েছে
- full workflow (filter → reshape → analyze → summarize) build করা হয়েছে
- real-world pipeline simulation করা হয়েছে

---

## 📈 Output / Result

- iteration concept clear হয়েছে
- performance difference বোঝা গেছে
- NumPy workflow mindset তৈরি হয়েছে
- data analysis pipeline structure শেখা গেছে
- real-world ML preprocessing flow বুঝতে সাহায্য করেছে

---

## 🚀 What I Learned

- nditer → efficient iteration tool
- transpose → axis swap concept
- NumPy loop replace করে performance boost দেয়
- data pipeline step-by-step build করা যায়
- filtering + stats = analysis core

---

## 🧠 Key Concepts (Quick Revision)

- nditer → element-wise iteration
- .T → transpose
- vectorization → fast computation
- loop → slow approach
- boolean filtering → data cleaning
- reshape → structure change
- pipeline → end-to-end flow

---

## 📝 Notes

- বড় dataset এ loop avoid করা best practice
- nditer debugging + exploration এর জন্য useful
- real ML pipeline always follow: clean → transform → analyze
- NumPy is foundation for data science

---

## 📌 Next Day Preview

- final revision of NumPy concepts
- advanced mini project
- interview-style questions practice
- full NumPy recap

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- mini data analysis project build করা
- marks prediction simple model flow add করা

### 🧪 Practice Ideas

- নিজের dataset create করে full pipeline run করো
- filtering + reshape + stats combine করে experiment করো

# 📅 Day 17 — Random + Math + Linear Algebra

## 🎯 Objective

- আজকে NumPy-এর random, math, এবং linear algebra concept শেখা
- reproducible randomness বোঝা
- log, exp, trig functions practice করা
- matrix multiplication, transpose, এবং dot product clear করা

---

## 📚 Topics Covered

- rand, randint, uniform
- seed
- log, log10, exp
- sin, cos, tan
- matrix multiplication
- transpose
- dot product

---

## 📁 Project Structure

```bash
day-17/
│── 01_random_basic.py
│── 02_random_seed.py
│── 03_math_log_exp.py
│── 04_trigonometry.py
│── 05_matrix_multiplication.py
│── 06_transpose.py
│── 07_dot_product.py
│── 08_linear_algebra_combined.py
│── README.md
```

---

## 📊 Dataset

- File Name: data.csv
- Description: এই day-তে কোনো external dataset ব্যবহার করা হয়নি। সবকিছু NumPy random, math, এবং linear algebra practice-এর জন্য manually তৈরি করা হয়েছে
- Columns:
  - column1 → simulated numerical values
  - column2 → N/A

---

## 💻 Code Breakdown (File by File)

### 📄 1. 01_random_basic.py

#### 🔹 Purpose

- random number generation শেখা
- random float, integer, এবং uniform distribution practice করা

#### 🧾 Code

```python
import numpy as np

print(np.random.rand(3))
print(np.random.randint(1, 10, 5))
print(np.random.uniform(10, 20, 5))
```

#### 🧠 Explanation

- Line 1 → NumPy import করা হয়েছে
- Line 4 → 0 থেকে 1 এর মধ্যে 3টা random float তৈরি
- Line 7 → 1 থেকে 9 এর মধ্যে 5টা random integer তৈরি
- Line 10 → 10 থেকে 20 এর মধ্যে 5টা float value তৈরি
- Logic → random data generation অনেক analysis task-এ লাগে

---

### 📄 2. 02_random_seed.py

#### 🔹 Purpose

- reproducible randomness বোঝা
- seed ব্যবহার করে same output বারবার পাওয়া

#### 🧾 Code

```python
import numpy as np

np.random.seed(42)

print(np.random.rand(3))
```

#### 🧠 Explanation

- Line 1 → NumPy import করা হয়েছে
- Line 4 → seed fixed করা হয়েছে
- Line 6 → same random output repeat হবে
- Logic → ML experiment এবং testing-এর জন্য reproducibility খুব important

---

### 📄 3. 03_math_log_exp.py

#### 🔹 Purpose

- log এবং exponential function practice করা

#### 🧾 Code

```python
import numpy as np

arr = np.array([1, 10, 100, 1000])

print(np.log(arr))
print(np.log10(arr))
print(np.exp([1, 2, 3]))
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3 → numeric array তৈরি
- Line 5 → natural log calculate
- Line 6 → base 10 log calculate
- Line 9 → exponential values calculate
- Logic → math operations array-এর উপর directly করা যায়

---

### 📄 4. 04_trigonometry.py

#### 🔹 Purpose

- trigonometric functions শেখা
- radians-based calculation বোঝা

#### 🧾 Code

```python
import numpy as np

arr = np.array([0, np.pi/2, np.pi])

print(np.sin(arr))
print(np.cos(arr))
print(np.tan(arr))
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3 → radians in array
- Line 5 → sine values
- Line 6 → cosine values
- Line 7 → tangent values
- Logic → trigonometry-এর জন্য radians use করতে হয়

---

### 📄 5. 05_matrix_multiplication.py

#### 🔹 Purpose

- matrix multiplication শেখা
- `np.matmul()` এবং `@` operator ব্যবহার করা

#### 🧾 Code

```python
import numpy as np

a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [5, 6],
    [7, 8]
])

print(np.matmul(a, b))
print(a @ b)
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3-9 → দুইটা matrix তৈরি
- Line 11 → `np.matmul()` দিয়ে multiplication
- Line 14 → `@` operator দিয়ে same কাজ
- Logic → `*` নয়, matrix multiplication-এর জন্য `@` ব্যবহার করতে হয়

---

### 📄 6. 06_transpose.py

#### 🔹 Purpose

- transpose concept বোঝা
- rows আর columns swap হওয়া দেখা

#### 🧾 Code

```python
import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(arr.T)
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3-6 → 2D array তৈরি
- Line 8 → transpose print করা হয়েছে
- Logic → `.T` rows এবং columns swap করে

---

### 📄 7. 07_dot_product.py

#### 🔹 Purpose

- dot product শেখা
- vector multiplication concept বোঝা

#### 🧾 Code

```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.dot(a, b))
print(a @ b)
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3-4 → two vectors
- Line 6 → dot product calculation
- Line 9 → একই কাজ `@` operator দিয়ে
- Logic → vector operation এবং linear algebra-তে dot product fundamental

---

### 📄 8. 08_linear_algebra_combined.py

#### 🔹 Purpose

- সব linear algebra concept একসাথে practice করা
- matrix multiplication, transpose, dot product combine করা

#### 🧾 Code

```python
import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [2, 0],
    [1, 2]
])

C = A @ B
print("Matrix Multiplication:\n", C)

print("Transpose:\n", A.T)

v1 = np.array([1, 2])
v2 = np.array([3, 4])

print("Dot Product:", np.dot(v1, v2))
```

#### 🧠 Explanation

- Line 1 → NumPy import
- Line 3-10 → দুইটা matrix তৈরি
- Line 12 → matrix multiplication
- Line 15 → transpose print করা হয়েছে
- Line 17-20 → dot product example
- Logic → linear algebra workflow clear করা হয়েছে

---

## ⚙️ Implementation Flow

- random data generation করা হয়েছে
- seed দিয়ে reproducibility দেখা হয়েছে
- log, exp, trig functions practice করা হয়েছে
- matrix multiplication এবং transpose শেখা হয়েছে
- dot product concept clear করা হয়েছে
- combined linear algebra workflow practice করা হয়েছে

---

## 📈 Output / Result

- random number generation skill build হয়েছে
- math functions array-এর উপর ব্যবহার করা শিখা গেছে
- linear algebra operations clear হয়েছে
- ML-ready mathematical foundation তৈরি হয়েছে

---

## 🚀 What I Learned

- random data generate করা যায়
- seed দিলে same output repeat হয়
- log এবং exp array-based compute করা যায়
- trigonometry radians-based
- matrix multiplication আর dot product fundamental linear algebra concept

---

## 🧠 Key Concepts (Quick Revision)

- `np.random.rand()` → 0 to 1 float
- `np.random.randint()` → integer range
- `np.random.uniform()` → float range
- `np.random.seed()` → reproducibility
- `np.log()`, `np.log10()`, `np.exp()` → math functions
- `np.sin()`, `np.cos()`, `np.tan()` → trig functions
- `@` → matrix multiplication
- `np.dot()` → dot product
- `.T` → transpose

---

## 📝 Notes

- seed ব্যবহার করলে output repeat হয়
- trig function radians-এ কাজ করে
- `*` আর `@` এক জিনিস না
- linear algebra ভবিষ্যৎ ML-এর জন্য খুব important

---

## 📌 Next Day Preview

- final iteration practice
- full workflow integration
- data science style mini pipeline
- NumPy complete revision

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- random data simulator বানানো যায়
- linear algebra practice notebook বানানো যায়

### 🧪 Practice Ideas

- নিজের seed set করে random output compare করো
- matrix multiplication manually verify করো
- log/exp/trig values experiment করো

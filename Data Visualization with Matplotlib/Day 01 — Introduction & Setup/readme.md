# 📅 Day 1 — Introduction & Setup

## 🎯 Objective

- আজকে Data Visualization কী সেটা বুঝবো।
- Matplotlib কেন ব্যবহার করা হয় সেটা শিখবো।
- প্রথম basic plot বানানো শিখবো।
- Figure, Axes, labels, title, এবং `plt.show()` কী কাজ করে সেটা বুঝবো।

## 📚 Topics Covered

- What is Data Visualization
- Why Matplotlib is important
- Installing Matplotlib
- Importing `pyplot`
- First plot
- Understanding Figure & Axes
- `plt.show()`
- Basic Line Plot
- `xlabel()`
- `ylabel()`
- `title()`

## 📁 Project Structure

```bash
day-1/
│── 01_intro.py
│── 02_install_note.py
│── 03_first_plot.py
│── 04_understanding_figure_axes.py
│── 05_basic_line_plot.py
│── 06_labels_and_title.py
│── README.md
```

## 📊 Dataset

- **File Name:** No dataset used
- **Description:** এই day-তে কোনো real dataset লাগেনি, কারণ focus ছিল Matplotlib basics শেখা
- **Columns:** Not applicable

## 💻 Code Breakdown (File by File)

### 📄 1. `01_intro.py`

#### 🔹 Purpose

- Data Visualization কী তা explain করে
- Visualization কেন দরকার সেটা বুঝায়

#### 🧾 Code

```python
"""
DAY 1 - Introduction to Data Visualization

What is Data Visualization?
---------------------------
Data Visualization means showing data in graphical form
like charts, graphs, and plots.

Why is it important?
---------------------
- Helps understand data easily
- Finds patterns quickly
- Used in AI, Data Science, Business analysis
"""

# No code here — just understanding concept
print("Data Visualization = Turning data into charts/graphs 📊")
```

#### 🧠 Explanation

- `""" ... """` দিয়ে বড় explanation লেখা হয়েছে
- এটা code নয়, বরং learning note
- `print()` line টা শুধু concept remember করার জন্য

---

### 📄 2. `02_install_note.py`

#### 🔹 Purpose

- Matplotlib install করার নিয়ম দেখায়

#### 🧾 Code

```python
"""
HOW TO INSTALL MATPLOTLIB

Matplotlib is a Python library used for data visualization.

Install command (run in terminal / cmd):
----------------------------------------
pip install matplotlib
"""

print("If not installed, run: pip install matplotlib")
```

#### 🧠 Explanation

- Matplotlib install করার command note করা হয়েছে
- `print()` দিয়ে reminder দেখানো হয়েছে
- এই file user-friendly setup guide হিসেবে কাজ করে

---

### 📄 3. `03_first_plot.py`

#### 🔹 Purpose

- প্রথম simple plot তৈরি করা

#### 🧾 Code

```python
# Import pyplot module from matplotlib
# pyplot is the most commonly used part of matplotlib
import matplotlib.pyplot as plt

"""
FIRST SIMPLE PLOT
------------------
We will plot a simple graph using some numbers
"""

# X-axis values
x = [1, 2, 3, 4, 5]

# Y-axis values
y = [2, 4, 6, 8, 10]

# Create the plot
plt.plot(x, y)

# Show the plot window
plt.show()
```

#### 🧠 Explanation

- `import matplotlib.pyplot as plt` → plotting করার জন্য module import করা হয়েছে
- `x` list এ input values আছে
- `y` list এ output values আছে
- `plt.plot(x, y)` → line graph তৈরি করে
- `plt.show()` → graph screen-এ দেখায়

---

### 📄 4. `04_understanding_figure_axes.py`

#### 🔹 Purpose

- Figure এবং Axes এর concept বুঝায়

#### 🧾 Code

```python
import matplotlib.pyplot as plt

"""
UNDERSTANDING FIGURE & AXES

Figure = Whole canvas (like a page)
Axes   = Actual graph area inside figure
"""

# Create figure and axes manually
fig, ax = plt.subplots()

# ax is where we draw the graph
ax.plot([1, 2, 3], [1, 4, 9])

# Show plot
plt.show()
```

#### 🧠 Explanation

- `plt.subplots()` দিয়ে figure এবং axes তৈরি করা হয়েছে
- `fig` = পুরো canvas
- `ax` = যেখানে actual plot draw হয়
- `ax.plot()` দিয়ে graph আঁকা হয়েছে

---

### 📄 5. `05_basic_line_plot.py`

#### 🔹 Purpose

- Basic line plot বানানো
- labels এবং title add করা

#### 🧾 Code

```python
import matplotlib.pyplot as plt

"""
BASIC LINE PLOT
---------------
Line plot connects points with a line
It is used to show trends over time
"""

x = [1, 2, 3, 4, 5]
y = [3, 5, 7, 9, 11]

plt.plot(x, y)

# Add labels and title (VERY IMPORTANT)
plt.xlabel("X Axis (Input Values)")
plt.ylabel("Y Axis (Output Values)")
plt.title("My First Line Plot")

plt.show()
```

#### 🧠 Explanation

- `plt.plot(x, y)` → line তৈরি করে
- `plt.xlabel()` → x-axis এর নাম দেয়
- `plt.ylabel()` → y-axis এর নাম দেয়
- `plt.title()` → chart title দেয়
- এগুলো graph-কে readable করে

---

### 📄 6. `06_labels_and_title.py`

#### 🔹 Purpose

- Labels এবং title আরও clearly practice করা

#### 🧾 Code

```python
import matplotlib.pyplot as plt

"""
LABELS & TITLE
--------------
These make graphs understandable
"""

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)

# X-axis label
plt.xlabel("Time")

# Y-axis label
plt.ylabel("Value")

# Graph title
plt.title("Simple Growth Chart")

plt.show()
```

#### 🧠 Explanation

- এখানে একই concept আবার practice করা হয়েছে
- `Time` x-axis এ রাখা হয়েছে
- `Value` y-axis এ রাখা হয়েছে
- `Simple Growth Chart` দিয়ে plot-এর meaning স্পষ্ট করা হয়েছে

## ⚙️ Implementation Flow

- Data visualization concept বোঝা হয়েছে
- Matplotlib install করার নিয়ম শেখা হয়েছে
- `pyplot` import করা হয়েছে
- প্রথম line plot বানানো হয়েছে
- Figure আর Axes এর difference শেখা হয়েছে
- Axis labels এবং title add করা হয়েছে
- Output graph screen-এ দেখানো হয়েছে

## 📈 Output / Result

### Key findings:

- Data কে chart আকারে দেখালে বুঝতে সহজ হয়
- Line plot দিয়ে trend বোঝা যায়
- Figure আর Axes concept future plotting এর base তৈরি করে
- Labels এবং title graph কে clear করে

## 🚀 What I Learned

- Data Visualization কী
- Matplotlib কেন important
- `plt.plot()` কীভাবে কাজ করে
- Figure আর Axes কী
- `xlabel()`, `ylabel()`, `title()` কী কাজ করে

## 🧠 Key Concepts (Quick Revision)

- Data Visualization = data কে graph/chart আকারে দেখানো
- Matplotlib = Python-এর most popular plotting library
- `plt.plot()` = line graph বানায়
- `plt.show()` = plot display করে
- `Figure` = whole canvas
- `Axes` = actual plotting area
- `xlabel()`, `ylabel()`, `title()` = chart readable করে

## 📝 Notes

- `plt.show()` না দিলে অনেক সময় plot দেখা যায় না
- `import matplotlib.pyplot as plt` ঠিকভাবে লিখতে হয়
- Empty plot না এলে data list length check করতে হয়
- Labels না দিলে graph বুঝতে কঠিন হয়

## 📌 Next Day Preview

- Multiple line plots
- `color`
- `linewidth`
- `linestyle`
- `marker`
- `legend()`
- `grid()`
- Custom ticks
- Real dataset line plotting

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- একই plot-এ আরও বেশি data add করা
- Different color ব্যবহার করা
- Real-world dataset দিয়ে line chart বানানো
- Save figure practice করা

### 🧪 Practice Ideas

- 1 থেকে 10 পর্যন্ত সংখ্যা দিয়ে plot বানাও
- temperature data নিয়ে simple line chart বানাও
- `xlabel`, `ylabel`, `title` change করে practice করো
- `plt.plot()` এর সাথে different value list try করো

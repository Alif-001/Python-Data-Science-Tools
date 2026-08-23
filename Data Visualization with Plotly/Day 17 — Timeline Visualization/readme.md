# 📅 Day 17 — Timeline Visualization (`px.timeline()`)

---

## 🎯 Objective

- আজকে আমরা শিখবো কীভাবে **time-based project workflow visualize করা যায়**
- বুঝবো কোন task কখন শুরু এবং শেষ হচ্ছে
- project scheduling এবং Gantt chart তৈরি করা
- real-world project management visualization করা

---

## 📚 Topics Covered

- `px.timeline()`
- Gantt chart basics
- Project tracking system
- Task scheduling visualization
- Duration analysis
- Overlapping tasks understanding
- Time-based data handling

---

## 📁 Project Structure

```text id="tl17p1"
Day 17 — Timeline Visualization/
│
├── 1_basic_timeline.py
├── 2_gantt_chart.py
├── 3_project_tracking.py
├── 4_task_scheduling.py
└── project_tasks.csv
```

---

## 📊 Dataset

**File Name:** `project_tasks.csv`

**Description:**
Software project planning dataset showing tasks with start and end dates for timeline visualization.

**Columns:**

- task → কাজের নাম (Requirement, Design, Development etc.)
- start → কাজ শুরু হওয়ার তারিখ
- end → কাজ শেষ হওয়ার তারিখ
- team → কোন team কাজটি করছে

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `1_basic_timeline.py`

### 🔹 Purpose

- basic timeline chart তৈরি করা
- project tasks schedule visualize করা

### 🧾 Code

```python id="tl17c1"
import pandas as pd
import plotly.express as px

df = pd.read_csv("project_tasks.csv")

df["start"] = pd.to_datetime(df["start"])
df["end"] = pd.to_datetime(df["end"])

fig = px.timeline(
    df,
    x_start="start",
    x_end="end",
    y="task",
    title="Project Timeline Overview"
)

fig.show()
```

---

### 🧠 Explanation

- `pd.to_datetime()` → date format convert করে
- `px.timeline()` → time-based visualization তৈরি করে
- `x_start`, `x_end` → task duration define করে

👉 Logic:

- প্রতিটি task কতদিন চলেছে তা visualize করা হয়
- overlapping tasks easily দেখা যায়

---

## 📄 2. `2_gantt_chart.py`

### 🔹 Purpose

- Gantt chart তৈরি করা
- team-wise project breakdown দেখা

### 🧾 Code

```python id="tl17c2"
import pandas as pd
import plotly.express as px

df = pd.read_csv("project_tasks.csv")

df["start"] = pd.to_datetime(df["start"])
df["end"] = pd.to_datetime(df["end"])

fig = px.timeline(
    df,
    x_start="start",
    x_end="end",
    y="task",
    color="team",
    title="Gantt Chart - Project Breakdown"
)

fig.show()
```

---

### 🧠 Explanation

- `color="team"` → team অনুযায়ী tasks আলাদা হয়
- Gantt chart project planning visualize করে

👉 Logic:

- কে কোন কাজ করছে clear বোঝা যায়
- team workload distribution দেখা যায়

---

## 📄 3. `3_project_tracking.py`

### 🔹 Purpose

- task duration calculate করা
- project bottleneck analysis করা

### 🧾 Code

```python id="tl17c3"
import pandas as pd
import plotly.express as px

df = pd.read_csv("project_tasks.csv")

df["start"] = pd.to_datetime(df["start"])
df["end"] = pd.to_datetime(df["end"])

df["duration_days"] = (df["end"] - df["start"]).dt.days

print(df)

fig = px.timeline(
    df,
    x_start="start",
    x_end="end",
    y="task",
    color="duration_days",
    title="Project Tracking (Duration View)"
)

fig.show()
```

---

### 🧠 Explanation

- duration calculate করা হয়: `end - start`
- `color="duration_days"` → দীর্ঘ task highlight হয়

👉 Logic:

- কোন task বেশি সময় নিচ্ছে তা identify করা যায়
- project delay analysis করা যায়

---

## 📄 4. `4_task_scheduling.py`

### 🔹 Purpose

- optimized task scheduling visualize করা
- workflow clean করা

### 🧾 Code

```python id="tl17c4"
import pandas as pd
import plotly.express as px

df = pd.read_csv("project_tasks.csv")

df["start"] = pd.to_datetime(df["start"])
df["end"] = pd.to_datetime(df["end"])

df = df.sort_values("start")

fig = px.timeline(
    df,
    x_start="start",
    x_end="end",
    y="task",
    color="team",
    title="Task Scheduling Overview"
)

fig.update_yaxes(autorange="reversed")

fig.show()
```

---

### 🧠 Explanation

- `sort_values("start")` → proper schedule order তৈরি করে
- `autorange="reversed"` → classic Gantt look দেয়

👉 Logic:

- workflow structured হয়
- scheduling conflicts reduce হয়

---

## ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- date columns convert করা হয়েছে
- task duration calculate করা হয়েছে
- timeline chart তৈরি করা হয়েছে
- Gantt-style visualization তৈরি করা হয়েছে
- scheduling optimized করা হয়েছে

---

## 📈 Output / Result

### Key Findings:

- Backend Development সবচেয়ে long task
- Design এবং Development overlap করে
- QA phase late stage এ শুরু হয়
- overall project timeline clearly visible

---

## 🚀 What I Learned

- Timeline chart time-based visualization বোঝায়
- Gantt chart project management এর core tool
- duration analysis bottleneck identify করে
- scheduling workflow optimize করতে সাহায্য করে

---

## 🧠 Key Concepts (Quick Revision)

- Timeline → time-based visualization
- Gantt chart → project planning tool
- Start/End → task duration define করে
- Duration → task length measure করে
- Scheduling → workflow arrangement

---

## 📝 Notes

- date format ভুল হলে chart কাজ করবে না
- overlapping tasks proper planning দরকার
- small dataset এ timeline less meaningful হতে পারে

---

## 📌 Next Day Preview

আগামী দিনে আমরা শিখবো:

- 🗺️ Choropleth Map (`px.choropleth`)
- geographic data visualization
- country/state-based analysis
- spatial data understanding

---

## ⭐ Bonus

### 🔥 Improvements Ideas

- real Jira project dataset ব্যবহার করো
- milestone tracking add করো
- dependency graph তৈরি করো

---

### 🧪 Practice Ideas

- নতুন task add করো (Code Review)
- team-wise workload compare করো
- longest task identify করো
- project delay risk analysis করো

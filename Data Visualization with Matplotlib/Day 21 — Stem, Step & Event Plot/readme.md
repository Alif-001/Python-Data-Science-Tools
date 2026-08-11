# 📅 Day 21 — Stem, Step & Event Plot

## 🎯 Objective

- আজকে discrete data visualization শিখবো
- Signal, state change, এবং event-based data plot করা শিখবো
- Stem plot, step plot, এবং event plot-এর use case বুঝবো
- Real dataset দিয়ে discrete pattern analysis করা শিখবো

---

## 📚 Topics Covered

- Stem plot
- Step plot
- Event plot
- Discrete signal visualization

---

## 📁 Project Structure

```bash
day-21/
│── 01_stem_plot_basics.py
│── 02_stem_signal_analysis.py
│── 03_step_plot_basics.py
│── 04_step_signal_changes.py
│── 05_event_plot_basics.py
│── 06_event_signal_firing.py
│── 07_csv_stem_step_event.py
│── signal_data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** `signal_data.csv`
- **Description:** Simple discrete signal data used for stem plot and step plot visualization

### Columns:

- `time` → Time index or sequence position
- `value` → Signal value at each time point

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. `01_stem_plot_basics.py`

### 🔹 Purpose

- Basic stem plot বুঝতে সাহায্য করে
- Discrete data point clearly show করে

### 🧠 Explanation

- `x` values দিয়ে index তৈরি করা হয়েছে
- `y` values দিয়ে signal/data points রাখা হয়েছে
- `plt.stem(x, y)` ব্যবহার করে stem plot আঁকা হয়েছে
- এটি discrete measurements দেখানোর জন্য useful

---

## 📄 2. `02_stem_signal_analysis.py`

### 🔹 Purpose

- Signal analysis-এর জন্য stem plot ব্যবহার শেখা

### 🧠 Explanation

- `t` variable দিয়ে time sequence তৈরি করা হয়েছে
- `signal` variable-এ sine wave + noise ব্যবহার করা হয়েছে
- Stem plot দিয়ে discrete signal representation দেখানো হয়েছে
- DSP (Digital Signal Processing)-এ এই concept খুব useful

---

## 📄 3. `03_step_plot_basics.py`

### 🔹 Purpose

- Step plot-এর basic usage শেখা

### 🧠 Explanation

- `x` এবং `y` values দিয়ে changing values show করা হয়েছে
- `plt.step(x, y, where="mid")` ব্যবহার করা হয়েছে
- Step plot sudden change বোঝাতে useful
- Stock price, system state, threshold-based data-তে কাজে লাগে

---

## 📄 4. `04_step_signal_changes.py`

### 🔹 Purpose

- State change visualization করা

### 🧠 Explanation

- `time` array দিয়ে sequence তৈরি করা হয়েছে
- `state` list-এ ON/OFF pattern রাখা হয়েছে
- `plt.step(..., where="post")` ব্যবহার করে state transition দেখানো হয়েছে
- Sudden change visualize করতে step plot perfect

---

## 📄 5. `05_event_plot_basics.py`

### 🔹 Purpose

- Event-based data visualize করা

### 🧠 Explanation

- `events` list-এর প্রতিটি inner list আলাদা category represent করে
- `plt.eventplot(events)` ব্যবহার করা হয়েছে
- Specific time-এ ঘটছে এমন ঘটনা দেখাতে event plot useful
- Spike, log, event timing display করার জন্য ব্যবহার হয়

---

## 📄 6. `06_event_signal_firing.py`

### 🔹 Purpose

- Spike / firing event visualization শেখা

### 🧠 Explanation

- তিনটি neuron firing time generate করা হয়েছে
- `np.random.randint()` দিয়ে random event times তৈরি করা হয়েছে
- `plt.eventplot([neuron1, neuron2, neuron3])` ব্যবহার করা হয়েছে
- Neuroscience বা spike detection style data-তে কাজে লাগে

---

## 📄 7. `signal_data.csv`

### 🔹 Purpose

- Real discrete dataset হিসেবে ব্যবহার করা হয়েছে

### 🧠 Explanation

- CSV file থেকে time এবং value read করা হয়েছে
- Stem plot এবং step plot দুইভাবেই একই data visualized হয়েছে
- Real data-এর উপর discrete plotting practice করা হয়েছে

---

## 📄 8. `07_csv_stem_step_event.py`

### 🔹 Purpose

- CSV data ব্যবহার করে multiple plot তৈরি করা

### 🧠 Explanation

- `csv.DictReader()` দিয়ে CSV read করা হয়েছে
- `time` এবং `value` list-এ data store করা হয়েছে
- `plt.subplot()` দিয়ে side-by-side plots বানানো হয়েছে
- এক dataset থেকে stem plot এবং step plot compare করা হয়েছে

---

## ⚙️ Implementation Flow

- CSV dataset তৈরি করা হয়েছে
- Data read করা হয়েছে
- Stem plot দিয়ে discrete values দেখানো হয়েছে
- Step plot দিয়ে sudden change visualized করা হয়েছে
- Event plot দিয়ে event timing দেখানো হয়েছে
- Multiple plot compare করে pattern analysis করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- Stem plot discrete values clearly show করে
- Step plot sudden state change বোঝাতে সাহায্য করে
- Event plot time-based events represent করে
- Signal data analysis-এর জন্য এই plots খুব useful
- One dataset থেকে multiple chart compare করা যায়

---

## 🚀 What I Learned

- Stem plot কীভাবে কাজ করে
- Step plot কেন discrete change বোঝাতে useful
- Event plot কীভাবে event timing represent করে
- Signal-like data visualization concept
- Same dataset multiple way-এ present করা যায়

---

## 🧠 Key Concepts (Quick Revision)

- `plt.stem()` → discrete points show করে
- `plt.step()` → sudden change show করে
- `plt.eventplot()` → event timing visualize করে
- `where="mid"` → মাঝখানে step change দেখায়
- `where="post"` → change পরে show করে
- CSV data → real dataset analysis-এর জন্য useful

---

## 📝 Notes

- Stem plot বেশি useful discrete numerical data-র জন্য
- Step plot state-based data-তে ভালো কাজ করে
- Event plot category-wise events show করতে পারে
- Overlapping points avoid করতে data carefully choose করা উচিত

---

## 📌 Next Day Preview

- Time Series Visualization
- Date handling
- Time axis formatting
- Financial-style plotting
- Datetime-based charts

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Multi-category event comparison add করা
- Real sensor data ব্যবহার করা
- Stem + step + event dashboard বানানো
- Noise filtering logic add করা

### 🧪 Practice Ideas

- Sensor reading-এর stem plot বানাও
- Machine ON/OFF state-এর step plot বানাও
- Exam timing event plot বানাও
- CSV data দিয়ে multiple plots compare করো

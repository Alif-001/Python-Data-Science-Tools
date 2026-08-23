# 📅 Day 25 — Advanced Color Palettes

---

# 🎯 Objective

- Seaborn color palettes বোঝা
- Different palette types শেখা (sequential, diverging, qualitative)
- Custom color palette তৈরি করা
- Visualization কে more meaningful এবং professional করা
- Color-based data storytelling শেখা

---

# 📚 Topics Covered

- `sns.color_palette()`
- Sequential palette
- Diverging palette
- Qualitative palette
- Custom palette creation
- Palette in real plots
- Color-based storytelling

---

# 📁 Project Structure

```bash id="day25-structure"
day-25/
│── 01_color_palette_basics.py
│── 02_sequential_palette.py
│── 03_diverging_palette.py
│── 04_qualitative_palette.py
│── 05_custom_palette.py
│── 06_palette_in_plot.py
│── 07_real_world_palette_usage.py
│── 08_advanced_palette_story.py
│── product_sales.csv
│── README.md
```

---

# 📊 Dataset

## 📌 File Name: `product_sales.csv`

## 📌 Description

এই dataset এ বিভিন্ন product এর sales data দেওয়া আছে different regions অনুযায়ী, যা color-based analysis শেখার জন্য ব্যবহার করা হয়েছে।

---

## 📌 Columns

- `product` → product name (A, B, C)
- `region` → sales region (North, South, East)
- `sales` → total sales value

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_color_palette_basics.py

## 🔹 Purpose

- Default Seaborn color palette বোঝা
- Basic palette structure দেখা

## 🧾 Code

```python id="day25-1"
palette = sns.color_palette()
sns.palplot(palette)
```

## 🧠 Explanation

- Default color cycle show করে
- Visualization styling এর base idea দেয়

---

# 📄 2. 02_sequential_palette.py

## 🔹 Purpose

- Sequential color scale বোঝা
- Low → High intensity representation

## 🧾 Code

```python id="day25-2"
palette = sns.color_palette("Blues", 10)
sns.palplot(palette)
```

## 🧠 Explanation

- Light color = low value
- Dark color = high value
- Ordered data represent করে

---

# 📄 3. 03_diverging_palette.py

## 🔹 Purpose

- Diverging color scale বোঝা
- Positive vs negative contrast বোঝা

## 🧾 Code

```python id="day25-3"
palette = sns.color_palette("coolwarm", 10)
sns.palplot(palette)
```

## 🧠 Explanation

- Blue = low value
- Red = high value
- Middle = neutral point

---

# 📄 4. 04_qualitative_palette.py

## 🔹 Purpose

- Categorical data coloring শেখা

## 🧾 Code

```python id="day25-4"
palette = sns.color_palette("Set2", 8)
sns.palplot(palette)
```

## 🧠 Explanation

- No order relation
- Each category = separate color
- Used for grouping

---

# 📄 5. 05_custom_palette.py

## 🔹 Purpose

- Custom colors তৈরি করা
- Branding control শেখা

## 🧾 Code

```python id="day25-5"
custom_colors = ["#ff9999", "#66b3ff", "#99ff99"]
palette = sns.color_palette(custom_colors)
sns.palplot(palette)
```

## 🧠 Explanation

- User-defined colors ব্যবহার করা হয়েছে
- Dashboard / UI design এর জন্য useful

---

# 📄 6. 06_palette_in_plot.py

## 🔹 Purpose

- Real plot এ palette apply করা

## 🧾 Code

```python id="day25-6"
sns.barplot(data=tips, x="day", y="total_bill", palette="Blues")
```

## 🧠 Explanation

- Color = value intensity represent করে
- Visual understanding improve করে

---

# 📄 7. 07_real_world_palette_usage.py

## 🔹 Purpose

- Business-level visualization তৈরি করা

## 🧾 Code

```python id="day25-7"
sns.barplot(data=df, x="product", y="sales", hue="region", palette="Set2")
```

## 🧠 Explanation

- Region-based color grouping
- Easy comparison between categories

---

# 📄 8. 08_advanced_palette_story.py

## 🔹 Purpose

- Statistical storytelling with color

## 🧾 Code

```python id="day25-8"
sns.boxplot(data=tips, x="day", y="total_bill", palette="coolwarm")
```

## 🧠 Explanation

- Color adds emotional + analytical meaning
- Distribution differences highlight করে

---

# ⚙️ Implementation Flow

- Default palette visualize করা হয়েছে
- Sequential, diverging, qualitative palettes শেখা হয়েছে
- Custom colors তৈরি করা হয়েছে
- Real plots এ palettes apply করা হয়েছে
- Business dataset visualize করা হয়েছে
- Statistical storytelling তৈরি করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Sequential palette = ordered data
- Diverging palette = comparison (high vs low)
- Qualitative palette = categories
- Custom palette = branding control

---

# 🚀 What I Learned

- Color psychology in data visualization
- Different palette types usage
- Professional plotting techniques
- Business-level visualization design
- Storytelling with colors

---

# 🧠 Key Concepts (Quick Revision)

- Color = data encoding
- Sequential → ordered values
- Diverging → deviation from center
- Qualitative → categories
- Custom → user-defined design

---

# 📝 Notes

## 📌 Mistakes

- Wrong palette type ব্যবহার করলে misleading visualization হতে পারে
- Too many colors = confusion

## 📌 Optimization Tips

- Always choose palette based on data type
- Keep color consistency in dashboards

---

# 📌 Next Day Preview

## 📅 Day 26 — Figure-Level vs Axes-Level Deep Dive

- `relplot`, `catplot`, `displot`
- Axes vs figure concept deep understanding
- Multi-plot layouts
- When to use what

---

# ⭐ Bonus

## 🔥 Improvements Ideas

- Dashboard color theme design করা
- Brand-based visualization style তৈরি করা
- Heatmap + palette experiment করা

---

## 🧪 Practice Ideas

- Same plot different palettes compare করো
- Custom palette দিয়ে dashboard design করো
- Diverging palette vs sequential palette compare করো

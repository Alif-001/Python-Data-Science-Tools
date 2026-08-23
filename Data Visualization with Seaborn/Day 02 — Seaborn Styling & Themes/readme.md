# 📅 Day 2 — Seaborn Styling & Themes

---

# 🎯 Objective

- Seaborn এর styling system বোঝা
- Professional-looking visualization তৈরি করা
- Different themes ও styles compare করা
- Context scaling ব্যবহার শেখা
- Color palettes ব্যবহার করা
- Figure customization শেখা
- Matplotlib + Seaborn integration বোঝা

---

# 📚 Topics Covered

- `sns.set_theme()`
- `sns.set_style()`
- `darkgrid`
- `whitegrid`
- `dark`
- `white`
- `ticks`
- Context scaling
- Color palettes
- Figure styling

---

# 📁 Project Structure

```bash id="7w2ms1"
day-2/
│── 01_theme_basics.py
│── 02_set_style_comparison.py
│── 03_context_scaling.py
│── 04_color_palettes.py
│── 05_figure_style_customization.py
│── README.md
```

---

# 📊 Dataset

- **Dataset Name:** `tips`
- **Source:** Built-in Seaborn Dataset
- **Loaded Using:** `sns.load_dataset("tips")`

## 📌 Description

Restaurant tipping dataset যেখানে customer bill, tip, gender, smoking status ইত্যাদি তথ্য রয়েছে।

## 📌 Columns

- `total_bill` → মোট বিল
- `tip` → tip amount
- `sex` → customer gender
- `smoker` → smoker কি না
- `day` → সপ্তাহের দিন
- `time` → lunch/dinner
- `size` → মোট মানুষ সংখ্যা

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_theme_basics.py

## 🔹 Purpose

- `sns.set_theme()` শেখা
- Theme apply করা
- Plot appearance control করা

---

## 🧾 Code

```python id="dd3h2m"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.set_theme(
    style="darkgrid",
    palette="deep",
    font_scale=1.2
)

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip"
)

plt.title("Theme Demo - darkgrid")
plt.show()
```

---

## 🧠 Explanation

- `sns.set_theme()`
  - পুরো visualization এর appearance control করে

- `style="darkgrid"`
  - Background grid apply করে

- `palette="deep"`
  - Default color palette সেট করে

- `font_scale=1.2`
  - Text size increase করে

- `sns.scatterplot()`
  - Scatter plot তৈরি করে

---

# 📄 2. 02_set_style_comparison.py

## 🔹 Purpose

- Different Seaborn styles compare করা

---

## 🧾 Code

```python id="w0ng0x"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

styles = ["darkgrid", "whitegrid", "dark", "white", "ticks"]

for style in styles:

    sns.set_style(style)

    sns.scatterplot(
        data=tips,
        x="total_bill",
        y="tip"
    )

    plt.title(f"Style: {style}")
    plt.show()
```

---

## 🧠 Explanation

- `sns.set_style()`
  - Plot background style পরিবর্তন করে

- `for style in styles`
  - সব styles loop করে দেখানো হয়েছে

- Different styles:
  - `darkgrid`
  - `whitegrid`
  - `dark`
  - `white`
  - `ticks`

---

## 📌 Style Usage

- `darkgrid` → analysis এর জন্য ভালো
- `whitegrid` → reports এর জন্য clean look
- `dark` → presentation style
- `white` → minimal design
- `ticks` → publication style

---

# 📄 3. 03_context_scaling.py

## 🔹 Purpose

- Context scaling শেখা
- Plot readability control করা

---

## 🧾 Code

```python id="1r1d8m"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

contexts = ["paper", "notebook", "talk", "poster"]

for context in contexts:

    sns.set_theme(context=context)

    sns.scatterplot(
        data=tips,
        x="total_bill",
        y="tip"
    )

    plt.title(f"Context: {context}")
    plt.show()
```

---

## 🧠 Explanation

- Context scaling controls:
  - Font size
  - Label size
  - Line thickness
  - Overall readability

- `paper`
  - Small plots for research papers

- `notebook`
  - Default notebook size

- `talk`
  - Presentation slides

- `poster`
  - Large poster-style plots

---

# 📄 4. 04_color_palettes.py

## 🔹 Purpose

- Color palettes শেখা
- Category-based coloring করা

---

## 🧾 Code

```python id="3r31w9"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

palettes = [
    "deep",
    "muted",
    "bright",
    "pastel",
    "dark",
    "colorblind"
]

for palette in palettes:

    sns.set_theme(palette=palette)

    sns.scatterplot(
        data=tips,
        x="total_bill",
        y="tip",
        hue="sex"
    )

    plt.title(f"Palette: {palette}")
    plt.show()
```

---

## 🧠 Explanation

- `palette`
  - Plot color system control করে

- `hue="sex"`
  - Male/Female অনুযায়ী different colors দেয়

- `colorblind`
  - Accessibility-friendly palette

---

## 📌 Popular Palettes

- `deep`
- `muted`
- `bright`
- `pastel`
- `dark`
- `colorblind`

---

# 📄 5. 05_figure_style_customization.py

## 🔹 Purpose

- Figure customization শেখা
- Plot size, labels, legends customize করা

---

## 🧾 Code

```python id="5kv2cw"
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.set_theme(
    style="whitegrid",
    palette="pastel",
    font_scale=1.3
)

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=tips,
    x="total_bill",
    y="tip",
    hue="time"
)

plt.title("Customized Figure Styling", fontsize=16)
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")

plt.legend(title="Time of Day")

plt.tight_layout()

plt.show()
```

---

## 🧠 Explanation

- `plt.figure(figsize=(10, 6))`
  - Figure size control করে

- `plt.title()`
  - Plot title set করে

- `plt.xlabel()`
  - X-axis label সেট করে

- `plt.ylabel()`
  - Y-axis label সেট করে

- `plt.legend()`
  - Legend customize করে

- `plt.tight_layout()`
  - Overlapping fix করে

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Theme apply করা হয়েছে
- Different styles compare করা হয়েছে
- Context scaling apply করা হয়েছে
- Color palettes visualize করা হয়েছে
- Figure customization করা হয়েছে
- Matplotlib integration ব্যবহার করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Seaborn themes visualization কে professional look দেয়
- Different styles different use-case এর জন্য useful
- Context scaling readability improve করে
- Color palettes data interpretation সহজ করে
- Matplotlib integration advanced customization সম্ভব করে

---

# 🚀 What I Learned

- `sns.set_theme()`
- `sns.set_style()`
- Styling system
- Context scaling
- Color palette usage
- Figure customization
- Matplotlib integration
- Professional visualization design

---

# 🧠 Key Concepts (Quick Revision)

- `sns.set_theme()` → full theme control
- `sns.set_style()` → background style control
- `palette` → color system control
- `context` → scaling control
- `hue` → category coloring
- `tight_layout()` → overlap fix

---

# 📝 Notes

## 📌 Common Mistakes

- Theme apply না করা
- Wrong palette selection
- Overcrowded visualization তৈরি করা
- Figure size ছোট রাখা

---

## 📌 Optimization Tips

- `whitegrid` reports এর জন্য best
- `darkgrid` EDA এর জন্য useful
- `colorblind` palette accessibility improve করে
- `talk` context presentations এর জন্য ideal

---

# 📌 Next Day Preview

## 📅 Day 3 — Line Plot

আগামী দিনে শিখবো:

- `sns.lineplot()`
- Trend visualization
- Multiple line plots
- `hue`
- `style`
- `size`
- Confidence interval
- Error bars
- Time-series plotting

---

# ⭐ Bonus (Optional)

## 🔥 Improvement Ideas

- Custom palette তৈরি করা
- Multiple themes compare করা
- Presentation-ready charts তৈরি করা
- Publication-style visualization তৈরি করা

---

## 🧪 Practice Ideas

- Different themes apply করে একই plot compare করো
- `iris` dataset এ palettes test করো
- Figure size পরিবর্তন করে visualization compare করো
- `hue` ব্যবহার করে multiple category visualization তৈরি করো

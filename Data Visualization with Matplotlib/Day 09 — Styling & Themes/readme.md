# 📅 Day 9 — Styling & Themes

## 🎯 Objective

- আজকে Matplotlib এর styling system শিখবো
- Built-in themes ব্যবহার করা শিখবো
- Dark mode visualization বানানো শিখবো
- Custom professional charts design করা শিখবো
- Real-world dashboard style plotting শিখবো

---

## 📚 Topics Covered

- Built-in styles
- Dark background
- Custom themes
- Font size
- Font family
- Background color
- Axis styling
- Spine customization
- Professional visualization styling

---

## 📁 Project Structure

```bash
day-9/
│── 01_builtin_styles.py
│── 02_dark_theme.py
│── 03_custom_theme.py
│── 04_font_customization.py
│── 05_axis_styling.py
│── 06_spine_customization.py
│── 07_background_color.py
│── 08_professional_style.py
│── 09_real_professional_chart.py
│── company_growth.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** company_growth.csv
- **Description:** Company revenue and profit growth data used for professional visualization

### Columns:

- year → Business year
- revenue → Total revenue
- profit → Net profit

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. main.py (Concept Entry)

### 🔹 Purpose

- Styling system overview
- Visualization aesthetics concept বোঝা

### 🧾 Code

```python id="sty_main9"
print("Styling & Themes Day 9 🎨")
```

### 🧠 Explanation

- Visualization শুধু data না, designও গুরুত্বপূর্ণ
- Good styling = better understanding

---

## 📄 2. analysis.py

### 🔹 Purpose

- Data appearance analysis

### 🧾 Code

```python id="sty_analysis9"
def style_analysis():
    return "Improving visual readability and aesthetics"
```

### 🧠 Explanation

- Styling improves insight readability
- Business charts need clean visuals

---

## 📄 3. utils.py

### 🔹 Purpose

- Helper styling functions

### 🧾 Code

```python id="sty_utils9"
def format_color(color):
    return color.lower()
```

### 🧠 Explanation

- Color formatting standardize করে
- Reusable styling helper

---

## 📄 4. 01_builtin_styles.py

### 🔹 Purpose

- Built-in theme ব্যবহার শেখা

### 🧾 Code

```python id="sty1"
plt.style.use("ggplot")
```

### 🧠 Explanation

- Predefined themes দ্রুত styling দেয়
- ggplot, seaborn, classic available

---

## 📄 5. 02_dark_theme.py

### 🔹 Purpose

- Dark mode visualization

### 🧾 Code

```python id="sty2"
plt.style.use("dark_background")
```

### 🧠 Explanation

- Modern dashboard look
- Eye-friendly dark UI style

---

## 📄 6. 03_custom_theme.py

### 🔹 Purpose

- Manual customization

### 🧾 Code

```python id="sty3"
plt.figure(facecolor="lightgray")
plt.plot(x, y, color="blue")
```

### 🧠 Explanation

- Background + line color manually control
- Full customization possible

---

## 📄 7. 04_font_customization.py

### 🔹 Purpose

- Font styling

### 🧾 Code

```python id="sty4"
plt.title("Font Example", fontsize=18, fontweight="bold")
```

### 🧠 Explanation

- Font size readability improve করে
- Bold text = highlight important info

---

## 📄 8. 05_axis_styling.py

### 🔹 Purpose

- Axis styling control

### 🧾 Code

```python id="sty5"
plt.tick_params(axis="x", colors="red")
```

### 🧠 Explanation

- Axis labels customize করা যায়
- Better UI/UX in plots

---

## 📄 9. 06_spine_customization.py

### 🔹 Purpose

- Chart border control

### 🧾 Code

```python id="sty6"
ax.spines["top"].set_visible(False)
```

### 🧠 Explanation

- Spines = border lines
- Clean professional look তৈরি হয়

---

## 📄 10. 07_background_color.py

### 🔹 Purpose

- Background styling

### 🧾 Code

```python id="sty7"
plt.figure(facecolor="#f0f0f0")
```

### 🧠 Explanation

- Light background = clean visualization
- Theme consistency important

---

## 📄 11. 08_professional_style.py

### 🔹 Purpose

- Professional dashboard chart

### 🧾 Code

```python id="sty8"
plt.style.use("seaborn-v0_8")
plt.plot(x, y, marker="o")
```

### 🧠 Explanation

- Real-world analytics style
- Clean and modern visualization

---

## 📄 12. 09_real_professional_chart.py

### 🔹 Purpose

- Real business chart styling

### 🧾 Code

```python id="sty9"
plt.plot(years, revenue)
plt.plot(years, profit)
```

### 🧠 Explanation

- Company growth analysis
- Revenue vs profit comparison
- Business insight visualization

---

## ⚙️ Implementation Flow

- Built-in themes ব্যবহার করা হয়েছে
- Dark mode visualization তৈরি করা হয়েছে
- Fonts এবং axis styling শেখা হয়েছে
- Spines customization করা হয়েছে
- Background design control করা হয়েছে
- Professional dashboard chart বানানো হয়েছে

---

## 📈 Output / Result

### Key findings:

- Styling improves readability significantly
- Dark mode modern UI experience দেয়
- Spines remove করলে chart clean হয়
- Fonts highlight important data
- Professional charts business-ready হয়

---

## 🚀 What I Learned

- Built-in vs custom styling
- Dark theme usage
- Font & axis customization
- Spine manipulation
- Professional chart design principles

---

## 🧠 Key Concepts (Quick Revision)

- `plt.style.use()` → theme apply
- `dark_background` → dark mode
- `fontsize` → text size control
- `spines` → border control
- `tick_params()` → axis styling
- `facecolor` → background color

---

## 📝 Notes

- Styling = readability + aesthetics
- Too many colors avoid করা উচিত
- Professional charts clean এবং minimal হয়
- Consistency in design is important

---

## 📌 Next Day Preview

- Text & Annotation system
- Advanced labeling techniques
- Arrow annotation
- Data highlighting
- Storytelling with graphs

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Interactive styled dashboard
- Theme switching system
- Auto professional report generator
- Branding-based visualization system

### 🧪 Practice Ideas

- Company annual report design করো
- Stock market styled chart বানাও
- Dark/light mode toggle dashboard তৈরি করো
- Sales performance report design করো

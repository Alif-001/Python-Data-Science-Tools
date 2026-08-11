# 📅 Day 30 — Exporting & Publishing

🎯 Objective

- আজকে আমরা শিখবো কিভাবে Matplotlib plots save এবং export করতে হয়
- High-quality image, PDF report এবং transparent background তৈরি করা শিখবো
- Professional publication-ready visualization তৈরি করার workflow বুঝবো
- Real-world reporting system (business / research) এ chart export ব্যবহার করা শিখবো

---

📚 Topics Covered

- Save plot as PNG image
- Save plot as PDF (vector format)
- High-resolution export (DPI control)
- Transparent background export
- Publication-quality figure design
- Multi-format exporting workflow

---

📁 Project Structure

```
day-30/
│── 01_save_as_png.py
│── 02_save_as_pdf.py
│── 03_high_resolution_export.py
│── 04_transparent_background.py
│── 05_publication_quality.py
│── 06_multiple_formats_export.py
│── 07_csv_export_report.py
│── report_data.csv
│── README.md
```

---

📊 Dataset

**File Name:** report_data.csv

**Description:**
Business report dataset containing daily sales and profit values used for visualization and exporting.

**Columns:**

- column1 → day (time index)
- column2 → sales (daily sales value)
- column3 → profit (daily profit value)

---

💻 Code Breakdown (File by File)

---

📄 1. main.py (Save as PNG Example)

🔹 Purpose

- Plot তৈরি করে PNG image হিসেবে save করা

🧾 Code

```python id="png1"
plt.savefig("plot_basic.png")
```

🧠 Explanation

- plot তৈরি হওয়ার পরে image হিসেবে save করা হয়েছে
- PNG format = most common image format
- report / presentation এ ব্যবহার করা যায়

---

📄 2. analysis.py (Save as PDF Example)

🔹 Purpose

- vector quality report তৈরি করা

🧾 Code

```python id="pdf1"
plt.savefig("plot_graph.pdf")
```

🧠 Explanation

- PDF = high-quality scalable format
- print বা research paper এর জন্য best
- zoom করলেও quality নষ্ট হয় না

---

📄 3. utils.py (High Resolution Export)

🔹 Purpose

- high quality image তৈরি করা (DPI control)

🧾 Code

```python id="dpi1"
plt.savefig("high_res_plot.png", dpi=300)
```

🧠 Explanation

- DPI = image clarity measure
- 300 DPI = publication standard
- বেশি DPI = sharper image

---

⚙️ Implementation Flow

- Data load করা হয়েছে (CSV বা NumPy)
- Plot তৈরি করা হয়েছে (line graph)
- Style + labels set করা হয়েছে
- Savefig ব্যবহার করে export করা হয়েছে
- PNG / PDF / JPG format generate করা হয়েছে

---

📈 Output / Result

Key findings:

- High-quality charts generate করা যায়
- Report-ready visualization তৈরি সম্ভব
- Multiple format export support পাওয়া যায়
- Professional data presentation workflow তৈরি হয়

---

🚀 What I Learned

- Matplotlib figure export system
- DPI vs image quality relationship
- PDF vs PNG format difference
- Publication-ready visualization design

---

🧠 Key Concepts (Quick Revision)

- `savefig()` → plot save করার function
- `dpi` → image quality control
- `bbox_inches="tight"` → extra white space remove
- `transparent=True` → background remove
- PDF → vector format (best for research)

---

📝 Notes

- `plt.savefig()` অবশ্যই `plt.show()` এর আগে ব্যবহার করা ভালো
- High DPI file size বড় হয়
- Transparent background presentation slide এ useful
- PDF format scientific publishing এ widely used

---

📌 Next Day Preview

- Final project integration
- Complete data visualization pipeline
- Dashboard-style project build
- Portfolio-ready visualization system

---

⭐ Bonus (Optional)

🔥 Improvements Ideas

- automatic report generator বানানো
- dashboard export system তৈরি করা
- real-time data auto-save system

🧪 Practice Ideas

- sales report generator বানাও
- student result report PDF বানাও
- stock market chart exporter বানাও

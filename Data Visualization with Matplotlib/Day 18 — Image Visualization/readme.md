# 📅 Day 18 — Image Visualization

---

## 🎯 Objective

- আজকে Matplotlib দিয়ে image visualization শিখবো
- `imshow()` ব্যবহার করে image display করা শিখবো
- Grayscale ও RGB image বুঝবো
- Interpolation concept শিখবো
- CSV data কে image হিসেবে visualize করা শিখবো

---

## 📚 Topics Covered

- `imshow()`
- Displaying images
- Grayscale image
- RGB image
- Interpolation
- Colorbar

---

## 📁 Project Structure

```bash
day-18/
│── 01_imshow_basics.py
│── 02_grayscale_image.py
│── 03_rgb_image.py
│── 04_interpolation.py
│── 05_colorbar_explained.py
│── 06_zoom_and_crop_image.py
│── 07_csv_image_visualization.py
│── pixel_data.csv
│── README.md
```

---

## 📊 Dataset

- **File Name:** pixel_data.csv
- **Description:** Pixel intensity values যেগুলোকে image হিসেবে visualize করা হয়

### Columns:

- row0 → প্রথম row pixel values
- row1 → second row pixel values
- row2 → third row pixel values
- row3 → fourth row pixel values
- row4 → fifth row pixel values

---

## 💻 Code Breakdown (File by File)

---

## 📄 1. 01_imshow_basics.py

### 🔹 Purpose

- Basic image display using matrix

### 🧾 Code

```python
plt.imshow(image)
plt.colorbar()
```

### 🧠 Explanation

- Matrix values = pixel intensity
- `imshow()` image render করে
- `colorbar()` intensity scale দেখায়

---

## 📄 2. 02_grayscale_image.py

### 🔹 Purpose

- Grayscale image visualization

### 🧾 Code

```python
plt.imshow(gray_image, cmap="gray")
```

### 🧠 Explanation

- 0 → black
- 255 → white
- `cmap="gray"` image কে black-white style দেয়

---

## 📄 3. 03_rgb_image.py

### 🔹 Purpose

- RGB image concept বোঝা

### 🧾 Code

```python
plt.imshow(rgb_image)
```

### 🧠 Explanation

- প্রতিটি pixel = [R, G, B]
- Red, Green, Blue mix হয়ে color তৈরি হয়
- Real image representation

---

## 📄 4. 04_interpolation.py

### 🔹 Purpose

- Image smoothness control শেখা

### 🧾 Code

```python
plt.imshow(image, interpolation="bilinear")
```

### 🧠 Explanation

- `nearest` → pixelated view
- `bilinear` → smooth
- `bicubic` → more smooth & professional

---

## 📄 5. 05_colorbar_explained.py

### 🔹 Purpose

- Color scale বোঝা

### 🧾 Code

```python
plt.colorbar()
```

### 🧠 Explanation

- Value → color mapping দেখায়
- Data intensity বুঝতে সাহায্য করে

---

## 📄 6. 06_zoom_and_crop_image.py

### 🔹 Purpose

- Image cropping / zooming শেখা

### 🧾 Code

```python
cropped = image[3:8, 3:8]
```

### 🧠 Explanation

- slicing ব্যবহার করে image অংশ select করা হয়
- zoom effect তৈরি করা যায়
- image processing basic concept

---

## 📄 7. 07_csv_image_visualization.py

### 🔹 Purpose

- CSV data থেকে image তৈরি করা

### 🧾 Code

```python
plt.imshow(data, cmap="gray")
```

### 🧠 Explanation

- CSV matrix → image
- numbers = pixels
- data visualization + image processing combined

---

## ⚙️ Implementation Flow

- Matrix data তৈরি করা হয়েছে
- Grayscale image display করা হয়েছে
- RGB image concept বোঝা হয়েছে
- Interpolation styles compare করা হয়েছে
- Image cropping করা হয়েছে
- CSV data → image visualization করা হয়েছে

---

## 📈 Output / Result

### Key findings:

- `imshow()` image rendering tool
- Grayscale = single channel intensity
- RGB = color mixing system
- Interpolation image quality control করে
- CSV data থেকেও image তৈরি সম্ভব

---

## 🚀 What I Learned

- Image representation using arrays
- Grayscale vs RGB difference
- Interpolation techniques
- Image cropping concept
- Data → Image conversion

---

## 🧠 Key Concepts (Quick Revision)

- `imshow()` → image display
- `cmap="gray"` → grayscale image
- RGB → 3 channel color system
- interpolation → image smoothness
- slicing → cropping technique
- colorbar → intensity scale

---

## 📝 Notes

- Image data ভুল হলে visualization ভুল হবে
- RGB image always 3D array
- Large images memory heavy হতে পারে
- interpolation selection important for quality

---

## 📌 Next Day Preview

- Contour Plot
- 2D function visualization
- Scientific surface mapping
- Advanced mathematical visualization

---

## ⭐ Bonus (Optional)

### 🔥 Improvements Ideas

- Image editor mini tool বানানো
- CSV → image converter app
- Real photo pixel analyzer
- Interactive zoom tool

### 🧪 Practice Ideas

- Random noise image visualize করো
- RGB color mixer simulation বানাও
- Image crop tool তৈরি করো
- Black-white filter experiment করো

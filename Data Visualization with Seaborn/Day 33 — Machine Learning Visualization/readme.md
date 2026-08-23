# 📅 Day 33 — Machine Learning Visualization (Seaborn + Scikit-learn)

---

# 🎯 Objective

- Machine Learning mindset এর সাথে visualization connect করা
- Feature vs target relationship বোঝা
- Multiple features একসাথে analyze করা
- Simple Linear Regression model visualize করা
- Prediction vs actual compare করা
- Residual (error) analysis করা
- Feature importance বুঝা (correlation-based)

---

# 📚 Topics Covered

- Feature vs target visualization
- Multi-variable relationship analysis
- Correlation heatmap for ML
- Linear Regression visualization
- Prediction vs actual comparison
- Residual analysis (error understanding)
- Target distribution analysis
- Feature importance (correlation-based)
- ML-style dashboard creation

---

# 📁 Dataset

## 📌 File Name: `ml_data.csv`

## 📌 Description

একটি simple synthetic dataset যেখানে student performance based prediction problem তৈরি করা হয়েছে।

## 📌 Columns

- `study_hours` → daily study time
- `attendance` → class attendance percentage
- `previous_score` → previous exam score
- `final_score` → target variable (exam result)

---

# 📁 Project Structure

```bash id="ml33_structure"
day-33/
│── ml_data.csv
│── 01_feature_relationship.py
│── 02_multi_feature_analysis.py
│── 03_correlation_ml.py
│── 04_simple_ml_model_visual.py
│── 05_residual_analysis.py
│── 06_distribution_target_analysis.py
│── 07_feature_importance_visual.py
│── 08_full_ml_insight_dashboard.py
│── README.md
```

---

# 💻 Code Breakdown (File by File)

---

# 📄 1. 01_feature_relationship.py

## 🔹 Purpose

- Single feature vs target relationship বোঝা

## 🧾 Code

```python id="ml33_1"
sns.scatterplot(data=df, x="study_hours", y="final_score")
```

## 🧠 Explanation

- Study hours increase → score increase pattern দেখা যায়
- Basic ML intuition build করে

---

# 📄 2. 02_multi_feature_analysis.py

## 🔹 Purpose

- Multiple feature impact analyze করা

## 🧾 Code

```python id="ml33_2"
sns.scatterplot(
    data=df,
    x="attendance",
    y="final_score",
    hue="study_hours",
    size="previous_score"
)
```

## 🧠 Explanation

- Multiple variables একসাথে relationship show করে
- Real ML problems multi-factor based

---

# 📄 3. 03_correlation_ml.py

## 🔹 Purpose

- Feature importance intuition build করা

## 🧾 Code

```python id="ml33_3"
corr = df.corr()

sns.heatmap(corr, annot=True, cmap="coolwarm", center=0)
```

## 🧠 Explanation

- Correlation matrix → feature strength বোঝায়
- High correlation = strong predictor

---

# 📄 4. 04_simple_ml_model_visual.py

## 🔹 Purpose

- Linear Regression model visualize করা

## 🧾 Code

```python id="ml33_4"
model = LinearRegression()
model.fit(X, y)

df["predicted"] = model.predict(X)

sns.scatterplot(data=df, x="study_hours", y="final_score")
sns.lineplot(data=df, x="study_hours", y="predicted")
```

## 🧠 Explanation

- Actual vs predicted comparison
- Model learning behavior visualize করা

---

# 📄 5. 05_residual_analysis.py

## 🔹 Purpose

- Model error (residual) analyze করা

## 🧾 Code

```python id="ml33_5"
df["residual"] = df["final_score"] - df["predicted"]

sns.scatterplot(data=df, x="predicted", y="residual")
plt.axhline(0, color="red")
```

## 🧠 Explanation

- Residual = actual - predicted
- Error pattern বুঝতে সাহায্য করে
- Ideal model → residual random spread

---

# 📄 6. 06_distribution_target_analysis.py

## 🔹 Purpose

- Target variable distribution বোঝা

## 🧾 Code

```python id="ml33_6"
sns.histplot(df["final_score"], kde=True)
```

## 🧠 Explanation

- Score distribution normal কিনা দেখা হয়
- Model performance understanding এ সাহায্য করে

---

# 📄 7. 07_feature_importance_visual.py

## 🔹 Purpose

- Feature importance estimate করা

## 🧾 Code

```python id="ml33_7"
corr = df.corr()["final_score"].drop("final_score")

sns.barplot(x=corr.index, y=corr.values)
```

## 🧠 Explanation

- Which feature matters most?
- Study hours usually strongest predictor

---

# 📄 8. 08_full_ml_insight_dashboard.py

## 🔹 Purpose

- Full ML analysis dashboard তৈরি করা

## 🧾 Code

```python id="ml33_8"
fig, axes = plt.subplots(2, 2)

sns.scatterplot(data=df, x="study_hours", y="final_score", ax=axes[0,0])
sns.lineplot(data=df, x="study_hours", y="predicted", ax=axes[0,1])
sns.scatterplot(data=df, x="predicted", y="residual", ax=axes[1,0])
sns.histplot(df["final_score"], kde=True, ax=axes[1,1])
```

## 🧠 Explanation

- Full ML pipeline in one view
- Feature → prediction → error → distribution

---

# ⚙️ Implementation Flow

- Dataset load করা হয়েছে
- Feature vs target relationship analyze করা হয়েছে
- Multi-variable visualization করা হয়েছে
- Correlation heatmap তৈরি করা হয়েছে
- Linear regression model train করা হয়েছে
- Prediction visualize করা হয়েছে
- Residual analysis করা হয়েছে
- Final ML dashboard তৈরি করা হয়েছে

---

# 📈 Output / Result

## 📌 Key Findings

- Study hours strongest predictor of final score
- Attendance also affects performance
- Previous score contributes to prediction
- Model fits data almost linearly
- Residuals show small error pattern

---

# 🚀 What I Learned

- ML visualization workflow
- Feature engineering intuition
- Model interpretation using plots
- Prediction vs actual comparison
- Error analysis (residuals)
- Feature importance using correlation

---

# 🧠 Key Concepts (Quick Revision)

- Feature = input variable
- Target = output variable
- Correlation = relationship strength
- Prediction = model output
- Residual = error (actual - predicted)
- Visualization = ML understanding tool

---

# 📝 Notes

## 📌 Common Mistakes

- correlation = causation ধরে নেওয়া
- residual analysis ignore করা
- single feature dependency assumption

## 📌 Optimization Tips

- Always visualize before modeling
- Multiple features always check করা
- Error pattern analyze করা must

---

# 📌 Next Day Preview

## 📅 Day 34 — Dashboard Style Visualization

আগামী দিনে শিখবে:

- Multi-plot dashboards
- Business + ML combined views
- Insight storytelling
- Professional presentation layouts

---

# ⭐ Bonus

## 🔥 Improvement Ideas

- Multiple ML models compare করা
- Polynomial regression visualize করা
- Real dataset (Kaggle) apply করা

---

## 🧪 Practice Ideas

- attendance vs final_score analyze করো
- previous_score importance check করো
- residual pattern try to interpret করো

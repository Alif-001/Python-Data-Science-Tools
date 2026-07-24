# =========================================
# Merge with multiple columns (advanced)
# =========================================

import pandas as pd

emp = pd.read_csv("employees.csv")

# 👉 extra dataset
dept_info = pd.DataFrame({
    'Department': ['IT', 'HR', 'Finance'],
    'Location': ['Dhaka', 'Sylhet', 'Rajshahi']
})

# 👉 merge using Department
merged = pd.merge(emp, dept_info, on='Department', how='left')

print(merged)

# 👉 explanation:
# multiple dataset join করা যায়
# =========================================
# join() - Basic Index Based Join
# =========================================

import pandas as pd

emp = pd.read_csv("employees.csv")
sal = pd.read_csv("salary.csv")

# 👉 EmpID কে index বানানো
emp = emp.set_index('EmpID')
sal = sal.set_index('EmpID')

# 👉 join (index based merge)
df = emp.join(sal)

print(df)

# 👉 explanation:
# join() = index based combine
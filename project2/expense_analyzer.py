import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("expenses.csv")

total_by_category = df.groupby("Category")["Amount"].sum()
highest_expense = df.loc[df["Amount"].idxmax()]

print("Total spending by category:")
print(total_by_category)
print("\nHighest single expense:")
print(highest_expense)

total_by_category.plot(kind="bar", color="skyblue")
plt.title("Monthly Expenses by Category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

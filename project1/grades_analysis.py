import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("grades.csv")

subjects = ["Math", "English", "IT"]

averages = df[subjects].mean()
maximums = df[subjects].max()
minimums = df[subjects].min()

print("Average scores:")
print(averages)
print("\nMaximum scores:")
print(maximums)
print("\nMinimum scores:")
print(minimums)

averages.plot(kind="bar", color="lightgreen")
plt.title("Average Student Grades by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

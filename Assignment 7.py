import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1. Load the CSV dataset[cite: 3]
df = pd.read_csv("sample_data_assignment_07.csv")

# Display the dataset[cite: 3]
print("Dataset:")
print(df)

# --- Main Assignment Plots ---

# Line Plot[cite: 3]
plt.figure(figsize=(7, 4.5))
plt.plot(df["Student"], df["Python"], marker="o")
plt.title("Python Marks of Students")
plt.xlabel("Student")
plt.ylabel("Python Marks")
plt.grid(True)
plt.show()

# Bar Plot[cite: 3]
plt.figure(figsize=(7, 4.5))
plt.bar(df["Student"], df["Maths"])
plt.title("Maths Marks of Students")
plt.xlabel("Student")
plt.ylabel("Maths Marks")
plt.show()

# Scatter Plot[cite: 3]
plt.figure(figsize=(7, 4.5))
plt.scatter(df["Maths"], df["Python"], s=70)
plt.title("Maths vs Python Marks")
plt.xlabel("Maths Marks")
plt.ylabel("Python Marks")
plt.grid(True)
plt.show()

# Correlation Matrix and Heatmap[cite: 3]
correlation = df[["Maths", "Python", "Attendance"]].corr()
print("\nCorrelation Matrix:")
print(correlation)

plt.figure(figsize=(6.5, 5))
sns.heatmap(correlation, annot=True, cmap="Blues", vmin=-1, vmax=1)
plt.title("Correlation Heatmap")
plt.show()


# --- Challenge / Extension Task ---[cite: 6]
print("\n--- Challenge Task Summary & Extra Plots ---")

# Calculate and display average scores[cite: 6]
print(f"Average Maths Marks: {df['Maths'].mean():.2f}")
print(f"Average Python Marks: {df['Python'].mean():.2f}")
print(f"Average Attendance: {df['Attendance'].mean():.2f}")

# Histogram of Python marks[cite: 6]
plt.figure(figsize=(7, 4.5))
plt.hist(
    df["Python"], bins=4, color="skyblue", edgecolor="black", label="Python"
)
plt.title("Histogram of Python Marks")
plt.xlabel("Marks Range")
plt.ylabel("Frequency")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()

# Box Plot for Maths and Python marks[cite: 6]
plt.figure(figsize=(7, 4.5))
plt.boxplot(
    [df["Maths"], df["Python"]],
    labels=["Maths", "Python"],
    patch_artist=True,
    boxprops=dict(facecolor="lightgreen"),
)
plt.title("Box Plot for Maths and Python Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.grid(True, linestyle="--", alpha=0.7)
plt.show()

# Pie chart showing student distribution by city[cite: 6]
city_counts = df["City"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(
    city_counts,
    labels=city_counts.index,
    autopct="%1.1f%%",
    startangle=140,
    colors=["#ff9999", "#66b3ff", "#99ff99"],
)
plt.title("Proportion of Students by City")
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the Excel file
df = pd.read_excel("array.xlsx")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("\n ASSIGNMENT 6: DATA PREPROCESSING ")

# Display original dataset
print("\nOriginal Dataset:")
print(df)

print("\nNumber of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

# Display first five records
print("\nFirst Five Records:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
df.info()

# Remove extra spaces from text values
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()
    df[col] = df[col].replace("", np.nan)

# Convert Age and Marks into numeric values
print("\nData Type Conversion:")

for col in ["Age", "Marks"]:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].replace([np.inf, -np.inf], np.nan)
        print(col, "converted into numeric type.")

print("\nData Types:")
print(df.dtypes)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

print("\nTotal Missing Values:", df.isnull().sum().sum())

# Count duplicate records
print("\nDuplicate Records:")
print("Total duplicates:", df.duplicated().sum())

# Fill missing values
print("\nHandling Missing Values:")

for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        if df[col].notna().any():
            df[col] = df[col].fillna(df[col].mean())
            print(col, "filled with mean value")

    else:
        if not df[col].mode().empty:
            df[col] = df[col].fillna(df[col].mode()[0])
            print(col, "filled with most common value")

# Remove duplicate records
df = df.drop_duplicates()
df = df.reset_index(drop=True)

print("\nAfter Removing Duplicates:")
print(df)

print("\nRemaining Rows:", len(df))

# Display cleaned dataset
print("\nCleaned Dataset:")
print(df.to_string(index=False))

# Display final dataset information
print("\nFinal Dataset Information:")
df.info()

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicates After Cleaning:")
print(df.duplicated().sum())

# Plot student marks using Matplotlib
plt.figure(figsize=(8, 5))

plt.bar(df["Name"], df["Marks"])

plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Save the cleaned dataset
df.to_csv("preprocessed_array.csv", index=False)

print("\nCleaned data saved as preprocessed_array.csv")

print("\n DATA PREPROCESSING COMPLETED ")

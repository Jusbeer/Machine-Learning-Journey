import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load dataset
df = pd.read_csv("C:/Users/jusbe/Desktop/pythonProject/Leaning Machine Learning/archive/StudentsPerformance.csv")
original_cols = df.columns.tolist()
print("Dataset loaded.")
print("Initial shape:", df.shape)

# STEP 1: Check for Missing Values
print("\nSTEP 1: Checking Missing Values")
missing_counts = df.isnull().sum()
total_rows = len(df)

for col in df.columns:
    missing = missing_counts[col]
    if missing > 0:
        percent_missing = (missing / total_rows) * 100
        print(f"⚠️ '{col}': {missing} missing ({percent_missing:.1f}%)")
        if percent_missing > 50:
            df.drop(columns=[col], inplace=True)
            print(f"Dropped column '{col}' (too many missing values)")
print("✅ Missing value handling complete.")

# STEP 2: Drop Unnecessary Columns (Customize this as needed)
print("\nSTEP 2: Dropping Unnecessary Columns")
# Example: df.drop(columns=['student_id'], inplace=True)
print("No columns dropped (customize this step as needed).")

# STEP 3: Encode Categorical Columns
print("\nSTEP 3: Encoding Categorical Columns")
label_encoder = LabelEncoder()
for col in df.select_dtypes(include='object').columns:
    print(f"➤ Encoding '{col}'")
    df[col] = label_encoder.fit_transform(df[col])
print("✅ Encoding complete.")

# STEP 4: Fix Data Types
print("\nSTEP 4: Fixing Data Types")
# Pandas usually handles this well, but you can check:
# df = df.astype({'math score': 'int'})
print("✅ Data type checks complete.")

# STEP 5: Feature Scaling
print("\nSTEP 5: Feature Scaling")
scaler = StandardScaler()
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])
print("✅ Features scaled using StandardScaler (mean=0, std=1).")

# STEP 6: Outlier Detection (Basic)
print("\nSTEP 6: Outlier Detection (basic)")
for col in numeric_cols:
    outliers = np.sum(np.abs(df[col]) > 3)
    if outliers > 0:
        print(f"⚠️ Column '{col}' has {outliers} possible outliers (> |3 std|)")

# Save cleaned dataset
df.to_csv("C:/Users/jusbe/Desktop/pythonProject/Leaning Machine Learning/archive/StudentsPerformance_cleaned.csv", index=False)
print("\nCleaned dataset saved as 'StudentsPerformance_cleaned.csv'")

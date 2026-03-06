What is Data QA?

Data QA (Quality Assurance) in AI/ML ensures that the data you use to train models is clean, consistent, and reliable. Poor data can cause models to make bad predictions, so checking data before training is critical.

Key goals of Data QA:

Detect errors, missing values, or inconsistent formats.

Identify unusual patterns that could skew model results.

Ensure data is in the right format for ML pipelines.

Key Checks in Data QA:
a. Outliers

Definition: Values that are very different from most of the data.

Why: Outliers can distort model training (e.g., predicting house prices with one extremely expensive property).

How to check:

Visual: Boxplots, scatter plots.

Statistical: Values outside 1.5× IQR (interquartile range) or ±3 standard deviations.

Python example:

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# Boxplot to visualize outliers
sns.boxplot(x=df['age'])
plt.show()

# Detect using IQR
Q1 = df['age'].quantile(0.25)
Q3 = df['age'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['age'] < Q1 - 1.5*IQR) | (df['age'] > Q3 + 1.5*IQR)]
print(outliers)


b. Inconsistent Values

Definition: Values that don’t follow a consistent format or expected categories.

Examples:

Gender column: Male, M, male → inconsistent.

Date column: 2023-01-02, 01/02/2023 → different formats.

How to check:
# Unique values in a column
print(df['gender'].unique())

# Convert to consistent format
df['gender'] = df['gender'].str.lower().replace({'m': 'male', 'f': 'female'})

c. Distributions

Definition: Understanding how data values are spread.

Why: Helps detect skewness, missing ranges, or unexpected patterns.

How to check:

# Histogram
df['age'].hist(bins=20)
plt.show()

# Value counts for categorical data
print(df['gender'].value_counts())

Upload Validation Scripts

Validation scripts are automated scripts that check for:

Missing or null values

Outliers

Inconsistent formatting

Duplicate rows

Example simple validation script:

def validate_data(df):
    print("Missing values:\n", df.isnull().sum())
    print("\nDuplicate rows:", df.duplicated().sum())
    print("\nColumn distributions:\n", df.describe())
    
    # Example outlier check
  for col in df.select_dtypes(include=['int', 'float']):
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        outliers = df[(df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)]
        print(f"\nOutliers in {col}:", outliers.shape[0])
        
validate_data(df)


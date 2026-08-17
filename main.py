import pandas as pd
file_path = "C:/Users/Administrator/Downloads/research-and-development-survey-2025.csv"
df = pd.read_csv(file_path)
print("Dataset imported successfully 1\n",df)
print("="*60)

print("1. first  5 rows")
print("="*60)
print(df.head(),"\n")

print("="*60)
print("2. DATASET DIMENSIONS")
print("="*60)
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}\n")

print("="*60)
print("3. COLUMN NAMES & DATA TYPES")
print("="*60)
print(df.dtypes,"\n")

print("="*60)
print("4. CONCISE SUMMARY")
print("="*60)
df.info()
print("\n")

print("="*60)
print("5. MISSING VALUES CHECK")
print("="*60)
missing_data = df.isnull().sum()
print(missing_data[missing_data>0] if missing_data.sum()>0 else "no missing data")
print("\n")

print("="*60)
print("6. DUPLICATE ROWS CHECK")
print("="*60)
print(f"Number of duplicate rows: {df.duplicated().sum()}\n")

print("="*60)
print("7.  NUMERICAL SUMMARY STATISTICS")
print("="*60)
print(df.describe().T,"\n")

print("="*60)
print("8.CATEGORICAL SUMMARY STATISTICS")
print("="*60)
print(df.describe(include=['object', 'category']).count(), "\n")

print("="*60)
print("9. VALUE COUNTS FOR CATEGORICAL COLUMNS")
print("="*60)

print("="*60)
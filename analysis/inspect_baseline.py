import pandas as pd

FILE = "/home/aiops/dataset/processed/baseline_normal.csv"

df = pd.read_csv(FILE)

print("=" * 70)
print("BASELINE DATASET INSPECTION")
print("=" * 70)

print("\nJumlah baris :", len(df))
print("Jumlah kolom:", len(df.columns))

print("\nKolom:")
for col in df.columns:
    print("-", col)

print("\nTipe data:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

numeric = df.select_dtypes(include="number")

print("\nSTATISTIK DESKRIPTIF")
print(numeric.describe().T)

print("\nMinimum:")
print(numeric.min())

print("\nMaximum:")
print(numeric.max())

print("\nMedian:")
print(numeric.median())

print("\nPemeriksaan selesai.")

import pandas as pd

DATASET = "/home/aiops/dataset/raw/infrastructure_metrics.csv"

print("=" * 60)
print("AIOps Infrastructure Dataset Inspection")
print("=" * 60)

# Membaca dataset
df = pd.read_csv(DATASET)

print("\n[1] Ukuran Dataset")
print("Jumlah baris :", len(df))
print("Jumlah kolom :", len(df.columns))

print("\n[2] Nama Kolom")
for column in df.columns:
    print("-", column)

print("\n[3] Tipe Data")
print(df.dtypes)

print("\n[4] Lima Data Pertama")
print(df.head())

print("\n[5] Lima Data Terakhir")
print(df.tail())

print("\n[6] Missing Value")
print(df.isnull().sum())

print("\n[7] Duplikasi")
print("Jumlah baris duplikat:", df.duplicated().sum())

print("\n[8] Statistik Numerik")
print(df.describe())

print("\n" + "=" * 60)
print("Inspection selesai")
print("=" * 60)

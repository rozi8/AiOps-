import pandas as pd

INPUT_FILE = "/home/aiops/dataset/raw/infrastructure_metrics.csv"
OUTPUT_FILE = "/home/aiops/dataset/processed/baseline_normal.csv"

START_TIME = "2026-09-22 23:01:22"

df = pd.read_csv(INPUT_FILE)

df["timestamp"] = pd.to_datetime(df["timestamp"])

baseline = df[df["timestamp"] >= START_TIME].copy()

baseline.to_csv(OUTPUT_FILE, index=False)

print("=" * 60)
print("BASELINE DATASET")
print("=" * 60)

print("Mulai :", baseline["timestamp"].min())
print("Akhir :", baseline["timestamp"].max())
print("Jumlah data :", len(baseline))

print("\nFile:")
print(OUTPUT_FILE)

print("\nMissing values:")
print(baseline.isnull().sum())

print("\nDuplikasi:")
print(baseline.duplicated().sum())

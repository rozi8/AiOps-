import pandas as pd

FILE = "/home/aiops/dataset/processed/baseline_normal.csv"

df = pd.read_csv(FILE)
df["timestamp"] = pd.to_datetime(df["timestamp"])

interval = df["timestamp"].diff().dt.total_seconds().dropna()

normal_15s = interval.between(14.5, 15.5)
near_16s = interval.between(15.5, 16.5)
gap = interval > 30

print("=" * 60)
print("BASELINE INTERVAL CHECK")
print("=" * 60)

print("\nJumlah data :", len(df))

print("\nPeriode:")
print("Mulai :", df["timestamp"].min())
print("Akhir :", df["timestamp"].max())

print("\nInterval:")
print("Minimum :", interval.min(), "detik")
print("Maximum :", interval.max(), "detik")
print("Median  :", interval.median(), "detik")
print("Mean    :", interval.mean(), "detik")

print("\nKlasifikasi interval:")
print("Sekitar 15 detik :", normal_15s.sum())
print("Sekitar 16 detik :", near_16s.sum())
print("Gap > 30 detik   :", gap.sum())

print("\nInterval selain sekitar 15 detik:")
print((~normal_15s).sum())

if gap.sum() > 0:
    print("\nGAP:")
    print(interval[gap].to_string())

print("\nMissing timestamp :", df["timestamp"].isna().sum())
print("Duplicate row    :", df.duplicated().sum())

print("\nPemeriksaan selesai.")

import pandas as pd

FILE = "/home/aiops/dataset/raw/infrastructure_metrics.csv"

df = pd.read_csv(FILE)
df["timestamp"] = pd.to_datetime(df["timestamp"])

interval = df["timestamp"].diff().dt.total_seconds().dropna()

# Toleransi untuk floating point
normal_15s = interval.between(14.5, 15.5)
near_16s = interval.between(15.5, 16.5)
abnormal = ~normal_15s

print("=" * 60)
print("AIOps Dataset Interval Check")
print("=" * 60)

print("\nJumlah data :", len(df))

print("\nPeriode data:")
print("Mulai :", df["timestamp"].min())
print("Akhir :", df["timestamp"].max())

print("\nInterval:")
print("Minimum :", interval.min(), "detik")
print("Maximum :", interval.max(), "detik")
print("Median  :", interval.median(), "detik")
print("Mean    :", interval.mean(), "detik")

print("\nJumlah interval:")
print("Sekitar 15 detik :", normal_15s.sum())
print("Sekitar 16 detik :", near_16s.sum())
print("Di luar toleransi :", abnormal.sum())

print("\nInterval yang tidak normal:")
print(
    interval[abnormal]
    .value_counts()
    .sort_index()
)

print("\nMissing timestamp:")
print(df["timestamp"].isna().sum())

print("\nPemeriksaan selesai.")

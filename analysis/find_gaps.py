import pandas as pd

FILE = "/home/aiops/dataset/raw/infrastructure_metrics.csv"

df = pd.read_csv(FILE)
df["timestamp"] = pd.to_datetime(df["timestamp"])

df["interval_seconds"] = (
    df["timestamp"].diff().dt.total_seconds()
)

gaps = df[df["interval_seconds"] > 30].copy()

print("=" * 70)
print("AIOps Dataset Gap Detection")
print("=" * 70)

print("\nJumlah gap > 30 detik :", len(gaps))

for _, row in gaps.iterrows():
    print("\nTimestamp sebelumnya :", 
          df.loc[row.name - 1, "timestamp"])

    print("Timestamp berikutnya  :", row["timestamp"])

    print("Gap                   :", 
          row["interval_seconds"], "detik")

print("\nPemeriksaan selesai.")

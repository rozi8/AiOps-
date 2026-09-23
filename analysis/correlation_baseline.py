import pandas as pd

FILE = "/home/aiops/dataset/processed/baseline_normal.csv"

df = pd.read_csv(FILE)

features = [
    "cpu_usage_percent",
    "memory_usage_percent",
    "load_1m",
    "swap_usage_percent",
    "disk_usage_percent",
    "disk_read_bytes_per_sec",
    "disk_write_bytes_per_sec",
    "network_rx_bytes_per_sec",
    "network_tx_bytes_per_sec"
]

corr = df[features].corr()

print("=" * 80)
print("KORELASI ANTAR FITUR BASELINE")
print("=" * 80)

print("\nMatriks korelasi:")
print(corr.round(3))

print("\nPasangan korelasi kuat (|r| >= 0.70):")

found = False

for i in range(len(features)):
    for j in range(i + 1, len(features)):
        value = corr.iloc[i, j]

        if abs(value) >= 0.70:
            print(
                f"{features[i]} <-> {features[j]} : "
                f"{value:.3f}"
            )
            found = True

if not found:
    print("Tidak ditemukan pasangan dengan |r| >= 0.70.")

print("\nPemeriksaan korelasi selesai.")

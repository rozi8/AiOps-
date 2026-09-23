import pandas as pd
import matplotlib.pyplot as plt

DATASET = "/home/aiops/dataset/raw/infrastructure_metrics.csv"

df = pd.read_csv(DATASET)
df["timestamp"] = pd.to_datetime(df["timestamp"])

print("=" * 60)
print("AIOps Infrastructure Dataset Visualization")
print("=" * 60)

print("\nJumlah data :", len(df))
print("Periode     :", df["timestamp"].min(), "s/d", df["timestamp"].max())

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

for feature in features:
    plt.figure(figsize=(10, 4))

    plt.plot(df["timestamp"], df[feature])

    plt.title(feature)
    plt.xlabel("Timestamp")
    plt.ylabel(feature)
    plt.xticks(rotation=45)
    plt.tight_layout()

    output = "/home/aiops/analysis/" + feature + ".png"
    plt.savefig(output)
    plt.close()

    print("Saved:", output)

print("\nVisualisasi selesai.")

import pandas as pd
import matplotlib.pyplot as plt
import os

INPUT_FILE = "/home/aiops/dataset/processed/baseline_normal.csv"
OUTPUT_DIR = "/home/aiops/analysis/baseline_plots"

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(INPUT_FILE)

df["timestamp"] = pd.to_datetime(df["timestamp"])

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

    plt.figure(figsize=(14, 5))

    plt.plot(
        df["timestamp"],
        df[feature]
    )

    plt.title(f"Baseline - {feature}")
    plt.xlabel("Timestamp")
    plt.ylabel(feature)
    plt.grid(True)

    plt.tight_layout()

    output_file = os.path.join(
        OUTPUT_DIR,
        f"{feature}.png"
    )

    plt.savefig(output_file)
    plt.close()

    print(f"[OK] {output_file}")

print("\nSemua visualisasi selesai.")

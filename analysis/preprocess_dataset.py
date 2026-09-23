import pandas as pd
from sklearn.preprocessing import StandardScaler

INPUT_FILE = "/home/aiops/dataset/raw/infrastructure_metrics.csv"
OUTPUT_FILE = "/home/aiops/dataset/processed/infrastructure_scaled.csv"

FEATURES = [
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

print("=" * 60)
print("AIOps Dataset Preprocessing")
print("=" * 60)

df = pd.read_csv(INPUT_FILE)

df["timestamp"] = pd.to_datetime(df["timestamp"])

X = df[FEATURES]

print("\n[1] Data sebelum scaling")
print(X.head())

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

df_scaled = pd.DataFrame(
    X_scaled,
    columns=FEATURES
)

df_scaled.insert(0, "timestamp", df["timestamp"])

df_scaled.to_csv(OUTPUT_FILE, index=False)

print("\n[2] Data setelah scaling")
print(df_scaled.head())

print("\n[3] Output")
print(OUTPUT_FILE)

print("\nPreprocessing selesai.")

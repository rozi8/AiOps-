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

result = []

for feature in features:
    mean = df[feature].mean()
    std = df[feature].std()
    variance = df[feature].var()

    if mean != 0:
        cv = (std / mean) * 100
    else:
        cv = 0

    result.append({
        "feature": feature,
        "mean": mean,
        "std": std,
        "variance": variance,
        "cv_percent": cv
    })

result_df = pd.DataFrame(result)

print("=" * 100)
print("ANALISIS VARIABILITAS FITUR")
print("=" * 100)

print(
    result_df.to_string(
        index=False,
        float_format=lambda x: f"{x:.6f}"
    )
)

print("\nKeterangan:")
print("CV = (standard deviation / mean) × 100%")

print("\nFitur dengan variance = 0:")
for _, row in result_df.iterrows():
    if row["variance"] == 0:
        print("-", row["feature"])

print("\nAnalisis selesai.")

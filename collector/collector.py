import csv
import json
import os
import time
import urllib.parse
import urllib.request
from datetime import datetime

PROMETHEUS_URL = "http://127.0.0.1:9090/api/v1/query"
OUTPUT_FILE = "/home/aiops/dataset/raw/infrastructure_metrics.csv"
INTERVAL = 15

QUERIES = {
    "cpu_usage_percent":
        '100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[1m])) * 100)',

    "memory_usage_percent":
        '(1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) * 100',

    "load_1m":
        'node_load1',

    "swap_usage_percent":
        '(1 - node_memory_SwapFree_bytes / node_memory_SwapTotal_bytes) * 100',

    "disk_usage_percent":
        '100 * (1 - node_filesystem_avail_bytes{mountpoint="/",fstype!~"tmpfs|overlay"} / node_filesystem_size_bytes{mountpoint="/",fstype!~"tmpfs|overlay"})',

    "disk_read_bytes_per_sec":
        'rate(node_disk_read_bytes_total{device="sda"}[1m])',

    "disk_write_bytes_per_sec":
        'rate(node_disk_written_bytes_total{device="sda"}[1m])',

    "network_rx_bytes_per_sec":
        'rate(node_network_receive_bytes_total{device="enp0s25"}[1m])',

    "network_tx_bytes_per_sec":
        'rate(node_network_transmit_bytes_total{device="enp0s25"}[1m])'
}


def query_prometheus(query):
    params = urllib.parse.urlencode({"query": query})
    url = f"{PROMETHEUS_URL}?{params}"

    with urllib.request.urlopen(url, timeout=10) as response:
        data = json.loads(response.read().decode())

    results = data["data"]["result"]

    if not results:
        return None

    return float(results[0]["value"][1])


def collect_metrics():
    metrics = {}

    for name, query in QUERIES.items():
        try:
            metrics[name] = query_prometheus(query)
        except Exception as error:
            print(f"[ERROR] {name}: {error}")
            metrics[name] = None

    return metrics


def save_metrics(metrics):
    file_exists = os.path.isfile(OUTPUT_FILE)

    fieldnames = [
        "timestamp",
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

    with open(OUTPUT_FILE, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        row = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            **metrics
        }

        writer.writerow(row)


print("AIOps Infrastructure Collector started.")
print(f"Output: {OUTPUT_FILE}")
print(f"Interval: {INTERVAL} seconds")

while True:
    metrics = collect_metrics()

    save_metrics(metrics)

    print(
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        metrics
    )

    time.sleep(INTERVAL)

# AIOps Infrastructure Anomaly Detection

Implementasi **deteksi anomali multivariat pada infrastruktur server menggunakan Isolation Forest** sebagai bagian dari penelitian tugas akhir.

## Gambaran Umum

Proyek ini mengimplementasikan pipeline AIOps untuk mendeteksi perilaku anomali pada infrastruktur server dengan menganalisis beberapa metrik sistem secara simultan.

Berbeda dengan pemantauan berbasis ambang batas pada satu metrik, pendekatan ini menggunakan **Isolation Forest** untuk mengidentifikasi pola penggunaan sumber daya yang tidak biasa berdasarkan hubungan multivariat antar metrik infrastruktur.

## Arsitektur

```text id="d4w6uk"
Server
  │
  ▼
Node Exporter
  │
  ▼
Prometheus
  │
  ▼
Python Collector
  │
  ▼
Dataset Infrastruktur
  │
  ▼
Preprocessing
  │
  ▼
Isolation Forest
  │
  ▼
Normal / Anomali
```

## Metrik yang Dipantau

* Penggunaan CPU
* Penggunaan memori
* System load 1 menit
* Penggunaan swap
* Penggunaan disk
* Throughput disk read/write
* Throughput jaringan RX/TX

Metrik dikumpulkan dengan interval sekitar **15 detik**.

## Teknologi

| Komponen         | Teknologi        |
| ---------------- | ---------------- |
| Sistem Operasi   | Debian Linux     |
| Exporter         | Node Exporter    |
| Monitoring       | Prometheus       |
| Pengumpulan Data | Python           |
| Pengolahan Data  | Pandas, NumPy    |
| Machine Learning | Scikit-learn     |
| Model            | Isolation Forest |
| Visualisasi      | Matplotlib       |
| Version Control  | Git              |

## Struktur Proyek

```text id="d3j3b9"
.
├── analysis/
│   ├── baseline_plots/
│   └── *.py
├── collector/
│   └── collector.py
├── dataset/
│   └── metadata/
├── prometheus/
│   └── config/
├── .gitignore
├── LICENSE
└── README.md
```

## Alur Penelitian

1. Mengumpulkan metrik infrastruktur server.
2. Membentuk dan memvalidasi dataset kondisi normal.
3. Melakukan analisis eksploratif dan preprocessing data.
4. Membangun model Isolation Forest.
5. Melakukan skenario anomali infrastruktur secara terkontrol.
6. Mengevaluasi kemampuan model dalam mendeteksi anomali.

Skenario anomali yang direncanakan meliputi **tekanan CPU, tekanan memori, tekanan disk I/O, lonjakan trafik jaringan, dan tekanan beberapa sumber daya secara bersamaan**.

## Status Pengembangan

**Status: Dalam Pengembangan**

### Selesai

* [x] Deployment Prometheus dan Node Exporter
* [x] Pengumpulan metrik infrastruktur secara otomatis
* [x] Pembentukan dataset baseline
* [x] Analisis kualitas data
* [x] Analisis variabilitas fitur
* [x] Analisis korelasi
* [x] Visualisasi baseline

### Selanjutnya

* [ ] Seleksi dan preprocessing fitur
* [ ] Implementasi Isolation Forest
* [ ] Eksperimen anomali terkontrol
* [ ] Evaluasi model

## Konteks Penelitian

Repository ini digunakan untuk mendukung penelitian tugas akhir dengan judul:

> **"Implementasi AIOps untuk Deteksi Anomali Multivariat pada Infrastruktur Server Menggunakan Isolation Forest"**

Penelitian berfokus pada **deteksi anomali pada tingkat infrastruktur server** menggunakan machine learning dalam kerangka AIOps.

## Lisensi

Proyek ini menggunakan **MIT License**. Lihat [LICENSE](LICENSE) untuk informasi selengkapnya.

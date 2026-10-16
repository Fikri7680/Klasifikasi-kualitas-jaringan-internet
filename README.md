# Klasifikasi Kualitas Jaringan Internet dengan Random Forest

Project praktikum Machine Learning untuk mengklasifikasikan kualitas jaringan internet menjadi **Baik**, **Sedang**, atau **Buruk**.

## Dataset
- File: `dataset/dataset_kualitas_jaringan.csv`
- Jumlah: 1,500 baris data
- Fitur: latency, download, upload, packet loss, jitter, dan kekuatan sinyal
- Target: `kualitas_jaringan`
- **Penting:** dataset ini dibuat secara sintetis untuk keperluan pembelajaran. Data bukan pengukuran jaringan nyata.

## Struktur folder
```text
project_machine_learning_jaringan/
├── dataset/
│   └── dataset_kualitas_jaringan.csv
├── src/
│   └── main.py
├── hasil/
│   ├── distribusi_kelas.png
│   ├── confusion_matrix.png
│   └── feature_importance.png
├── laporan_praktikum.docx
├── requirements.txt
└── README.md
```

## Fitur dataset
| Kolom | Arti | Satuan |
|---|---|---|
| `latency_ms` | Waktu respons jaringan | milidetik |
| `download_mbps` | Kecepatan unduh | Mbps |
| `upload_mbps` | Kecepatan unggah | Mbps |
| `packet_loss_pct` | Persentase paket hilang | persen |
| `jitter_ms` | Variasi waktu kedatangan paket | milidetik |
| `signal_strength_dbm` | Kekuatan sinyal | dBm |
| `kualitas_jaringan` | Label kelas yang diprediksi | Baik/Sedang/Buruk |

## Cara menjalankan dari nol

### 1. Pasang Python
Install Python 3.10 atau lebih baru dari https://www.python.org/downloads/. Saat instalasi Windows, centang **Add Python to PATH**.

### 2. Unduh project
Unduh ZIP dari GitHub, lalu ekstrak. Atau clone repository:
```bash
git clone URL_REPOSITORY_KAMU
cd project_machine_learning_jaringan
```
Ganti `URL_REPOSITORY_KAMU` dengan URL repository milikmu.

### 3. Buat virtual environment (opsional tetapi disarankan)
Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```
macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install library
```bash
python -m pip install -r requirements.txt
```

### 5. Jalankan program
Dari folder utama project:
```bash
python src/main.py
```
Program menampilkan jumlah data, distribusi kelas, akurasi, classification report, confusion matrix, serta contoh prediksi. Grafik evaluasi disimpan di folder `hasil`.

## Ringkasan evaluasi pada pembagian data 80:20
- Jumlah data latih: 1200
- Jumlah data uji: 300
- Akurasi pada proses pembuatan: 88.00%

Nilai dapat berbeda jika dataset, parameter, atau versi library diubah. Akurasi tinggi pada data sintetis tidak membuktikan model siap digunakan pada jaringan nyata.

## Algoritma
Random Forest membangun banyak pohon keputusan dan menggabungkan prediksinya. Model ini digunakan untuk klasifikasi multi-kelas.

## Mengunggah ke GitHub dari nol
1. Buat akun atau masuk di https://github.com/.
2. Klik tombol **New repository**.
3. Isi nama repository, misalnya `klasifikasi-kualitas-jaringan`.
4. Pilih Public atau Private, lalu klik **Create repository**.
5. Cara paling mudah: klik **Add file → Upload files**, lalu unggah isi folder project (bukan folder `.venv`).
6. Isi pesan commit, misalnya `Menambahkan project praktikum Machine Learning`.
7. Klik **Commit changes**.
8. Salin URL repository untuk dicantumkan pada laporan.

Alternatif menggunakan Git:
```bash
git init
git add .
git commit -m "Project klasifikasi kualitas jaringan"
git branch -M main
git remote add origin URL_REPOSITORY_KAMU
git push -u origin main
```
Perintah Git memerlukan Git yang sudah terpasang dan autentikasi GitHub.

## Catatan akademik
Dataset bersifat sintetis. Jelaskan batasan ini saat presentasi. Untuk penelitian jaringan sebenarnya, kumpulkan data pengukuran yang valid dan definisikan label kualitas berdasarkan standar atau kebutuhan yang dijelaskan dalam laporan.

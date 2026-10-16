"""
Project: Klasifikasi Kualitas Jaringan Internet
Algoritma: Random Forest
Catatan: Dataset dalam project ini adalah data sintetis untuk pembelajaran,
bukan hasil pengukuran jaringan nyata.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "dataset" / "dataset_kualitas_jaringan.csv"
RESULT_DIR = ROOT / "hasil"
RESULT_DIR.mkdir(exist_ok=True)

def main():
    # 1. Membaca dataset
    data = pd.read_csv(DATA_PATH)
    print("Lima data pertama:")
    print(data.head())
    print(f"\nJumlah data: {len(data)}")
    print("\nDistribusi kelas:")
    print(data["kualitas_jaringan"].value_counts())

    # 2. Memisahkan fitur (X) dan target (y)
    X = data.drop(columns=["kualitas_jaringan"])
    y = data["kualitas_jaringan"]

    # 3. Membagi data: 80% pelatihan, 20% pengujian
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 4. Membuat dan melatih model Random Forest
    model = RandomForestClassifier(
        n_estimators=150,
        random_state=42,
        class_weight="balanced"
    )
    model.fit(X_train, y_train)

    # 5. Melakukan prediksi dan evaluasi
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nAkurasi model: {accuracy:.4f} ({accuracy * 100:.2f}%)")
    print("\nClassification report:")
    print(classification_report(y_test, y_pred, zero_division=0))
    print("\nConfusion matrix (urutan kelas: Baik, Sedang, Buruk):")
    print(confusion_matrix(y_test, y_pred, labels=["Baik", "Sedang", "Buruk"]))

    # 6. Menyimpan confusion matrix
    cm = confusion_matrix(y_test, y_pred, labels=["Baik", "Sedang", "Buruk"])
    disp = ConfusionMatrixDisplay(cm, display_labels=["Baik", "Sedang", "Buruk"])
    disp.plot(values_format="d")
    plt.title("Confusion Matrix Random Forest")
    plt.tight_layout()
    plt.savefig(RESULT_DIR / "confusion_matrix.png", dpi=160)
    plt.close()

    # 7. Menyimpan feature importance
    importance = pd.Series(model.feature_importances_, index=X.columns).sort_values()
    importance.plot(kind="barh", figsize=(7, 4))
    plt.title("Feature Importance Random Forest")
    plt.xlabel("Importance")
    plt.tight_layout()
    plt.savefig(RESULT_DIR / "feature_importance.png", dpi=160)
    plt.close()

    # 8. Contoh prediksi data baru
    contoh = pd.DataFrame([{
        "latency_ms": 35,
        "download_mbps": 50,
        "upload_mbps": 15,
        "packet_loss_pct": 0.5,
        "jitter_ms": 4,
        "signal_strength_dbm": -55
    }])
    hasil = model.predict(contoh)[0]
    print("\nContoh input:")
    print(contoh.to_string(index=False))
    print(f"Prediksi kualitas jaringan: {hasil}")

if __name__ == "__main__":
    main()

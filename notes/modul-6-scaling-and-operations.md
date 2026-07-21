# Modul 6: Scaling with Google Cloud Operations

## Daftar Isi
- [1. Scaling with Google Cloud Operations](#1-scaling-with-google-cloud-operations)
- [2. Fundamentals of Cloud Cost Management](#2-fundamentals-of-cloud-cost-management)

---

## 1. Scaling with Google Cloud Operations
Saat organisasi berekspansi ke *cloud*, mengelola sumber daya secara efektif menjadi tantangan yang kompleks. 
* **Peran Cloud Operations:** Dianggap sebagai pemeliharaan (*care and feeding*) infrastruktur dan aplikasi *cloud* agar berjalan lancar tanpa mengabaikan aspek penting.
* **Empat Prioritas Utama:** Mengelola reliabilitas, performa, keamanan, dan efisiensi biaya secara bersamaan.
* **Fokus Modul:** 
  1. Pengendalian anggaran melalui tata kelola keuangan (*financial governance*).
  2. Pemahaman konsep inti reliabilitas untuk menjaga sistem tetap sehat dan tangguh.

---

## 2. Fundamentals of Cloud Cost Management
Teknologi *cloud* telah mengubah secara fundamental siapa yang mengontrol sumber daya IT. Kekuatan untuk mendeploy infrastruktur telah bergeser dari departemen IT terpusat ke tim individu dan pengembang (*developers*). Meskipun fleksibilitas ini mendorong inovasi, hal tersebut menghadirkan tantangan kompleks terkait anggaran dan tata kelola.

### A. Total Cost of Ownership (TCO) & Financial Models
Perpindahan ke *cloud* mengubah cara pandang organisasi terhadap pengeluaran dan nilai investasi IT (*financial foresight*):
* **CapEx (Capital Expenditure):** 
  * Karakteristik: Membeli aset fisik di muka, terikat anggaran jangka panjang, dan proses pengadaan yang lambat (*weeks of approvals*).
  * Risiko: Risiko salah prediksi pertumbuhan yang berujung pada pemborosan aset atau *downtime*.
* **OpEx (Operational Expenditure):** 
  * Karakteristik: Mengubah status perusahaan dari pemilik perangkat keras menjadi konsumen layanan. Memungkinkan fleksibilitas tinggi dan kecepatan tinggi (*agility*).
  * Risiko ("Bill Shock"): Kebebasan untuk mengaktifkan sumber daya secara instan dapat memicu lonjakan biaya jika tidak diawasi dengan cermat. Perubahan pola kerja bergeser dari pemeliharaan perangkat keras menjadi pemantauan penggunaan.

### B. Cloud Financial Governance
Karena tagihan *cloud* naik dan turun berdasarkan penggunaan aktual (*actual usage*), mengandalkan rencana anggaran tetap (*fixed plans*) saja sering kali tidak cukup untuk mencegah pembengkakan biaya. Untuk tetap terkontrol, tata kelola keuangan (*financial governance*) harus digunakan untuk melacak dan mengelola biaya secara *real-time*. 

Pendekatan ini memerlukan pembaruan di tiga area utama:
* **People (Orang):** Melibatkan kolaborasi lintas fungsi antara tim Keuangan (*Finance*), Teknologi (*Technology*), dan Bisnis/Unit Kerja untuk menyelaraskan pengeluaran dengan tujuan bisnis.
* **Process (Proses):** Pemantauan dan analisis penggunaan serta biaya *cloud* secara rutin untuk membangun budaya akuntabilitas di setiap tim agar dapat mengenali pemborosan (*waste*).
* **Technology (Teknologi):** Memanfaatkan perangkat bawaan (*built-in tools*) dari Google Cloud untuk memperoleh visibilitas penuh, menegakkan akuntabilitas, dan mengendalikan risiko pengeluaran berlebih (*overspending*).

### C. Cloud Financial Governance Best Practices
Beberapa praktik terbaik untuk meningkatkan prediktabilitas dan kontrol sumber daya *cloud*:

1. **Identifikasi Pengelola Biaya (Define Ownership & Accountability)**
   * **Define ownership:** Tentukan pemilik proyek secara jelas (*project owners*) dan libatkan campuran manajer IT serta pengendali keuangan.
   * **Set permissions:** Gunakan kebijakan (*policies*) untuk mengontrol hak akses secara tepat mengenai siapa saja yang dapat melihat biaya dan menghabiskan anggaran.
   * **Use budgets:** Buat anggaran dengan peringatan otomatis (*automated alerts*) untuk memantau batas pengeluaran.

2. **Pahami Perbedaan Invoice vs. Cost Management Tools**
   * **Invoice:** Dokumen tagihan statis yang menunjukkan jumlah total pembayaran atas layanan yang telah digunakan.
   * **Cost Management Tools:** Perangkat lunak analitik yang menjelaskan secara rinci *mengapa* suatu pengeluaran terjadi hingga tingkat sumber daya (*resource level*) dan memberikan rekomendasi optimasi.

3. **Gunakan Google Cloud Cost Management Tools**
   * **Gain visibility:** Lacak sumber daya apa saja yang digunakan, siapa yang menggunakannya, dan berapa biayanya.
   * **Establish a rhythm:** Tentukan penanggung jawab pemantauan biaya dan lakukan peninjauan laporan secara rutin.
   * **Forecast:** Gunakan [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator) untuk memodelkan dampak perubahan arsitektur atau penggunaan terhadap anggaran masa depan.

---

[↑ Back to Daftar Isi](#daftar-isi)

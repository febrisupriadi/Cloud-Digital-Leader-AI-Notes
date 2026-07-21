# Modul 6: Scaling with Google Cloud Operations

## Daftar Isi
- [1. Scaling with Google Cloud Operations](#1-scaling-with-google-cloud-operations)
- [2. Fundamentals of Cloud Cost Management](#2-fundamentals-of-cloud-cost-management)
- [3. Controlling Access & Resource Hierarchy](#3-controlling-access--resource-hierarchy)

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

---
[↑ Back to Daftar Isi](#daftar-isi)

2. **Pahami Perbedaan Invoice vs. Cost Management Tools**
   * **Invoice:** Dokumen tagihan statis yang menunjukkan jumlah total pembayaran atas layanan yang telah digunakan.
   * **Cost Management Tools:** Perangkat lunak analitik yang menjelaskan secara rinci *mengapa* suatu pengeluaran terjadi hingga tingkat sumber daya (*resource level*) dan memberikan rekomendasi optimasi.

3. **Gunakan Google Cloud Cost Management Tools**
   * **Gain visibility:** Lacak sumber daya apa saja yang digunakan, siapa yang menggunakannya, dan berapa biayanya.
   * **Establish a rhythm:** Tentukan penanggung jawab pemantauan biaya dan lakukan peninjauan laporan secara rutin.
   * **Forecast:** Gunakan [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator) untuk memodelkan dampak perubahan arsitektur atau penggunaan terhadap anggaran masa depan.

---
[↑ Back to Daftar Isi](#daftar-isi)

## 3. Controlling Access & Resource Hierarchy
Dengan beralihnya organisasi ke model *pay-as-you-go*, pembatasan akses fisik (seperti kunci pintu ruang server) tidak lagi relevan. Pengorganisasian aset dan penerapan aturan keamanan memerlukan struktur hierarkis berbasis logika.

### A. Struktur Hierarki Sumber Daya Google Cloud (*Resource Hierarchy*)
Mirip seperti struktur folder pada sistem komputer, Google Cloud menggunakan struktur berbentuk pohon (*tree-like structure*) yang mengelompokkan aset secara logis dari bawah ke atas:
1. **Resources (Sumber Daya):** Level terbawah yang merepresentasikan virtual machines, Cloud Storage buckets, tabel di BigQuery, dan aset individual lainnya.
2. **Projects (Proyek):** Level kedua tempat mengorganisasikan sumber daya (misalnya wadah untuk satu *website* atau aplikasi tertentu).
3. **Folders (Folder):** Level ketiga yang opsional untuk mengelompokkan beberapa proyek atau sub-folder, memudahkan penerapan aturan bersama (misalnya memisahkan lingkungan *testing* dan *production*).
4. **Organization Node (Simpul Organisasi):** Level tertinggi yang merangkum seluruh proyek, folder, dan sumber daya perusahaan.


### B. Manfaat Hierarki Sumber Daya
* **Granular Access Control:** Memungkinkan penugasan peran (*roles*) dan izin pada tingkat spesifik (organisasi, folder, proyek, atau resource).
 * **Inheritance (Pewarisan):** Aturan atau izin yang ditetapkan pada level yang lebih tinggi (seperti Organization atau Folder) akan otomatis diturunkan (*propagate*) ke sumber daya di bawahnya, sehingga pengelolaan menjadi lebih efisien tanpa harus dikonfigurasi satu persatu.
* **Security & Compliance:** Mendukung prinsip hak istimewa terkecil (*principle of least privilege*) untuk meminimalkan risiko keamanan.
* **Visibility & Auditing:** Mempermudah pelacakan perubahan akses di seluruh hierarki guna meningkatkan akuntabilitas dan tinjauan kepatuhan.

### C. Contoh Implementasi Level Hierarki Sumber Daya

Untuk memahami bagaimana struktur ini diterapkan dalam organisasi nyata, berikut adalah contoh perbandingan penempatan aset dari level tertinggi hingga terbawah:

1. **Organization Node (Simpul Organisasi - Level Tertinggi)**
   * **Deskripsi:** Wadah utama yang merepresentasikan seluruh perusahaan (misalnya `pt-telekomunikasi-nusantara.com`).
   * **Contoh Kasus:** Diberikan kebijakan keamanan tingkat perusahaan (Company-wide security policy) yang mewajibkan seluruh data dienkripsi secara *default* dan melarang pembuatan *virtual machines* di wilayah geografis tertentu demi kepatuhan regulasi.

2. **Folders (Folder - Level Ketiga)**
   * **Deskripsi:** Digunakan untuk mengelompokkan departemen, unit bisnis, atau memisahkan lingkungan kerja (*environments*).
   * **Contoh Kasus:** Perusahaan membuat folder terpisah untuk **Production Environment** dan **Testing/Development Environment**. Aturan pembatasan akses (*access control*) diterapkan di folder *Testing* agar tim *developer* memiliki kebebasan penuh di sana, namun akses tersebut dibatasi secara ketat di folder *Production*.

3. **Projects (Proyek - Level Kedua)**
   * **Deskripsi:** Wadah logis tempat layanan dan sumber daya benar-benar diaktifkan dan dikelola.
   * **Contoh Kasus:** Dalam folder *Production*, terdapat proyek terpisah bernama `billing-system-prod` khusus untuk menampung aplikasi penagihan pelanggan, serta proyek `customer-portal-prod` untuk aplikasi web portal pengguna.

4. **Resources (Sumber Daya - Level Terbawah)**
   * **Deskripsi:** Komponen infrastruktur individual yang menjalankan fungsi operasional.
   * **Contoh Kasus:** Di dalam proyek `billing-system-prod`, terdapat aset spesifik seperti:
     * 3 buah *virtual machines* (Compute Engine) untuk server aplikasi.
     * 1 buah *database* terkelola (Cloud SQL) untuk menyimpan data transaksi.
     * Beberapa *Cloud Storage buckets* untuk menyimpan berkas laporan bulanan.

---
[↑ Back to Daftar Isi](#daftar-isi)

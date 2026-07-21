# Modul 6: Scaling with Google Cloud Operations

## Daftar Isi
- [1. Scaling with Google Cloud Operations](#1-scaling-with-google-cloud-operations)
- [2. Fundamentals of Cloud Cost Management](#2-fundamentals-of-cloud-cost-management)
- [3. Controlling Access & Resource Hierarchy](#3-controlling-access--resource-hierarchy)
- [4. Controlling Cloud Consumption](#4-controlling-cloud-consumption)
- [5. Operational Excellence and Reliability at Scale](#5-operational-excellence-and-reliability-at-scale)
- [6. Fundamentals of Cloud Reliability](#6-fundamentals-of-cloud-reliability)

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

## 4. Controlling Cloud Consumption
Setelah hierarki akses terkonfigurasi dengan baik, langkah selanjutnya adalah mengontrol konsumsi *cloud*. Tujuannya adalah merealisasikan penghematan biaya, mencegah pengeluaran berlebih, memaksimalkan sumber daya yang disediakan, serta memastikan kepatuhan terhadap regulasi industri.

### Alat untuk Mengontrol Konsumsi Cloud (*Tools to Control Cloud Consumption*)
Google Cloud menyediakan berbagai perangkat proaktif dan reaktif untuk membantu mengelola konsumsi:

1. **Resource Quota Policies:**
   * Berfungsi untuk menetapkan batasan (*limits*) pada jumlah sumber daya yang dapat dikonsumsi oleh suatu proyek atau pengguna.
   * Mencegah pembengkakan biaya dan memastikan penggunaan tetap berada dalam batas anggaran.

2. **Budget Threshold Rules:**
   * Memungkinkan pembuatan peringatan (*alerts*) otomatis ketika biaya mencapai atau melampaui jumlah tertentu.
   * Bertindak sebagai peringatan dini (*early warning*) sebelum biaya tidak terkendali.

3. **Cloud Billing Reports:**
   * Memberikan cara reaktif untuk melacak pengeluaran yang telah terjadi.
   * Data tagihan dapat diekspor ke BigQuery untuk analisis mendalam atau divisualisasikan menggunakan alat pelaporan.

4. **Dynamic Workload Scheduler:**
   * Mengatur jadwal penggunaan sumber daya untuk durasi tertentu dengan tarif diskon.
   * Sangat ideal untuk beban kerja non-darurat, seperti mematikan lingkungan *testing/development* secara otomatis di luar jam kerja untuk menghemat biaya.

5. **Spot VMs:**
   * Opsi yang sangat hemat biaya untuk beban kerja non-kritis dan tahan terhadap gangguan (*fault-tolerant*).
   * Memanfaatkan kapasitas Compute Engine yang tidak terpakai dengan diskon hingga 91%, dengan risiko dihentikan sementara jika Google membutuhkan kapasitas tersebut (disertai peringatan 30 detik).

6. **Committed Use Discounts (CUDs):**
   * Memberikan harga diskon sebagai imbalan atas komitmen penggunaan tingkat sumber daya minimum untuk jangka waktu tertentu bagi beban kerja yang dapat diprediksi.

---

[↑ Back to Daftar Isi](#daftar-isi)

## 5. Operational Excellence and Reliability at Scale

Setelah berhasil mengendalikan konsumsi dan biaya, langkah krusial berikutnya adalah membangun keunggulan operasional (*operational excellence*) dan reliabilitas (*reliability*) agar sistem tetap tangguh dan siap menghadapi lonjakan beban kerja yang masif.

### Pengertian dan Peran Utama
* **Operational Excellence:** Mengoptimalkan proses operasi agar sistem mampu menangani pertumbuhan skala secara efisien. Memastikan bahwa sistem otomatis mendeteksi lonjakan trafik (*traffic spikes*) dan memprovisi sumber daya baru secara otomatis.
* **Reliability:** Janji atau jaminan bahwa layanan akan terus *online* dan memberikan performa yang solid tanpa gangguan, terlepas dari seberapa besar peningkatan permintaan pengguna.

### Analogi "Sayuran" dalam Lingkungan Cloud
* Dalam strategi *cloud*, keunggulan operasional dan reliabilitas sering diibaratkan sebagai "sayuran" (*vegetables*)—sering kali tidak terlihat atau tidak seglamor fitur aplikasi baru, namun merupakan fondasi esensial yang membuat seluruh sistem tetap sehat, kuat, dan berjalan konsisten di balik layar.

### Menghadapi Lonjakan Trafik Ekstrem (Skala Besar)
* **Contoh Skenario Nyata:** Pada saat *flash sale* besar-besaran, trafik dapat meningkat secara drastis hingga ribuan persen dalam hitungan detik.
* **Peran Operasi & Arsitektur:** 
  * Sistem secara otomatis melakukan *scaling* (menambah atau mengurangi sumber daya) di latar belakang sehingga bisnis dapat memecahkan rekor transaksi tanpa mengalami kegagalan.
  * Jika sebuah *server* mengalami kelebihan beban, sistem secara mulus mengalihkan trafik ke *server* sehat lainnya sehingga pengguna tetap merasakan pengalaman tanpa hambatan (*flawless experience*).

---

[↑ Back to Daftar Isi](#daftar-isi)

## 6. Fundamentals of Cloud Reliability

Dalam lingkungan IT tradisional, sering kali terjadi pemisahan (*dual ownership*) antara tim pengembang (*developers*) dan tim operasional (*operators*):
* **Developers:** Didorong oleh kecepatan (*agility*), fokus menulis dan merilis kode baru dengan cepat untuk meningkatkan nilai bisnis serta pengalaman pengguna.
* **Operators:** Bertindak sebagai penjaga stabilitas (*stability*), cenderung meminimalkan perubahan guna mencegah gangguan pada sistem.

Pemisahan ini dulunya menciptakan hambatan dan silo komunikasi. Untuk menjembatani hal tersebut, diperlukan kerangka kerja budaya dan teknis yang menyatukan tujuan keduanya.

### A. DevOps dan Site Reliability Engineering (SRE)
* **DevOps (Developer Operations):** Pendekatan pengembangan perangkat lunak yang menekankan kolaborasi dan komunikasi antara tim pengembang dan operasional guna meningkatkan efisiensi, kecepatan, serta reliabilitas pengiriman sistem melalui otomatisasi dan peningkatan berkelanjutan.
* **Site Reliability Engineering (SRE):** Konsep di dalam DevOps yang menggabungkan aspek rekayasa perangkat lunak dan operasi untuk merancang, membangun, serta memelihara infrastruktur yang *scalable* dan andal.

### B. The Four Golden Signals (Empat Sinyal Utama)
Pemantauan (*monitoring*) adalah fondasi dari reliabilitas produk. Kinerja sistem diukur menggunakan empat sinyal utama:
1. **Latency:** Mengukur waktu yang dibutuhkan sistem untuk memproses dan mengembalikan hasil suatu permintaan. Sangat penting karena berdampak langsung pada pengalaman pengguna (*user experience*).
2. **Traffic:** Mengukur jumlah permintaan (*requests*) yang mencapai sistem, berfungsi sebagai indikator beban kerja saat ini dan perencanaan kapasitas (*capacity planning*).
3. **Saturation:** Mengukur seberapa dekat sistem dengan batas kapasitas maksimalnya, khususnya pada sumber daya yang paling terbatas.
4. **Errors:** Mengukur tingkat kegagalan atau kesalahan saat sistem menghasilkan respons yang tidak terduga atau salah.

### C. SLI, SLO, dan SLA (Indikator, Tujuan, dan Perjanjian Layanan)
Tiga konsep inti dalam menentukan target reliabilitas berdasarkan *four golden signals*:
* **Service Level Indicators (SLI):** Pengukuran spesifik secara kuantitatif tentang bagaimana performa layanan berjalan secara aktual (misalnya tingkat latensi rata-rata atau tingkat *error rate*).
* **Service Level Objectives (SLO):** Target reliabilitas internal yang ingin dicapai oleh tim untuk menjaga sistem tetap sehat (misalnya menetapkan target ketersediaan layanan sebesar 99.9% dalam sebulan).
* **Service Level Agreements (SLA):** Perjanjian eksternal/kontrak komersial dengan klien enterprise mengenai jaminan performa layanan, di mana pelanggaran terhadap batas ini berkonsekuensi pada penalti finansial atau kompensasi.

---

[↑ Back to Daftar Isi](#daftar-isi)

# Ringkasan Modul 4: Modernize Infrastructure and Applications with Google Cloud

![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)

Catatan ini mencakup fondasi modernisasi infrastruktur dan aplikasi dalam perjalanan transformasi digital.

## Daftar Isi
- [1. Fundamentals of Modernization](#1-fundamentals-of-modernization)
- [2. Modernizing Infrastructure in the Cloud](#2-modernizing-infrastructure-in-the-cloud)
- [3. Modernizing Apps in the Cloud](#3-modernizing-apps-in-the-cloud)
- [4. Course Summary](#4-course-summary)

---

## 1. Fundamentals of Modernization
### Modernize Infrastructure and Applications with Google Cloud
Modernisasi adalah langkah strategis untuk mengubah cara organisasi mengelola dan menjalankan beban kerja agar lebih efisien.

### Unlocking the Value of the Cloud
* **Fundamental Concepts:**
    * **Compute:** Kemampuan memproses informasi (penyimpanan, retrieval, analisis) secara *on-demand*.
    * **Workload:** Aplikasi, layanan, atau kapabilitas (kontainer, database, VM) yang berjalan di *cloud*.
    * **Discovery & Assessment:** Inventarisasi aplikasi dan biaya sebelum migrasi.
* **Why Choose the Cloud?:**
    * **TCO:** Efisiensi biaya dengan menghilangkan infrastruktur fisik.
    * **Scalability:** Penyesuaian sumber daya instan sesuai permintaan.
    * **Reliability:** Uptime tinggi dan ketersediaan global.
    * **Security:** Fitur keamanan canggih (enkripsi, *threat monitoring*).
    * **Flexibility & Managed Services:** Fokus pada *business logic* sementara penyedia mengelola pemeliharaan (database/analytics).
* **Migration Strategies (The 6Rs):**
    * Retire, Retain, Rehost, Replatform, Refactor, dan Reimagine.

[↑ Back to Daftar Isi](#daftar-isi)

---

## 2. Modernizing Infrastructure in the Cloud
### Cloud Corner: Analogi Arsitektur Komputasi
Memilih arsitektur komputasi seperti mendesain ruangan di rumah Anda; setiap beban kerja (*workload*) membutuhkan "ruangan" yang tepat:

*   **Virtual Machines (VM):** Seperti **"kamar suite" pribadi**. Lengkap, mandiri, dan memiliki sumber daya dedikasi penuh. Cocok untuk aplikasi tradisional yang membutuhkan kontrol sistem operasi penuh.
*   **Containers:** Seperti **"meja kerja di kantor bersama"**. Hemat ruang dan ringan karena berbagi *kernel* sistem operasi yang sama, namun setiap aplikasi tetap terisolasi. Sangat efisien untuk arsitektur *microservices*.
*   **Serverless:** Seperti **"alat dapur"**. Anda tidak perlu tahu bagaimana sistem listrik di dinding bekerja, cukup tekan tombol dan gunakan. Sumber daya hanya aktif saat kode dijalankan, sehingga sangat efisien untuk tugas spesifik tanpa perlu mengelola infrastruktur.

### Konsep Infrastruktur Lainnya
- **Virtualization:** Dasar dari *cloud computing* yang memungkinkan efisiensi hardware.
- **Modern cloud computing models:** Transisi dari infrastruktur fisik ke model *cloud-native*.
- **Hybrid and multicloud management:** Pengelolaan data dan beban kerja secara konsisten di lingkungan yang terdistribusi.

- **Virtualization:**
    - *Definisi:* Bentuk optimasi sumber daya yang memungkinkan beberapa sistem (Virtual Machines/VMs) berjalan pada hardware yang sama. Virtualisasi adalah "kunci" yang memecahkan masalah keterikatan aplikasi dengan hardware fisik yang kaku di masa lalu.
    - *Fungsi:* Menggunakan kumpulan sumber daya (CPU, RAM, Storage, Networking) secara bersamaan namun tetap terisolasi.
    - *Compute Engine:* Layanan IaaS (Infrastructure as a Service) Google Cloud untuk membuat dan mengelola VM. Compute Engine adalah implementasi praktisnya di Google Cloud yang memberikan fleksibilitas tanpa harus memikirkan data center fisik.
        - Tidak perlu investasi *upfront* (modal fisik).
        - Dapat dikonfigurasi seperti server fisik (OS, RAM, vCPU).
        - Pengelolaan dapat dilakukan via Console, CLI, atau API (Terraform/Compute Engine API).

### Google Cloud Serverless Computing Products
*   **Cloud Run:**
    *   *Fungsi:* Lingkungan *fully managed* untuk menjalankan aplikasi dalam **container**.
    *   *Kelebihan:* Mendukung bahasa pemrograman apa pun (asalkan bisa dikontainerisasi), *scaling* otomatis hingga ke nol saat tidak ada trafik. Pilihan utama untuk aplikasi web modern.
*   **Cloud Run Functions:**
    *   *Fungsi:* Platform untuk menjalankan *single-purpose functions* berbasis *event*.
    *   *Kelebihan:* Cocok untuk otomatisasi ringan (misal: kirim notifikasi saat ada file baru diunggah). Menggunakan model *event-driven*.
*   **App Engine:**
    *   *Fungsi:* *Platform as a Service* (PaaS) untuk membangun aplikasi web yang sangat *scalable*.
    *   *Kelebihan:* Manajemen *load balancing* dan *traffic splitting* otomatis. Cocok untuk aplikasi yang membutuhkan alur kerja terstruktur (Python, Java, Go).
*   **Poin krusial:** *Cloud Run* saat ini adalah pilihan yang lebih fleksibel karena berbasis container, sedangkan *App Engine* adalah "pemain lama" yang tetap sangat kuat untuk kebutuhan aplikasi web tertentu.

   
### Benefits of Serverless Computing
Beralih ke model *serverless* memberikan dampak strategis bagi organisasi:
* **Reduced Operational Costs:** Tidak perlu mengelola server atau infrastruktur fisik.
* **Scalability:** Penyesuaian kapasitas otomatis sesuai beban kerja.
* **Faster Time-to-Market:** Tim bisa fokus sepenuhnya pada penulisan kode dan inovasi.
* **Reduced Development Costs:** Menghilangkan beban *maintenance* infrastruktur.
* **Improved Resilience:** Mengandalkan *built-in availability* dari penyedia cloud.
* **Pay-per-use Pricing:** Biaya hanya dibebankan saat kode benar-benar dieksekusi (efisien).


## Hybrid and Multicloud Management
Sebagian besar *enterprise computing* di dunia masih berjalan di *on-premises* karena pertimbangan regulasi atau operasional. Migrasi ke *cloud* bukanlah keputusan "semua atau tidak sama sekali" (*all-or-nothing*).

### 1. Model Pengelolaan
*   **Hybrid Cloud:** Kombinasi infrastruktur *on-premises* (private cloud) dan public cloud yang saling terhubung menggunakan konektivitas aman agar sistem dapat berjalan bersamaan.
*   **Multicloud:** Penggunaan beberapa penyedia *public cloud* secara bersamaan untuk fleksibilitas maksimal dan menghindari ketergantungan pada satu vendor (*vendor lock-in*).

### 2. Pendekatan Google Cloud untuk Sistem Terdistribusi
Google Cloud mengelola sistem hibrida dan multicloud tanpa perlu membangun alat manajemen yang rumit dari awal melalui kombinasi:
*   **Google Kubernetes Engine (GKE):** Untuk mengelola *container* di berbagai lingkungan.
*   **Google Distributed Cloud (GDC):** Untuk menjalankan layanan Google Cloud di lingkungan *on-premises* atau *edge*.

### 3. Solusi Manajemen Data Terdistribusi
Untuk menghilangkan *data silos* dan menjaga keamanan data di berbagai lingkungan, Google Cloud menyediakan:
*   **Cloud SQL:** Layanan terkelola untuk MySQL, PostgreSQL, dan SQL Server sebagai jangkar data yang aman.
*   **AlloyDB Omni:** Edisi AlloyDB yang dapat diunduh untuk dijalankan secara lokal di *on-premises*, *edge*, atau *cloud* lain.
*   **BigQuery Omni:** Solusi analisis data multicloud untuk menganalisis data langsung di tempatnya (Google Cloud, AWS, atau Azure) tanpa memindahkan data.
*   **Looker:** Platform *business intelligence* (BI) yang bersifat *cloud-agnostic* untuk menyatukan tampilan data dari berbagai sumber.

[↑ Back to Daftar Isi](#daftar-isi)

---

## 3. Modernizing Apps in the Cloud
Setelah memahami cara memodernisasi infrastruktur, fokus beralih ke apa yang berjalan di atasnya: aplikasi. 

### Perubahan Paradigma Pengembangan Aplikasi
* **Monolithic vs. Microservices:**
    * *Monolithic (Tradisional):* Aplikasi raksasa di mana semua komponen digabung jadi satu. Mengubah satu baris kode dapat memicu risiko besar atau *"update anxiety"*.
    * *Microservices (Modern):* Pemecahan aplikasi menjadi komponen-komponen independen dan lebih kecil sehingga aman diperbarui tanpa menciptakan efek domino.
* **Strategi Aplikasi Legacy:** 
    * Anda tidak harus merombak sistem lama dalam semalam. Menggunakan pendekatan seperti **"lift and shift"** memungkinkan pemindahan beban kerja yang ada ke Google Cloud dengan cepat tanpa perlu menulis ulang kode dari awal untuk mendapatkan manfaat *cloud*.
* **Konektivitas dan Manajemen API:**
    * Aplikasi yang sudah dipindahkan harus dapat saling berkomunikasi secara aman melalui **APIs** (Application Programming Interfaces).
    * **Apigee API Management:** Platform untuk mengelola, mengamankan, dan menskalakan API secara terpusat.


### Modern Architectures and Migration Paths
* **Definisi Aplikasi:** Program komputer atau perangkat lunak yang membantu pengguna menyelesaikan tugas. Tradisional vs. Modern:
    * *Pengembangan Tradisional (On-Premises):* Membutuhkan waktu lama (bisa 6 bulan atau lebih) untuk pembaruan, menciptakan gesekan organisasi.
    * *Pendekatan Cloud:* Membuat organisasi lebih lincah (*agile*) dan responsif.
* **Benefits of Modern App Development (Cloud Corner):**
    * *Microservices (Seperti Blok Lego):* Memecah aplikasi monolitik menjadi bagian-bagian independen agar bisa di-scale secara terpisah tanpa merusak seluruh sistem.
    * *Managed Services:* Penyedia cloud mengurus perawatan rutin (patching, upgrade, monitoring), sehingga developer bisa fokus pada inovasi.
    * *Load Balancing:* Berfungsi sebagai "polisi lalu lintas" yang mendistribusikan trafik secara merata ke beberapa server dan menyediakan *automatic failover* saat ada gangguan.
    * *Pay-per-use Pricing:* Menghentikan pemborosan biaya untuk sumber daya yang sedang menganggur (*idle*).
* **Rehosting (Lift and Shift):**
    * Strategi memindahkan aplikasi *legacy* khusus dari *on-premises* ke *cloud* **tanpa mengubah kodenya sama sekali**, sebagai solusi cepat ketika pembangunan ulang dari awal (*rebuilding*) belum memungkinkan.
 

### Pathways for Legacy Application Migration
Google Cloud menyediakan dua solusi utama untuk rehosting aplikasi *legacy* khusus tanpa harus menulis ulang kode:
* **Google Cloud VMware Engine:** 
  * Memungkinkan migrasi *workload* VMware yang sudah ada ke *cloud* tanpa merancang ulang aplikasi atau mengubah operasional.
  * Mendukung lingkungan VMware yang mapan sekaligus memberikan skalabilitas, keamanan, dan keandalan Google Cloud, serta akses ke layanan native seperti BigQuery, AI/ML, dan GKE.
* **Bare Metal Solution:**
  * Dirancang untuk aplikasi *legacy* (seperti database Oracle) yang tidak dapat dengan mudah dimigrasikan ke lingkungan virtual.
  * Menyediakan server *bare metal* fisik dengan latensi rendah dan performa tinggi, sehingga kompatibilitas tetap terjaga sementara proses operasional internal tidak berubah.

### Application Programming Interfaces (APIs)
* **Definisi API:** Sekumpulan instruksi yang memungkinkan program perangkat lunak yang berbeda untuk saling berkomunikasi secara terstandar dan dapat diprediksi (dianalogikan seperti pelayan restoran yang menghubungkan pelanggan dengan dapur).
* **Manfaat Bisnis API:**
  * Memungkinkan pengembang mengakses fungsionalitas dan data dari program lain tanpa harus menulis ulang kode dari nol.
  * Menciptakan peluang bisnis baru, memperluas pengalaman pengguna, serta memungkinkan monetisasi data (seperti yang dilakukan AccuWeather).
* **Apigee API Management:**
  * Platform Google Cloud untuk mengelola, mengamankan, dan menskalakan API secara terpusat.
  * Bertindak sebagai *intelligent gateway* untuk mengamankan data sensitif, mengontrol trafik, menyediakan analitik, serta mengatur tingkat penawaran (*rate limits* dan *pricing tiers* bagi pengembang).

### Manfaat Utama Apigee API Management
* **Security:**
  * Melindungi API menggunakan autentikasi, otorisasi, dan enkripsi data.
  * Mencegah akses tidak sah serta melindungi sistem *backend* dari potensi ancaman.
* **Development Tools:**
  * Menyediakan portal pengembang (*developer portal*) agar para pengembang dapat dengan cepat mendaftar, mempelajari, dan menguji API.
* **Analytics:**
  * Memantau pola penggunaan trafik secara *real-time*.
  * Melacak siapa saja yang mendaftar serta mendeteksi anomali pada aktivitas penggunaan API.
* **Traffic Management:**
  * Mengatur arus lalu lintas data secara cerdas.
  * Melindungi sistem dari lonjakan trafik mendadak (*traffic spikes*) agar tidak mengalami *crash*, serta menetapkan kuota dan batasan akses (*rate limits*).
 

### Contoh Studi Kasus: AccuWeather dan Apigee
* **Tantangan:** 
  * AccuWeather ingin memperluas jangkauan data cuacanya tidak hanya ke mitra korporat besar, tetapi juga ke ribuan **pengembang independen** (*individual developers*) yang membangun aplikasi untuk mobil terhubung, rumah pintar, perangkat sandang (*wearables*), dan gawai lainnya.
  * Mereka membutuhkan cara untuk menyesuaikan penawaran bagi pengembang dengan tingkat kebutuhan yang berbeda-beda serta memonetisasi trafik tersebut.
* **Solusi Menggunakan Apigee:**
  * **Bundonisasi Produk API:** Membagi API ke dalam paket-paket penawaran yang berbeda, masing-masing lengkap dengan batasan kuota (*rate limits*) dan struktur harga (*pricing tiers*) tersendiri.
  * **Portal Pengembang (*Developer Portal*):** Menyediakan portal yang dapat disesuaikan agar pengembang bisa mendaftar dengan cepat, mempelajari, dan menguji API AccuWeather.
  * **Analitik Bawaan (*Built-in Analytics*):** Membantu AccuWeather memantau siapa saja yang mendaftar, mengukur volume trafik yang dihasilkan, melacak asal trafik, serta mendeteksi pola penggunaan yang tidak biasa (*anomalies*).
 

[↑ Back to Daftar Isi](#daftar-isi)

---

## 4. Course Summary
Berikut adalah rekapitulasi materi utama dari keseluruhan modul modernisasi ini:

### 1. Fundamentals of Modernization
* Mempelajari istilah-istilah penting dalam proses migrasi ke *cloud*.
* Memahami nilai strategis dari peralihan infrastruktur *on-premises* tradisional ke model *compute* berbasis *cloud* yang fleksibel (*elastic*).

### 2. Modernizing Infrastructure in the Cloud
* Memahami konsep dasar dan perbedaan arsitektur **Virtual Machine (VM)** dan **Container**.
* Mengetahui manfaat dari penggunaan **Serverless Computing**.
* Mempelajari strategi pengelolaan data dan *workload* komputasi secara konsisten di lingkungan terdistribusi yang bersifat **Hybrid** dan **Multicloud**.

### 3. Modernizing Applications in the Cloud
* Membandingkan metode pengembangan aplikasi tradisional dengan metode modern berbasis *cloud*.
* Mengeksplorasi pertimbangan dan perangkat untuk melakukan *rehosting* aplikasi *legacy* ke *cloud* (seperti *Google Cloud VMware Engine* dan *Bare Metal Solution*).
* Mendefinisikan peran penting **Application Programming Interfaces (APIs)**.
* Mempelajari manfaat pengelolaan dan pengamanan API secara terpusat menggunakan **Apigee API Management**.

[↑ Back to Daftar Isi](#daftar-isi)

---

## Referensi
- [CDL Study Guide - C4 - Modernize Infrastructure and Applications with Google Cloud
](https://services.google.com/fh/files/misc/cdl_study_guide_c4_modernize_infrastructure_and_applications_with_google_cloud_english.pdf)

---
*Langkah berikutnya dalam jalur pembelajaran Cloud Digital Leader:* **Trust and Security with Google Cloud**.

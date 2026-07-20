# Modul 5: Trust and Security with Google Cloud

## Daftar Isi
- [1. Key Security Terms and Concepts](#1-key-security-terms-and-concepts)
- [2. Cloud Security Components and CIA Triad](#2-cloud-security-components-and-cia-triad)

---

## 1. Key Security Terms and Concepts
Peralihan ke *cloud* membawa fleksibilitas besar, tetapi juga mengubah cara organisasi melindungi aset digital. Strategi keamanan yang kokoh sangat krusial untuk menghadapi ancaman siber yang dinamis.

### Model Akses Pengguna (User Access Governance)
* **Privileged Access:** Memberikan hak akses khusus kepada pengguna tertentu (seperti administrator sistem) untuk menangani tugas pengelolaan, pemecahan masalah, atau pemulihan data. Akses ini harus dipantau ketat karena memiliki risiko tinggi jika disalahgunakan.
* **Least Privilege:** Prinsip keamanan yang memberikan akses kepada pengguna **hanya sebatas yang mereka butuhkan** untuk menjalankan tugas pekerjaannya (akses minimum).
* **Zero-Trust Architecture:** Model keamanan yang **tidak mempercayai** pengguna atau perangkat apa pun secara default. Setiap akses harus melalui proses autentikasi dan otorisasi yang ketat secara terus-menerus.

### Pertahanan dan Kesiapan Siber
* **Security by Default:** Integrasi langkah-langkah keamanan ke dalam sistem dan aplikasi sejak tahap awal pengembangan (*by design*).
* **Security Posture:** Status keamanan keseluruhan dari lingkungan *cloud* yang diukur berdasarkan kesiapan menghadapi serangan serta kepatuhan terhadap kerangka kerja (*framework*) yang ditentukan.
* **Cyber Resilience:** Kemampuan organisasi untuk bertahan, merespons insiden secara efektif, dan pulih dengan cepat dari gangguan atau serangan siber.

### Langkah-Langkah Pengamanan Sumber Daya
* **Firewall:** Perangkat jaringan yang bertindak sebagai "satpam" untuk mengatur lalu lintas masuk dan keluar berdasarkan aturan keamanan yang telah ditetapkan.
* **Encryption & Decryption:** Proses mengubah data menjadi format yang tidak dapat dibaca (*encrypted*) menggunakan algoritma, dan mengembalikannya ke bentuk semula menggunakan kunci enkripsi (*decryption key*).
* **Data Loss Prevention (DLP):** Strategi dan perangkat untuk mengidentifikasi, memantau, dan melindungi informasi sensitif (seperti nomor kartu kredit atau data pribadi) agar tidak hilang, disalahgunakan, atau diakses secara tidak sah.

---
[↑ Back to Daftar Isi](#daftar-isi)

---

## 2. Cloud Security Components and CIA Triad
Model keamanan cloud dievaluasi melalui komponen-komponen yang membentuk postur keamanan yang kokoh menggunakan kerangka **CIA Triad**:

* **Confidentiality (Kerahasiaan):** 
  * Menjaga informasi penting tetap aman dan rahasia sehingga hanya pihak berwenang yang dapat mengaksesnya.
  * *Peran Enkripsi:* Menggunakan teknik enkripsi dan pengelolaan kunci untuk mencegah kebocoran data di cloud.
* **Integrity (Integritas):** 
  * Memastikan data tetap akurat, dapat dipercaya, dan tidak diubah atau dirusak selama penyimpanan maupun perpindahan.
  * *Mekanisme:* Menggunakan checksum atau digital signatures untuk memverifikasi keaslian dan mencegah modifikasi tidak sah.
* **Availability (Ketersediaan):** 
  * Memastikan sistem dan layanan cloud selalu dapat diakses oleh pihak yang berwenang saat dibutuhkan.
  * *Mekanisme:* Menerapkan *redundancy*, mekanisme *failover*, dan rencana pemulihan bencana (*disaster recovery*) untuk meminimalkan *downtime*.

### Komponen Operasional: Control & Compliance
Prinsip CIA Triad kadang saling bertolak belakang (misalnya enkripsi ketat dapat menurunkan kecepatan akses). Untuk menyeimbangkannya, diperlukan dua komponen operasional:
* **Control:** Kebijakan dan pengaman teknis (seperti autentikasi ketat dan pembatasan akses) untuk memitigasi risiko keamanan.
* **Compliance:** Kepatuhan terhadap hukum, regulasi, dan standar industri untuk membangun kepercayaan pemangku kepentingan dan meminimalkan risiko hukum.

---

### Knowledge Check: Security Concepts
* **Pertanyaan Kuis:** A security team is setting up a new cloud system. They put strict rules and tools in place to stop outsiders from breaking in. They also make sure that no files can be secretly changed while moving from one place to another. Which two security concepts are they focusing on?
* **Jawaban:** **Control and integrity**

[↑ Back to Daftar Isi](#daftar-isi)

---

---

## 3. Cloud Identity Management (The Three As & IAM)
Di lingkungan *cloud*, keamanan tidak lagi ditentukan oleh perimeter fisik, melainkan dikelola melalui identitas digital. Manajemen akses dikendalikan melalui tiga pilar utama yang disebut **The Three As**:

### 1. Authentication (Autentikasi)
* Berfungsi sebagai gerbang utama untuk memverifikasi siapa identitas pengguna atau sistem yang meminta akses.
* Menggunakan kredensial unik seperti kata sandi (*password*), token fisik, atau data biometrik (sidik jari/pengenalan suara).
* **Two-Step Verification (2SV / MFA):** Menambahkan lapisan keamanan ekstra dengan meminta dua metode verifikasi yang berbeda (misalnya kombinasi kata sandi dan kode verifikasi dari aplikasi seperti Google Authenticator).

### 2. Authorization (Otorisasi)
* Langkah berikutnya setelah identitas pengguna terautentikasi, yang menentukan **apa saja yang boleh dilakukan** oleh pengguna atau sistem tersebut.
* Menggunakan mekanisme kontrol akses berbasis peran (*roles*), tanggung jawab, dan hierarki organisasi untuk memastikan hak akses yang diberikan sudah tepat (*fine-grained control*).

### 3. Auditing / Accounting (Auditing)
* Berfungsi untuk memantau, mencatat, dan melacak aktivitas pengguna di dalam sistem.
* Mengumpulkan log aktivitas dan kejadian sistem untuk mendeteksi anomali, pelanggaran kebijakan, atau investigasi insiden keamanan (dapat dianalogikan seperti kamera pengawas/cctv).

---

### Google Cloud Identity and Access Management (IAM)
* **Pusat Komando Keamanan:** Layanan terpusat di Google Cloud untuk mengontrol siapa yang memiliki akses ke sumber daya dan apa yang dapat mereka lakukan.
* **Fitur Utama IAM:**
  * Membuat dan mengelola akun pengguna.
  * Menetapkan *roles* dan memberikan atau mencabut izin (*permissions*) ke sumber daya.
  * Mengaudit aktivitas pengguna dan memantau posisi keamanan secara menyeluruh.

---

### Knowledge Check: The Three As of Cloud Identity Management
* **Menampilkan kartu identitas untuk memasuki gedung terlaris:** [Authorization] *(Koreksi: Autentikasi / verifikasi identitas, namun dalam konteks kuis perhatikan kategori pencocokan kartu)*.
* **Menetapkan izin berdasarkan peran dan tanggung jawab:** **Authorization**
* **Memantau dan melacak aktivitas pengguna dalam sistem:** **Auditing**
* **Menganalisis log untuk mendeteksi anomali dan pelanggaran keamanan:** **Auditing**
* **Menyajikan kredensial unik seperti kata sandi atau sidik jari:** **Authentication**

[↑ Back to Daftar Isi](#daftar-isi)

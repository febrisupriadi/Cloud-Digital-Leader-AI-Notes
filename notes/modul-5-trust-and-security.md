# Modul 5: Trust and Security with Google Cloud

## Daftar Isi
- [1. Key Security Terms and Concepts](#1-key-security-terms-and-concepts)
- [2. Cloud Security Components and CIA Triad](#2-cloud-security-components-and-cia-triad)
- [3. Cloud Identity Management (The Three As & IAM)](#3-cloud-identity-management-the-three-as-and-iam)
- [4. Google's Trusted Infrastructure ](#4-googles-trusted-infrastructure)

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

## 3. Cloud Identity Management (The Three As and IAM)
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

[↑ Back to Daftar Isi](#daftar-isi)

---

---

## 4. Google's Trusted Infrastructure 

### 1. Data Centers
Google mendesain dan mengoperasikan jaringan pusat data (*data centers*) global secara mandiri sebagai fondasi dari strategi pertahanan berlapis (*defense-in-depth*).

### Keunggulan Infrastruktur Pusat Data Google
* **Purpose-Built Facilities:** Dibangun dari nol dengan standar keandalan, keamanan, dan efisiensi tingkat tinggi (saat ini mengoperasikan lebih dari 30 pusat data di seluruh dunia).
* **Efisiensi Energi (PUE Score):** Mengukur keberhasilan efisiensi menggunakan metrik **Power Usage Effectiveness (PUE)**. Contohnya, pusat data di Hamina, Finlandia, memanfaatkan air laut untuk sistem pendingin yang inovatif.
* **Skalabilitas dan Kustomisasi:** Memungkinkan penambahan server dengan cepat serta memberikan fleksibilitas untuk menghadirkan fitur-fitur eksklusif bagi pengguna.


### Security Built into the Compute Stack
Keamanan tidak hanya dijaga secara fisik, tetapi juga ditanamkan langsung ke dalam *compute stack* melalui perangkat keras dan perangkat lunak khusus:

* **Custom Security Hardware (Titan Chip):** 
  * Menggunakan chip Titan sebagai *hardware root of trust* untuk memverifikasi integritas sistem saat pertama kali dinyalakan (*secure boot*).
  * Mencegah manipulasi tingkat rendah (*low-level tampering*) dan memastikan hanya kode yang sah (*authentic code*) yang dapat berjalan.
* **Security Software:**
  * Menggunakan tumpukan perangkat lunak (*software stack*) khusus dengan kernel yang diperkeras (*hardened kernel*).
  * Komponen yang tidak esensial dipangkas untuk memperkecil celah serangan (*attack surface*), sehingga beban kerja Anda menjadi jauh lebih aman.


### 2. Secure Storage & Encryption
Meskipun pengamanan fisik dan perangkat keras sudah ketat, enkripsi merupakan benteng pertahanan utama untuk melindungi data itu sendiri. 

### Prinsip Dasar Enkripsi
* Menggunakan algoritma khusus untuk mengubah data yang dapat dibaca menjadi format acak (*scrambled*) yang tidak dapat dibaca tanpa kunci yang tepat.
* Berfungsi seperti brankas: bahkan jika seseorang berhasil mengambil perangkat atau hard drive secara fisik, data di dalamnya tetap tidak dapat dipahami tanpa kunci enkripsi.

### Enkripsi Data di Berbagai Status (Data States)
* **Data at Rest (Data saat disimpan):** Data yang tersimpan di perangkat fisik atau server. Google Cloud secara otomatis mengenkripsi semua konten pelanggan saat istirahat tanpa memerlukan konfigurasi tambahan. Pengguna juga dapat mengelola kunci enkripsi sendiri menggunakan **Cloud Key Management Service (Cloud KMS)**.
* **Data in Transit (Data saat dikirim/berpindah):** Data yang sedang bergerak melintasi jaringan. Google menggunakan protokol **Transport Layer Security (TLS)** untuk mengenkripsi dan memvalidasi data secara ketat.

### Standar Global Enkripsi
* **Advanced Encryption Standard (AES):** Standar global yang dipercaya oleh industri dan pemerintahan.
* **AES-256:** Digunakan secara *default* oleh Google Cloud untuk mengenkripsi data at rest sebagai lapisan perlindungan yang kuat dan berlapis.



### 3. Network Protection and Threat Detection
Keamanan di *cloud* tidak berhenti pada manajemen identitas dan *login*. Perlindungan juga harus mencakup infrastruktur jaringan yang mendasari serta jalur data yang dilaluinya untuk bertahan dari serangan eksternal maupun internal.

### Network Security di Google Cloud
1. **Embrace the power of zero-trust networks:** Menerapkan prinsip bahwa tidak ada jaringan atau perangkat yang dipercaya secara otomatis.
2. **Secure your connections to on-premises and multi-cloud environments:** Mengamankan jalur komunikasi dan koneksi antara lingkungan *on-premises*, *multi-cloud*, dan Google Cloud secara aman.
3. **Protect your perimeter:** Melindungi batas luar sistem dengan kontrol lalu lintas yang ketat.
4. **Protect your applications with Google Cloud Armor:** Melindungi layanan dan aplikasi dari ancaman seperti serangan *Distributed Denial of Service* (DDoS) dan serangan web berbahaya.
5. **Automate certificate management:** Mengotomatiskan penerbitan dan pembaruan sertifikat (SSL/TLS) untuk memastikan enkripsi jalur komunikasi tetap aman tanpa kerepotan administratif manual.

### Security Operations (SecOps)
Setelah arsitektur jaringan pengaman terpasang, tantangan berikutnya adalah pemantauan operasional sehari-hari secara berkelanjutan:
* **Vulnerability Management:** Proses rutin untuk mengidentifikasi dan menambal kerentanan celah keamanan pada infrastruktur maupun aplikasi menggunakan **Security Command Center**.
* **Log Management:** Mengumpulkan dan menganalisis log aktivitas di seluruh lingkungan sistem menggunakan layanan seperti **Cloud Logging** untuk mendeteksi anomali sejak dini.
* **Threat Response:** Proses terorganisir untuk merespons, menahan, mengeliminasi, dan memulihkan sistem dari serangan siber secara cepat.

### SecOps Benefits
Berikut adalah beberapa manfaat utama penerapan *Security Operations* (SecOps) dalam organisasi:
1. **Reduced risk of data breaches:** Menurunkan risiko terjadinya kebocoran data sensitif melalui deteksi dini dan pencegahan yang proaktif.
2. **Increased uptime:** Meningkatkan ketersediaan dan keandalan sistem (*uptime*) dengan meminimalkan gangguan atau *downtime* akibat serangan siber.
3. **Improved compliance:** Membantu organisasi memenuhi standar hukum, regulasi, dan kepatuhan industri secara lebih konsisten.
4. **Enhanced employee productivity:** Meningkatkan produktivitas karyawan melalui otomatisasi alur kerja keamanan (*workflow automation*) sehingga waktu yang dihabiskan untuk menangani ancaman manual menjadi lebih sedikit.


## 4. Cybersecurity Threats & Google Threat Intelligence
Di era yang saling terhubung secara global, pola ancaman keamanan telah bergeser dari sekadar pembatas fisik (*local fortress*) menjadi ancaman yang tidak terlihat dan datang dari berbagai arah.

### Jenis-Jenis Ancaman Keamanan Siber Utama
1. **Deceptive Social Engineering:** Upaya manipulasi psikologis melalui serangan seperti *phishing* untuk mengelabui pengguna agar mengunduh lampiran berbahaya atau membocorkan kata sandi.
2. **Physical Damage:** Risiko kerusakan fisik pada perangkat keras, gangguan daya, atau bencana alam (kebakaran, banjir) yang mengancam ketersediaan data.
3. **Malware, Viruses, and Ransomware:** Perangkat lunak berbahaya yang dirusak untuk mengganggu operasi, merusak sistem, atau menyandera file penting sampai tebusan dibayar (*ransomware*).
4. **Vulnerable Third-Party Systems:** Celah keamanan yang tidak disengaja masuk melalui mitra atau vendor pihak ketiga yang terhubung ke sistem utama perusahaan.
5. **Distributed Denial of Service (DDoS) Attacks:** Serangan yang membanjiri layanan online dengan trafik palsu secara masif agar pengguna sah tidak bisa mengakses sistem (*downtime*).
6. **LLM / Generative AI Attacks:** Serangan baru yang menargetkan kecerdasan buatan, di mana yang paling umum adalah *prompt injection* untuk mengabaikan batasan sistem dan mengekstrak data sensitif.
7. **Configuration Mistakes / Misconfiguration:** Kelalaian saat mengatur konfigurasi sumber daya cloud yang sering kali menjadi penyebab utama kebocoran data.


### Google Threat Intelligence
Untuk menghadapi berbagai ancaman tersebut dengan cepat dan akurat, Google Cloud menyediakan platform **Google Threat Intelligence**, yang menggabungkan:
* Keahlian investigasi insiden langsung dari **Mandiant**.
* Pustaka sampel malware global dari **VirusTotal**.
* Perspektif perlindungan miliaran pengguna oleh **Google**.
* Didukung oleh **Gemini** sebagai analis otomatis untuk memproses data dan menyajikan wawasan secara instan dari berbagai sumber data (*frontline intelligence, crowdsourced intelligence, open-source intelligence, curated intelligence, dan Google insights*).

### Data Sources
Untuk mendukung analisis Gemini dalam menyajikan wawasan secara instan, platform ini ditenagai oleh 5 sumber data unik:
1. **Frontline Intelligence:** Wawasan langsung mengenai ancaman (dampak potensial dan rekomendasi tindakan) berdasarkan pengalaman investigasi insiden nyata dari Mandiant (lebih dari 15 tahun pengalaman di garis depan).
2. **Crowdsourced Intelligence:** Pustaka sampel malware global dan data komunitas keamanan siber (seperti kontribusi dari VirusTotal).
3. **Open-Source Intelligence:** Informasi ancaman yang dikumpulkan dari berbagai sumber publik dan terbuka.
4. **Curated Intelligence:** Data yang dikurasi dan disaring secara khusus oleh para ahli keamanan untuk keakuratan tinggi.
5. **Google Insights:** Perspektif dan wawasan unik yang diperoleh Google dari melindungi miliaran pengguna di seluruh ekosistem internet.


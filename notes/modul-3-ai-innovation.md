# Ringkasan Modul 3: Innovating with Google Cloud Artificial Intelligence

![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)

Repository ini berisi catatan komprehensif dari jalur pembelajaran **Cloud Digital Leader** mengenai fondasi Kecerdasan Buatan (AI), Machine Learning (ML), dan persiapan data operasional bisnis.

## Daftar Isi - Modul 3
- 1. Innovating with Google Cloud Artificial Intelligence
- 2. The landscape of artificial intelligence
- 3. Agentic AI
- 4. The business value of AI and ML
- 5. Laying the foundation for successful ML
- 6. Google Cloud’s AI and ML solutions
- 7. Four paths to build ML models
- 8. Google’s AI Hypercomputer
- 9. Considerations when selecting Google Cloud AI/ML solutions
   
- [1. Pendahuluan & Konteks](#1-pendahuluan--konteks)
- [2. Landasan Teori AI/ML (Agnostik)](#2-landasan-teori-aiml-agnostik)
- [3. Ekosistem Google Cloud untuk AI](#3-ekosistem-google-cloud-untuk-ai)
- [4. Integritas Data & Kualitas Model](#4-integritas-data--kualitas-model)
- [5. Studi Kasus: Implementasi Jaringan](#5-studi-kasus-implementasi-jaringan)
- [6. Lampiran & Referensi](#6-lampiran--referensi)

---

## 1. 
## 2. 
## 3.
## 4.
## 5. 
## 6.
## 7. 
## 8. 
## 9. Considerations when selecting Google Cloud AI/ML solutions

Bagian ini membahas kerangka kerja strategis dalam memilih layanan AI/ML di [Google Cloud](https://www.skills.google/paths/9/course_templates/946/documents/631689) agar sesuai dengan kebutuhan bisnis dan kemampuan tim. Pemilihan solusi yang tepat melibatkan keseimbangan antara empat faktor utama: **kecepatan, diferensiasi, keahlian, dan upaya (effort).**

### 1. Empat Pilar Pertimbangan (Trade-offs)
Dalam setiap proyek AI/ML, terdapat variabel yang saling bersaing yang perlu dioptimalkan:

*   **Kecepatan:** Seberapa cepat model harus masuk ke fase produksi? 
    *   *Pre-trained APIs* menawarkan waktu implementasi tercepat.
    *   *Custom training* dari nol memakan waktu paling lama (bisa mencapai 12-36 bulan).
*   **Diferensiasi:** Seberapa unik kebutuhan model Anda? 
    *   Solusi *out-of-the-box* cocok untuk fungsi umum yang cepat dideploy.
    *   *Custom models* melalui [Gemini Enterprise Agent Platform](https://www.skills.google/paths/9/course_templates/946/documents/631689) memberikan kontrol penuh untuk hasil yang lebih spesifik dan kompetitif.
*   **Keahlian:** Menilai ketersediaan talenta (data scientist, ML engineer). Strategi mencakup pemanfaatan sumber daya internal (upskilling), atau kolaborasi dengan konsultan luar.
*   **Upaya (Effort):** Bergantung pada kompleksitas masalah dan ketersediaan data. Semakin besar kontrol yang dibutuhkan, semakin tinggi tingkat upaya dan investasi yang diperlukan.

### 2. Kategori Solusi
Google Cloud mengelompokkan solusinya ke dalam tiga kategori utama berdasarkan level kontrol yang diinginkan:

| Kategori | Layanan | Fokus |
| :--- | :--- | :--- |
| **SaaS** | [Document AI](https://www.skills.google/paths/9/course_templates/946/documents/631689), Agent Search | Dikelola sepenuhnya, hasil instan, tidak butuh keahlian Data Science. |
| **PaaS** | [Gemini Enterprise Agent Platform](https://www.skills.google/paths/9/course_templates/946/documents/631689) | Jalan tengah: akses model fondasi dengan kemampuan *tuning* data internal. |
| **IaaS** | Specialized AI Infrastructure | Kontrol fundamental penuh (Cloud TPU, NVIDIA GPU) untuk membangun model custom dari nol. |

---
*Catatan: Ringkasan ini merupakan bagian dari modul "Innovating with Google Cloud Artificial Intelligence" dalam jalur sertifikasi Cloud Digital Leader.*



---edit!!!
## 1. The Landscape of Artificial Intelligence
Memahami perbedaan mendasar antara berbagai terminologi dalam ekosistem AI.

| Terminologi | Fokus Utama | Contoh Implementasi |
| :--- | :--- | :--- |
| **Artificial Intelligence (AI)** | Sistem luas yang meniru kecerdasan manusia untuk memecahkan masalah. | Sistem pakar atau logika adaptif dasar. |
| **Machine Learning (ML)** | Mempelajari pola dari data historis secara mandiri. | Memprediksi anomali *traffic* harian dari pengolahan log dan data SNMP. |
| **Generative AI** | Menciptakan konten orisinal baru (teks, gambar, kode) dari sebuah perintah tunggal (*prompt*). | Membuat draf email apresiasi tim atau *script* otomatisasi Python. |

## 2. Agentic AI vs Generative AI
Evolusi AI dari sekadar pembuat konten (*creator*) menjadi eksekutor alur kerja otonom (*manager*).

*   **Generative AI (Pencipta):** Proses selesai setelah *output* dihasilkan. Tetap membutuhkan intervensi manusia untuk melakukan eksekusi lanjutan.
*   **Agentic AI (Pelaksana):** Sistem beroperasi secara otonom dengan kapabilitas perencanaan dan eksekusi multi-langkah. 
    *   *Contoh Kasus (Autonomous Network):* Sistem mendeteksi potensi latensi pada jaringan *backbone*, menghitung jalur *reroute* terbaik, mengeksekusi perubahan konfigurasi, dan mengirim ringkasan ke *bot* Telegram—semuanya tanpa intervensi manual.

## 3. The Business Value of AI and ML
Mengubah pendekatan operasional dari metode reaktif menjadi metode proaktif.

*   **Data Analytics / Business Intelligence (BI):** Bersifat *backward-looking*. Berfokus pada agregasi data untuk menjawab "Apa yang sudah terjadi?" (Misal: *Dashboard analytics* performa bulan lalu).
*   **AI / ML:** Bersifat *forward-looking*. Berfokus pada pengenalan pola untuk menjawab "Apa yang akan terjadi?" atau mengambil tindakan pencegahan (Misal: Memprediksi potensi gangguan pada infrastruktur DWDM).

### 4 Pilar Penawaran AI Google Cloud
Untuk memfasilitasi inovasi AI berskala besar, ekosistem *cloud* menyediakan:
1.  **Computing Power:** Akses ke perangkat keras khusus seperti **TPUs** (Tensor Processing Units) untuk *training* model yang cepat.
2.  **Data Management:** Integrasi pengelolaan data tanpa gesekan melalui **BigQuery** dan Looker.
3.  **Model Access:** Platform terpadu untuk membangun dan men-*deploy* model (termasuk Gemini).
4.  **Pre-built AI Agents:** Solusi aplikasi AI siap pakai yang mempercepat implementasi bisnis tanpa harus membangun dari nol.

## 4. Laying the Foundation for Successful ML
Model AI yang handal (*reliable*) sangat bergantung pada integritas data operasional dan kepatuhan terhadap standar etika.

### 6 Dimensi Kualitas Data (Berdasarkan DAMA & ISO 8000)
Data set harus dievaluasi melalui enam filter berikut:
1.  **Completeness:** Seluruh informasi dan kolom yang dibutuhkan terisi penuh (tidak ada *missing values*).
2.  **Uniqueness:** Tidak ada duplikasi data entitas yang terekam ganda di dalam sistem.
3.  **Timeliness:** Data mutakhir dan relevan dengan jendela waktu analisis saat ini.
4.  **Validity:** Data sesuai dengan struktur, format, dan aturan logika yang berlaku.
5.  **Accuracy:** Data mencerminkan realitas dan fakta lapangan secara presisi.
6.  **Consistency:** Format dan metrik data selaras melintasi berbagai *database* lintas departemen.

### Membangun Kepercayaan (Trust) pada AI
*   **Explainable AI:** Upaya membuka model *black box* agar logika pengambilan keputusan algoritma bisa dijelaskan, dipahami, dan divalidasi oleh manusia. Sangat krusial saat AI mengambil tindakan otomatis di lapangan.
*   **Responsible AI:** Memastikan sistem AI dibangun berdasarkan prinsip keadilan, bebas dari bias, dan aman untuk penggunaan etis berskala *enterprise*.

---
*Catatan ini merupakan fondasi konseptual sebelum memasuki implementasi solusi spesifik pada Google Cloud.*


## 5. Studi Kasus: Implementasi Jaringan
*Catatan: Kerangka kerja ini dirancang untuk mengintegrasikan prinsip-prinsip AI ke dalam alur kerja operasional jaringan.*

### 5.1. Otomatisasi Monitoring (The Foundation)
*   **Integrasi Data:** Membangun *pipeline* otomatisasi menggunakan Python untuk *polling* SNMP secara *real-time*.
*   **Analytics Dashboard:** Mengembangkan visualisasi data untuk mendeteksi pola anomali harian secara otomatis, memangkas *Mean Time to Detect* (MTTD) dibandingkan metode manual.

### 5.2. Mitigasi Gangguan Backbone (The Execution)
*   **Cross-Functional Coordination:** Menginisiasi *single source of truth* untuk menyelaraskan perspektif tim *Field Operations* dan *Network Planning*.
*   **Otonomi Proyek:** Memanfaatkan *agentic mindset* untuk mengawal stabilitas jaringan, khususnya pada infrastruktur DWDM se-Kalimantan.

### 5.3. Otomatisasi Pelaporan Lintas Unit via Bot Telegram (Deployed Project)
*   **Cross-Functional Automation:** Membantu unit Catudaya (Power Supply) dengan mengotomatisasi rekapitulasi laporan harian operasional di seluruh area.
*   **Efisiensi Operasional:** Mengembangkan [bot Telegram untuk laporan BBM dan genset](./scripts/bot-bbm_genset_v2.5/) yang memproses dan melaporkan data konsumsi secara otomatis, menggantikan pengumpulan data manual dan mempercepat pelaporan ke manajemen.

## 6. Lampiran & Referensi
*   *Catatan ini merupakan rangkuman pembelajaran mandiri dan pengalaman praktis.*

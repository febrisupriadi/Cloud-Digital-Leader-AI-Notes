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

# Laporan Praktikum Kriptografi
Minggu ke-: 7
Topik: Diffie-Hellman Key Exchange  
Nama: Putri Tripangesti  
NIM: 230320558 
Kelas: 5DSRA  

---

## 1. Tujuan
1. Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).

---

## 2. Dasar Teori
Diffie–Hellman Key Exchange adalah sebuah protokol kriptografi yang memungkinkan dua pihak bertukar kunci rahasia melalui jaringan publik tanpa harus pernah saling mengirimkan kunci itu secara langsung. Protokol ini bekerja dengan memanfaatkan sifat matematika operasi eksponensial pada bilangan prima dan logaritma diskret, sehingga pihak ketiga yang menyadap komunikasi tidak dapat dengan mudah menghitung kunci rahasia tersebut. Meskipun nilai-nilai seperti bilangan prima umum dan base (generator) dikirim secara terbuka, hasil perhitungan eksponensial yang dilakukan masing-masing pihak tetap terlindungi karena sulitnya menghitung logaritma diskret.

Prosesnya dimulai ketika kedua pihak menyepakati dua nilai publik: bilangan prima besar p dan generator g. Masing-masing pihak kemudian memilih kunci privat secara acak, lalu menghitung kunci publiknya dengan rumus g^a mod p atau g^b mod p. Kedua kunci publik ini kemudian ditukar secara terbuka. Setelah itu, masing-masing pihak menghitung kunci rahasia bersama dengan mengangkat kunci publik lawannya menggunakan kunci privat miliknya, menghasilkan nilai yang sama, yaitu g^ab mod p. Nilai inilah yang akan menjadi kunci enkripsi untuk komunikasi selanjutnya.

Keunggulan utama Diffie–Hellman adalah kemampuannya membangun kunci rahasia tanpa memerlukan pengiriman kunci secara langsung, sehingga mengurangi risiko penyadapan. Namun, protokol ini rentan terhadap serangan man-in-the-middle jika tidak disertai autentikasi, karena penyerang dapat menyamar sebagai salah satu pihak dalam proses pertukaran. Oleh sebab itu, Diffie–Hellman umumnya digunakan bersama mekanisme autentikasi tambahan seperti sertifikat digital untuk memastikan keamanan keseluruhan komunikasi.

---

## 3. Alat dan Bahan
- Visual Studio Code  
- Git dan akun GitHub  

---

## 4. Langkah Percobaan
1. Membuat file `diffie_hellman.py` di folder `praktikum/week7-diffie_hellman/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python diffie_hellman.py`.

---

## 5. Source Code
import random

# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p - 1)  # secret Alice
b = random.randint(1, p - 1)  # secret Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# menghitung kunci bersama
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B)

---

## 6. Hasil dan Pembahasan
Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)

Hasil percobaan Diffie–Hellman Key Exchange yang saya jalankan sudah sesuai ekspektasi. Dalam algoritma ini, tujuan utama adalah memastikan kedua pihak—dalam hal ini Alice dan Bob—dapat menghasilkan kunci rahasia yang sama meskipun mereka menghitungnya secara terpisah menggunakan kunci privat masing-masing. Ketika program menampilkan nilai kunci bersama yang identik, misalnya keduanya menghasilkan angka 16, itu menunjukkan bahwa proses pertukaran kunci berhasil dan prinsip matematika Diffie–Hellman berjalan sebagaimana mestinya. Nilai kunci dapat berbeda setiap percobaan karena penggunaan angka acak, tetapi kesamaan antara kunci Alice dan Bob adalah indikator bahwa algoritma bekerja dengan benar.

---

## 7. Jawaban Pertanyaan
1. Mengapa Diffie-Hellman memungkinkan pertukaran kunci di saluran publik?
    Diffie–Hellman memungkinkan pertukaran kunci melalui saluran publik karena protokol ini tidak pernah mengirimkan kunci rahasia secara langsung. Kedua pihak hanya bertukar nilai publik yang berasal dari operasi eksponensial modulo bilangan prima, sehingga pihak ketiga yang menyadap komunikasi tidak dapat dengan mudah menghitung kunci privat akibat sulitnya masalah logaritma diskret. Dengan memanfaatkan sifat matematika tersebut, kedua pihak dapat menghasilkan kunci rahasia yang sama tanpa harus membagikannya secara eksplisit.

2. Apa kelemahan utama protokol Diffie-Hellman murni?
    Kelemahan utama dari protokol Diffie–Hellman murni adalah tidak adanya mekanisme autentikasi. Karena nilai publik yang dipertukarkan tidak memiliki identitas pengirim yang terverifikasi, penyerang dapat menyusup di tengah komunikasi dan melakukan serangan man-in-the-middle (MITM), yaitu dengan menggantikan kunci publik kedua pihak sehingga mereka sebenarnya berkomunikasi dengan penyerang, bukan satu sama lain. Hal ini menyebabkan Diffie–Hellman murni tidak cukup aman jika digunakan tanpa langkah tambahan.

3. Bagaimana cara mencegah serangan MITM pada protokol ini?
    Cara paling efektif untuk mencegah serangan MITM pada Diffie–Hellman adalah dengan menambahkan proses autentikasi terhadap pihak-pihak yang bertukar kunci. Autentikasi dapat dilakukan menggunakan sertifikat digital, tanda tangan digital, atau protokol seperti TLS yang memverifikasi identitas melalui public key infrastructure (PKI). Dengan adanya autentikasi, kunci publik yang diterima dapat dipastikan berasal dari pihak yang benar, sehingga penyerang tidak dapat lagi menyisipkan kunci palsu atau memanipulasi proses pertukaran.

---

## 8. Kesimpulan
Berdasarkan percobaan dapat disimpulkan bahwa algoritma Diffie–Hellman berhasil menghasilkan kunci rahasia yang sama pada kedua pihak meskipun masing-masing menghitungnya secara terpisah. Hal ini membuktikan bahwa pertukaran nilai publik sudah cukup untuk membangun kunci bersama tanpa perlu mengirimkan kunci privat. Selain itu, hasil yang selalu identik pada kedua pihak menunjukkan bahwa mekanisme matematika Diffie–Hellman bekerja sesuai konsepnya.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
commit week7-diffie-hellman
Author: Putri Tripangesti <putritpgst@gmail.com>
Date:   2025-11-17

    week7-diffie-hellman: implementasi Diffie Hellman dan laporan 

```

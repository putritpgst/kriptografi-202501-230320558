# Laporan Praktikum Kriptografi
Minggu ke-: 2
Topik: week2-cryptosystem  
Nama: Putri Tripangesti 
NIM: 230320558  
Kelas: 5DSRA

---

## 1. Tujuan
1. Mengidentifikasi komponen dasar kriptosistem (plaintext, ciphertext, kunci, algoritma).  
2. Menggambarkan proses enkripsi dan dekripsi sederhana.  
3. Mengklasifikasikan jenis kriptosistem (simetris dan asimetris). 

---

## 2. Dasar Teori
Cipher klasik adalah metode penyandian pesan yang digunakan sebelum berkembangnya kriptografi modern berbasis komputer. Prinsip utamanya adalah mengubah susunan huruf dalam teks asli (plaintext) menjadi teks sandi (ciphertext) dengan aturan tertentu agar maknanya tersembunyi dari pihak yang tidak berwenang. Beberapa contoh cipher klasik yang terkenal antara lain Caesar Cipher, Vigenère Cipher, dan Transposition Cipher. Meskipun sederhana, metode ini menjadi dasar penting dalam memahami konsep keamanan data karena memperkenalkan ide substitusi (penggantian karakter) dan transposisi (penyusunan ulang karakter).

Konsep modular aritmetika berperan penting dalam sistem cipher klasik, terutama pada jenis substitusi seperti Caesar Cipher. Dalam aritmetika modular, operasi dilakukan dengan sisa hasil pembagian terhadap suatu bilangan tertentu yang disebut modulus. Misalnya, jika menggunakan alfabet dengan 26 huruf, maka perhitungan dilakukan dengan modulus 26, sehingga setelah huruf “Z” operasi kembali ke huruf “A”. Prinsip ini memungkinkan proses enkripsi dan dekripsi berjalan secara teratur dan konsisten, serta menjadi fondasi bagi berbagai algoritma kriptografi modern yang lebih kompleks.

---

## 3. Alat dan Bahan
- Visual Studio Code 
- Git dan akun GitHub  

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

# Input dari pengguna
msg = input("Masukkan teks yang ingin dienkripsi: ")
key = int(input("Masukkan kunci (angka): "))

# Enkripsi
enc = caesar_encrypt(msg, key)
# Dekripsi
dec = caesar_decrypt(enc, key)

# Output
print("\n=== HASIL ===")
print("Plaintext  :", msg)
print("Ciphertext :", enc)
print("Decrypted  :", dec)

---

## 6. Hasil dan Pembahasan
Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
![Hasil Diagram](screenshots/cyp.png)

Penjelasan Hasil: 
Plaintext: Cryptosystem Test
Kunci: 3
Ciphertext: Hwduytxdxyjr Yjxy
            → Setiap huruf digeser 5 posisi ke kanan dalam alfabet (contoh: C→H, R→W, Y→D, P→U).
Decrypted: Cryptosystem Test
            → Teks berhasil dikembalikan ke bentuk semula dengan kunci yang sama.
Artinya: Proses enkripsi dan dekripsi bekerja sesuai teori Caesar Cipher, hasilnya sesuai ekspektasi.

---

## 7. Jawaban Pertanyaan
1. Sebutkan komponen utama dalam sebuah kriptosistem.  
    Sebuah kriptosistem (cryptosystem) umumnya terdiri dari lima komponen utama:

    1. Plaintext (Teks asli) — Pesan atau data asli yang ingin dikirim secara rahasia.
    2. Ciphertext (Teks sandi) — Hasil dari proses enkripsi yang sudah tidak dapat dibaca secara langsung.
    3. Encryption Algorithm (Algoritma enkripsi) — Proses atau fungsi matematika yang mengubah plaintext menjadi   ciphertext menggunakan kunci tertentu.
    4. Decryption Algorithm (Algoritma dekripsi) — Proses kebalikan dari enkripsi, yang mengubah ciphertext kembali menjadi plaintext.
    5. Key (Kunci) — Nilai rahasia yang digunakan dalam proses enkripsi dan dekripsi. Tanpa kunci yang benar, pesan tidak dapat dibuka.

2. Apa kelebihan dan kelemahan sistem simetris dibandingkan asimetris?  
    - Kelebihan Sistem Simetris: Proses enkripsi dan dekripsi lebih cepat, lebih efisien untuk data dalam jumlah besar.
    - Kelebihan Sistem Asimetris: Tidak perlu berbagi kunci rahasia secara langsung, mendukung tanda tangan digital dan otentikasi.

    - Kelemahan Sistem Simetris: Distribusi kunci sulit, karena pengirim dan penerima harus memiliki kunci yang sama dan menjaganya tetap rahasia, kurang aman jika kunci diketahui pihak lain.
    - Kelemahan Sistem Asimetris: Proses lebih lambat karena operasi matematis yang kompleks, lebih boros sumber daya untuk data besar.

3. Mengapa distribusi kunci menjadi masalah utama dalam kriptografi simetris?
    Dalam kriptografi simetris, pengirim dan penerima menggunakan kunci yang sama untuk mengenkripsi dan mendekripsi pesan.
    Masalah muncul karena: Kunci harus dibagikan terlebih dahulu sebelum komunikasi dimulai. Jika kunci dikirim melalui saluran komunikasi yang tidak aman, pihak ketiga bisa mencegatnya dan membaca seluruh pesan. Semakin banyak pengguna yang terlibat, semakin banyak pasangan kunci yang harus dijaga dan didistribusikan, sehingga manajemennya menjadi rumit.
---

## 8. Kesimpulan
Program Caesar Cipher berhasil mengenkripsi dan mendekripsi teks dengan benar menggunakan pergeseran huruf sebanyak 5. Hasil dekripsi identik dengan plaintext awal, sehingga dapat disimpulkan bahwa implementasi algoritma Caesar Cipher ini berfungsi sesuai teori dan ekspektasi.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit week2-cryptosystem
Author: Putri Tripangesti <putritpgst@gmail.com>
Date:   2025-10-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```

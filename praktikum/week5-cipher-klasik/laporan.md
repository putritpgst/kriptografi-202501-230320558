# Laporan Praktikum Kriptografi
Minggu ke-: 5 
Topik: Cipher Klasik (Caesar, Vigenère, Transposisi)
Nama: Putri Tripangesti 
NIM: 230320558 
Kelas: 5DSRA 

---

## 1. Tujuan
- Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks.
- Menerapkan algoritma Vigenère Cipher dengan variasi kunci.
- Mengimplementasikan algoritma transposisi sederhana.
- Menjelaskan kelemahan algoritma kriptografi klasik.

---

## 2. Dasar Teori
Cipher Vigenère merupakan salah satu jenis cipher klasik yang termasuk dalam kelompok substitusi polialfabetik. Teknik ini menggunakan kata kunci (key) untuk menentukan pergeseran huruf pada teks asli (plaintext). Setiap huruf dalam kata kunci menentukan berapa banyak pergeseran alfabet yang dilakukan terhadap huruf pada pesan. Misalnya, jika huruf kunci adalah “B”, maka huruf dalam pesan akan digeser satu kali ke depan. Keunggulan Vigenère Cipher dibandingkan Caesar Cipher adalah tingkat keamanannya yang lebih tinggi karena pola pergeserannya tidak tetap, melainkan berubah-ubah sesuai panjang kata kunci.

Sementara itu, cipher Transposisi bekerja dengan cara menyusun ulang posisi huruf dalam plaintext tanpa mengubah huruf-huruf itu sendiri. Dengan kata lain, metode ini tidak melakukan substitusi karakter, melainkan hanya mengubah urutannya berdasarkan pola tertentu atau kunci yang telah ditetapkan. Contohnya adalah Columnar Transposition Cipher, di mana pesan ditulis dalam bentuk tabel dan kemudian dibaca berdasarkan urutan kolom tertentu.

---

## 3. Alat dan Bahan
- Visual Studio Code
- Git dan akun GitHub

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `cipher_klasik.py` di folder `praktikum/week5-cipher-klasik/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python cipher_klasik.py`.)

---

## 5. Source Code
### Langkah 1 — Implementasi Caesar Cipher

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

# Contoh uji
msg = "CLASSIC CIPHER"
key = 3
enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)


### Langkah 2 — Implementasi Vigenère Cipher
def vigenere_encrypt(plaintext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

# Contoh uji
msg = "KRIPTOGRAFI"
key = "KEY"
enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)


### Langkah 3 — Implementasi Transposisi Sederhana
def transpose_encrypt(plaintext, key=5):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    num_of_cols = int(len(ciphertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_cols
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

# Contoh uji
msg = "TRANSPOSITIONCIPHER"
enc = transpose_encrypt(msg, key=5)
dec = transpose_decrypt(enc, key=5)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)

---

## 6. Hasil dan Pembahasan
Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Output](screenshots/output.png)

Semua hasil yang ditampilkan pada output sudah sesuai dengan ekspektasi dari masing-masing algoritma cipher yang digunakan. Pada Caesar Cipher, ciphertext yang dihasilkan sudah benar karena setiap huruf pada plaintext bergeser tiga langkah sesuai key yang diberikan, dan proses dekripsinya berhasil mengembalikan teks ke bentuk aslinya tanpa perubahan. Pada Vigenère Cipher, pola enkripsi juga berjalan sesuai aturan, yaitu menggunakan pergeseran berdasarkan huruf-huruf pada kunci “KEY” yang berulang, dan hasil dekripsinya kembali menghasilkan plaintext “KRIPTOGRAFI”, menunjukkan bahwa implementasinya tepat. Begitu pula dengan Transposition Cipher, ciphertext yang tampak acak sebenarnya sesuai dengan mekanisme pembacaan huruf per kolom berdasarkan key=5, dan fakta bahwa dekripsi berhasil mengembalikan teks asli secara sempurna membuktikan bahwa algoritma bekerja sebagaimana mestinya. Dengan demikian, seluruh output yang muncul dari program sudah benar dan konsisten dengan perilaku algoritma yang diharapkan.

---

## 7. Jawaban Pertanyaan
1. Apa kelemahan utama algoritma Caesar Cipher dan Vigenère Cipher?
    Kelemahan mendasar dari Caesar Cipher adalah ruang kuncinya yang sangat kecil—hanya 26 kemungkinan pergeseran—sehingga dapat dipecahkan dengan brute force dalam hitungan detik. Pola huruf pada ciphertext pun tetap mengikuti pola frekuensi bahasa aslinya, sehingga mudah diungkap dengan analisis frekuensi. Sementara itu, Vigenère Cipher memang lebih kuat karena menggunakan kunci yang lebih panjang, tetapi tetap memiliki kelemahan yaitu pola berulang pada kunci (jika kuncinya pendek) yang menghasilkan pola berulang pada ciphertext. Kelemahan ini memungkinkan serangan seperti Kasiski examination dan Index of Coincidence untuk menebak panjang kunci dan memecahkan cipher tersebut. Kedua algoritma ini tidak lagi dianggap aman untuk standar modern karena tidak mampu menyembunyikan pola bahasa dengan baik.

2. Mengapa cipher klasik mudah diserang dengan analisis frekuensi?
    Cipher klasik mudah diserang dengan analisis frekuensi karena metode enkripsi mereka tidak mengubah pola statistik dari bahasa asli. Setiap bahasa memiliki karakteristik frekuensi tertentu—misalnya huruf “E” adalah yang paling sering muncul dalam bahasa Inggris. Jika metode enkripsi hanya mengganti atau menggeser huruf tanpa mengubah distribusi frekuensinya, pola ini akan tetap terlihat pada ciphertext. Penyerang dapat mencocokkan frekuensi huruf pada ciphertext dengan frekuensi umum suatu bahasa, lalu menebak huruf-huruf yang mungkin sesuai. Hal inilah yang membuat cipher klasik tidak aman ketika dihadapkan pada analisis statistik.

3. Bandingkan kelebihan dan kelemahan cipher substitusi vs transposisi.
    Cipher substitusi mengganti setiap huruf atau unit teks dengan simbol lain, sehingga menghasilkan ciphertext yang tampak berbeda dari plaintext tetapi masih mempertahankan urutan posisi. Kelebihannya adalah mudah diterapkan dan cepat dilakukan, namun kelemahannya terletak pada pola frekuensi huruf yang tetap terlihat, sehingga rentan terhadap analisis frekuensi. Sebaliknya, cipher transposisi tidak mengubah huruf-hurufnya, tetapi mengubah posisi atau urutannya. Hal ini membuat distribusi frekuensi huruf tetap sama, namun urutan kata dan kalimat menjadi kacau. Kelebihannya adalah cipher ini lebih tahan terhadap serangan yang mengandalkan pencocokan substitusi tunggal, tetapi kelemahannya adalah jika pola transposisi berhasil ditebak atau jika ada cukup ciphertext, penyerang dapat merekonstruksi urutan aslinya. Secara keseluruhan, substitusi lebih mudah dipatahkan dengan analisis frekuensi, sedangkan transposisi lebih rentan jika pola penyusunan ulang dapat ditemukan.

---

## 8. Kesimpulan
Percobaan pada Caesar Cipher, Vigenère Cipher, dan Transposition Cipher berjalan dengan baik, ditunjukkan dengan ciphertext yang berhasil didekripsi kembali menjadi plaintext secara tepat. Setiap algoritma menghasilkan output sesuai teori masing-masing, sehingga dapat disimpulkan bahwa implementasi program sudah benar dan berfungsi sebagaimana yang diharapkan.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
commit week5-cipher-klasik
Author: Putri Tripangesti <putritpgst@gmail.com>
Date:   2025-11-17

    week5-cipher-klasik: implementasi cipher klasik dan laporan
    
```

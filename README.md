# API_METHOD
API METHOD (GET,POST,PUSH & DELETED)

PROJECT API METHOD adalah project untuk mengetest beberapa metode rest API diantaranya GET,POST,PUT dan DELETE.
Metode ini mirip dengan Create,Read, Update dan Delete(CRUD).
Pengetesan dilakukan dengan 2 cara, yakni dengan library psycopg2 dan sqlalchemy (ORM), penggunaan psycopg2 dilakukan pada file
app_backup.py dan sqlalchemy pada file app.py.

Langkah-langkah pengetesan :
1.Buat koneksi yang terhubung ke database (dalam hal ini postgreSQL)
2.Buat define Flask
3.Buat endpoint awal, sebelum user
4.Masukkan config, untuk psycopg2 dan sqlalchemy (ORM) berbeda, bisa dilihat di masing-masing file
5.Buat fungsi if else di dalam sebuah fungsi user
6.Coba isi satu row data di database sesuai kolom yang dibuat
7.Buka Postman sebagai aplikasi untuk pengetesan
8.Buat Workspace baru, copy url flask yang telah dijalankan (Flask run) pada python
9.Copy URL -> pilih bagian GET untuk request 1, buat request 2 untuk mengetest POST dst.
10.Coba masing-masing method untuk lihat perubahan nya pada database.

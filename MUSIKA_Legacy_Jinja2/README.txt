MUSIKA LEGACY - TUGAS JINJA2

CARA MENJALANKAN (Windows):
1. Ekstrak ZIP.
2. Buka folder MUSIKA_Legacy_Jinja2 di VS Code.
3. Buka Terminal.
4. Jalankan: python -m pip install -r requirements.txt
5. Jalankan: python app.py
6. Buka: http://127.0.0.1:5000

UJI HALAMAN:
/ beranda
/tentang
/produk (menampilkan 6 produk dengan for dan filter)
/produk/1 (detail produk)
/produk/99 (custom 404)
/cek (uji username: abc = tidak valid; musika123 = tersedia; andi = sudah dipakai)
/member (isi username lalu submit untuk redirect ke /user/<username>)

Data produk dan username adalah data contoh. Halaman member bukan login sungguhan.
Jika ingin menerapkan ke project lama, backup project lama terlebih dahulu.

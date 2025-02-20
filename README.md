# Web Scraper DuckDuckGo dengan Selenium dan BeautifulSoup

## Deskripsi
Skrip ini digunakan untuk mencari situs web berdasarkan kata kunci dan jejak (footprint) menggunakan DuckDuckGo sebagai mesin pencari. Dengan menggunakan Selenium dan BeautifulSoup, skrip ini secara otomatis melakukan pencarian dan mengumpulkan hasil dari halaman DuckDuckGo.

## Fitur
- Menggunakan DuckDuckGo untuk melakukan pencarian web tanpa pelacakan pengguna.
- Menggunakan Selenium untuk mengotomatisasi input pencarian dan navigasi antar halaman.
- Menggunakan BeautifulSoup untuk mengekstrak URL dari hasil pencarian.
- Memungkinkan pengguna menentukan jumlah maksimum hasil yang dikumpulkan.
- Mengabaikan elemen pencarian yang tidak relevan.

## Persyaratan
Sebelum menjalankan skrip, pastikan Anda telah menginstal dependensi berikut:

- Python 3.x
- Selenium
- BeautifulSoup4
- Google Chrome
- ChromeDriver yang sesuai dengan versi Chrome Anda

Untuk menginstal dependensi, jalankan perintah berikut:
```sh
pip install selenium beautifulsoup4
```

## Instalasi
1. Clone repositori ini:
   ```sh
   git clone https://github.com/username/repo-name.git
   cd repo-name
   ```
2. Pastikan ChromeDriver sudah tersedia di direktori proyek atau di path sistem.
3. Jalankan skrip menggunakan perintah berikut:
   ```sh
   python scraper.py
   ```

## Penggunaan
Anda dapat menjalankan skrip dengan mengganti kata kunci dan footprint sesuai kebutuhan:

```python
if __name__ == "__main__":
    keyword = "site:.edu"
    footprint = "powered by WordPress"
    hasil = search_sites(keyword, footprint, num_results=500)
    
    print("\nLink yang ditemukan:")
    for idx, url in enumerate(hasil, start=1):
        print(f"{idx}. {url}")
```

## Catatan
- Pastikan menggunakan versi ChromeDriver yang sesuai dengan browser Chrome Anda.
- Jika ingin menjalankan Selenium dalam mode headless, hapus tanda komentar dari opsi `--headless=new` di dalam skrip.
- Skrip ini hanya mengumpulkan hasil pencarian dan tidak mengakses atau menyimpan data situs yang ditemukan.

## Lisensi
Skrip ini dirilis di bawah lisensi MIT. Anda bebas untuk menggunakan dan memodifikasinya sesuai kebutuhan.

## Kontribusi
Jika Anda ingin berkontribusi atau meningkatkan fitur skrip ini, silakan ajukan pull request atau buat issue di repositori ini.

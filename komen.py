from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Daftar URL yang akan diuji
links = [
    "https://www.nrem.iastate.edu/research/STRIPS/files/news/files/have_fun_and_learn_how_to_help_an_iconic_butterfly_at_the_iowa_city_monarch_festival.pdf",
    "https://professionalprograms.umbc.edu/blog/industry-news/power-of-mentorships/",
    "https://aitd.amity.edu/marketing/key-impacts-of-effective-communication/",
    "https://cat.xula.edu/food/3-reasons-to-stop-sharing-documents-via-email/",
    "https://source.washu.edu/news_clip/the-black-man-who-survived-education/",
]

# Konfigurasi Selenium
chrome_options = Options()
# Blokir gambar dan CSS
prefs = {
    "profile.managed_default_content_settings.images": 2,
    "profile.managed_default_content_settings.stylesheets": 2,
    "profile.default_content_setting_values.notifications": 2,
    }
# Argument tambahan untuk optimasi
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--headless=new")  
chrome_options.add_argument("--disable-gpu")  
chrome_options.add_argument("--no-sandbox")  
chrome_options.add_argument("--disable-dev-shm-usage")  
chrome_options.add_argument("--log-level=3")  
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  
chrome_options.add_argument("--disable-extensions")  
chrome_options.add_argument("--disable-infobars")  
chrome_options.add_argument("--disable-features=NetworkService,NetworkServiceInProcess")  
chrome_options.add_argument("--disable-software-rasterizer")  
chrome_options.add_argument("--disable-logging")

service = Service("./chromedriver")  # Ganti dengan path chromedriver yang sesuai
driver = webdriver.Chrome(service=service, options=chrome_options)

def check_comment_form(url):
    try:
        driver.get(url)
        time.sleep(10)  # Tunggu sebentar untuk loading

        # Cek apakah ada textarea atau input untuk komentar
        comment_box = driver.find_elements(By.TAG_NAME, "textarea")

        # Cek apakah ada elemen reCAPTCHA atau CAPTCHA lain
        captcha = driver.find_elements(By.CLASS_NAME, "g-recaptcha") or \
                  driver.find_elements(By.CLASS_NAME, "h-captcha") or \
                  driver.find_elements(By.XPATH, "//img[contains(@src, 'captcha')]")

        if comment_box and not captcha:
            print(f"✅ Kolom komentar TANPA CAPTCHA ditemukan di: {url}")
            return url
        else:
            print(f"❌ CAPTCHA atau tidak ada kolom komentar di: {url}")
            return None

    except Exception as e:
        print(f"⚠️ Gagal mengakses {url}: {e}")
        return None

# Looping untuk mengecek setiap link
valid_links = [url for url in links if check_comment_form(url)]

print("\n🔍 Situs dengan kolom komentar tanpa CAPTCHA:")
for link in valid_links:
    print(link)

# Data komentar
nama = "Iwan Gunawan"
email = "iwangunawanmylove@gmail.com"
komentar = "Terima kasih atas informasi yang bermanfaat! Artikel ini sangat membantu."

print("\n✍️ Mengisi formulir komentar di situs berikut:")

for url in valid_links:
    try:
        driver.get(url)
        time.sleep(5)  # Tunggu agar halaman termuat

        # Isi kolom komentar
        textarea = driver.find_element(By.ID, "comment")
        textarea.send_keys(komentar)

        # Isi kolom Nama
        nama_field = driver.find_element(By.ID, "author")
        nama_field.send_keys(nama)

        # Isi kolom Email
        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys(email)

        # Klik tombol submit
        submit_button = driver.find_element(By.ID, "submit")
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)  # Scroll ke tombol
        time.sleep(1)  # Tunggu sebentar setelah scroll
        submit_button.click()

        print(f"✅ Komentar berhasil dikirim di: {url}")

    except Exception as e:
        print(f"❌ Gagal mengirim komentar di {url}: {e}")

# Tutup browser setelah selesai
driver.quit()

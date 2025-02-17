from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import random

user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1'
]

headers = {
    'User-Agent': random.choice(user_agents)
}

def search_sites(keyword, footprint, num_results=500):
    base_url = "https://www.google.com/search?q="
    query = f"{keyword} {footprint}"

    # Konfigurasi ChromeDriver
    chrome_options = Options()
    chrome_options.add_argument("--lang=id")
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
    chrome_options.add_argument(f"user-agent={headers['User-Agent']}")  # Gunakan User-Agent

    # Sesuaikan path ke ChromeDriver Anda
    driver_service = ChromeService(executable_path='./chromedriver.exe')
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)

    print(f"Mencari situs untuk: {keyword} dengan footprint: {footprint}")
    driver.get(base_url + query)

    # Tunggu hingga kotak pencarian muncul
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'q'))
        )
    except TimeoutException:
        print("Waktu tunggu habis! Tidak bisa memuat halaman Google.")
        driver.quit()
        return []

    links = []

    # Loop untuk mengambil semua halaman
    while True:
        # Parsing halaman saat ini
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Mengambil semua link hasil pencarian
        for a_tag in soup.select('a'):
            href = a_tag.get('href')
            if href and href.startswith('http') and len(links) < num_results:
                links.append(href)

        # Cek apakah jumlah link sudah mencapai num_results
        if len(links) >= num_results:
            break

        # Coba klik tombol "Berikutnya" untuk ke halaman berikutnya
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//a[@id="pnnext"]'))
            )
            next_button.click()
            time.sleep(random.uniform(5, 10))  # Waktu tunda antara 5 hingga 10 detik secara acak
        except (NoSuchElementException, TimeoutException):
            print("Tidak ada halaman selanjutnya.")
            break

    driver.quit()
    return links

if __name__ == "__main__":
    # Contoh penggunaan
    keyword = "site:.edu"
    footprint = "powered by WordPress"
    hasil = search_sites(keyword, footprint, num_results=500)
    
    print("\nLink yang ditemukan:")
    for idx, url in enumerate(hasil, start=1):
        print(f"{idx}. {url}")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time

def search_sites(keyword, footprint, num_results=500):
    base_url = "https://html.duckduckgo.com/html/"
    query = f"{keyword} {footprint}"

    # Konfigurasi ChromeDriver
    chrome_options = Options()
    # chrome_options.add_argument("--headless=new")  
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

    # Sesuaikan path ke ChromeDriver Anda
    driver_service = ChromeService(executable_path='./chromedriver')
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)

    print(f"Mencari situs untuk: {keyword} dengan footprint: {footprint}")
    driver.get(base_url)

    # Cari kotak pencarian dan masukkan query
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

    # Tunggu halaman selesai dimuat
    time.sleep(3)

    links = []

    # Loop untuk mengambil semua halaman
    while True:
        # Parsing halaman saat ini
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Mengambil semua link hasil pencarian
        for h2_tag in soup.find_all('h2', class_='result__title'):
            # Cari elemen <a> di dalam <h2> dan ambil link di dalamnya
            link = h2_tag.find('a', href=True)
            if link:
                href = link['href']
                # Memastikan link dimulai dengan 'http' dan jumlah link tidak melebihi num_results
                if href.startswith('http') and len(links) < num_results:
                    links.append(href)

        # Cek apakah jumlah link sudah mencapai num_results
        # if len(links) >= num_results:
            # break

        # Coba klik tombol "Next" untuk ke halaman berikutnya
        try:
            next_button = driver.find_element(By.XPATH, '//input[@type="submit" and @value="Next"]')
            next_button.click()
            time.sleep(2)  # Tunggu halaman berikutnya selesai dimuat
        except NoSuchElementException:
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

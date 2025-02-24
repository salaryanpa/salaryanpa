from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Daftar URL yang akan diuji
links = [
    "https://www.rmf.harvard.edu/News-and-Blog/Blog-Home-Page/Blog/2014/June/Guidelines-for-Blog-Comments",
    "https://u.osu.edu/zagorsky.1/sample-page/comment-page-27/",
    "https://magazine.utah.edu/rq04/",
    "https://homes.cs.washington.edu/~kechun/_includes/comments.html",
    "https://pioneer.occc.edu/hook-robin-williams-best-movie-ever/",
    "https://www.academia.edu/6836314/_AGCode_is_ON_Smilies_are_ON_",
    "https://blogs.baylor.edu/digitalcollections/2013/10/10/jfk-at-50_white_slides/",
    "https://u.osu.edu/genrxuvoices/2015/01/07/amelia-arria-staying-active-and-engaged-in-classroom-vital-to-success-in-college/comment-page-1/",
    "https://magazine.utah.edu/rq-12/",
    "https://globalization.gc.cuny.edu/add-your-profile/",
    "https://news.mst.edu/2025/02/engineers-week-qa-with-dr-hossein-abedsoltan-assistant-teaching-professor-of-chemical-engineering/",
    "https://www.unmc.edu/healthsecurity/transmission/2025/02/19/the-latest-on-bird-flu-in-humans-chickens-and-more/",
    "https://writing.msu.edu/outreach/outreach-request-form/",
    "https://www.bu.edu/articles/2025/weekender-february-20-to-23/",
    "https://sites.tufts.edu/museumstudents/?p=23977",
    "https://www.unmc.edu/healthsecurity/transmission/2025/02/19/seroprevalence-of-highly-pathogenic-avian-influenza-ah5-virus-infections-among-bovine-veterinary-practitioners-united-states-september-2024/",
    "https://secure-advance.sbuniv.edu/controls/login/sts.ashx?sid=1858&gid=2&returnUrl=https%3A%2F%2Fcoreadus.ru/cuex/odxwwwimagesbyolivarescomfe61pr/",
    "https://mitsloan.mit.edu/shared/ods/documents?DocumentID=4270",
    "https://www.bu.edu/articles/2025/keeping-seeds-alive-if-the-world-ends/",
    "https://biotility.research.ufl.edu/contact/",
    "https://sites.lsa.umich.edu/mqr/2015/08/snapchats-and-secrets/",
    "https://siasic.strathmore.edu/contact/",
    "https://openlab.sps.cuny.edu/teaching-guides/2023/11/30/course-design-and-development-tutorial/",
    "https://dso.college.harvard.edu/pinserver/auth?redirect=http://yanvis.ru/oxf/cmbp/gr6fe14t/",
    "https://engagingcolumbus.owu.edu/panoramas/",
    "https://hydroinformatics.uiowa.edu/pdfs/13_6_environmental_monitor.pdf",
    "https://podcast.sog.unc.edu/2024/06/20/episode-13-nc-criminal-debrief/",
    "https://research.mcdb.ucla.edu/Goldberg/pdf/CohnSymposium.pdf",
    "https://senseable.mit.edu/news/pdfs/20220928_globalconstructionreview.pdf",
    "https://4thwalldramaturgy.byu.edu/what-is-dramaturgy",
    "https://luskin.ucla.edu/ucla-luskin-scholars-ranked-among-most-influential",
    "https://clsbluesky.law.columbia.edu/2025/02/20/how-ceo-taxes-drive-share-pledging/?noamp=mobile",
    "https://luskin.ucla.edu/it-is-only-possible-to-fail-if-we-forget",
    "https://www.diplomacy.edu/blog/the-paris-ai-summit-a-diplomatic-failure-or-a-strategic-success/",
    "https://www.leeward.hawaii.edu/events/nervous-system-regulation-for-everyone/",
    "https://clsbluesky.law.columbia.edu/2025/02/20/morrison-foerster-discusses-fca-risk-to-federal-contractors-of-trumps-dei-certification/?noamp=mobile",
    "https://daniels.du.edu/blog/michelin-star-chef-and-daughter-to-lead-2025-public-good-gala/",
    "https://iee.psu.edu/news/scientists-invent-device-turns-car-and-helicopter-exhaust-energy",
    "https://wp.nyu.edu/fee/weight-loss-cabbage-soup-recipe-how-i-shed-10-pounds-in-7-days-with-this-delicious-soup/",
    "https://blogs.oregonstate.edu/gardenecologylab/2025/02/17/an-update-on-native-plant-studies-from-the-garden-ecology-lab-at-oregon-state-university/",
    "https://blog.washcoll.edu/wordpress/theelm/2025/02/shoremen-lacrosse-opens-season-with-home-win-over-berry-college-ahead-of-more-home-games/",
    "https://observer.case.edu/a-friendly-reminder-about-healthcare/",
    "https://blogs.bcm.edu/2025/02/13/from-the-labs-uncovering-unique-features-of-early-onset-colorectal-cancer-in-racial-and-ethnic-minorities/",
    "https://cipit.strathmore.edu/product/patent-drafting-module-one/",
    "https://www.pseti.psu.edu/2025/02/18/searching-for-terraformed-planets-complementarity-in-exoplanet-technosignature-and-biosignature-searches/",
    "https://epscor.upr.edu/contacts/",
    "https://wp.nyu.edu/ditesa/2025/02/19/foods-that-burn-belly-fat-top-choices-for-a-slimmer-waistline-in-2025/",
    "https://ttr.tusculum.edu/writing-at-tusculum-university/zach-gass/",
    "https://blogs.bcm.edu/2025/02/14/what-are-considered-relationship-red-flags/",
    "https://observer.case.edu/cwru-reacts-to-changes-in-immigration-policy-ice-raids-in-cleveland/",
    "https://www.mdc.edu/main/images/Brickel%20-%20Miami%20Dade%20College%20Tower%20Theater%20to%20host%20MIFFecito_tcm6-90705.pdf",
    "https://professionalprograms.umbc.edu/blog/how-to-interview-with-confidence/",
    "https://clintonschool.uasys.edu/news/clinton-school-of-public-service-info-day-2024-your-path-to-making-real-change/",
    "https://english.iubat.edu/contact/",
    "https://rudnick.ku.edu/leave-reply",
    "https://blogs.uoregon.edu/heartyourself/about/",
    "https://cea.uprrp.edu/contact/",
    "https://www.nrem.iastate.edu/research/STRIPS/files/news/files/have_fun_and_learn_how_to_help_an_iconic_butterfly_at_the_iowa_city_monarch_festival.pdf",
    "https://professionalprograms.umbc.edu/blog/industry-news/power-of-mentorships/",
    "https://aitd.amity.edu/marketing/key-impacts-of-effective-communication/",
    "https://cat.xula.edu/food/3-reasons-to-stop-sharing-documents-via-email/",
    "https://source.washu.edu/news_clip/the-black-man-who-survived-education/",
]


# Konfigurasi Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Menjalankan browser tanpa tampilan GUI
service = Service("/path/to/chromedriver")  # Ganti dengan path chromedriver yang sesuai
driver = webdriver.Chrome(service=service, options=chrome_options)

def check_comment_form(url):
    try:
        driver.get(url)
        time.sleep(3)  # Tunggu sebentar untuk loading

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

# Tutup browser
driver.quit()

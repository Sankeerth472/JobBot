import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_jobs(driver, num_jobs=10):
    print("📦 Inside scrape_jobs")
    jobs = []

    try:
        driver.execute_script("""
            const overlay = document.querySelector('.search-global-typeahead__overlay');
            if (overlay) overlay.style.display = 'none';
        """)
        print("💥 Overlay removed")
    except Exception as e:
        print(f"⚠️ Couldn't remove overlay: {e}")

    time.sleep(2)

    for i in range(num_jobs):
        try:
            job_cards = driver.find_elements(By.CLASS_NAME, "job-card-container")
            if i >= len(job_cards):
                raise IndexError("No more job cards available")
            card = job_cards[i]
            driver.execute_script("arguments[0].scrollIntoView(true);", card)
            ActionChains(driver).move_to_element(card).click().perform()
            WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h1.t-24"))
            )

            time.sleep(1)
            soup = BeautifulSoup(driver.page_source, "html.parser")
            def safe_find(soup, selector):
                el = soup.select_one(selector)
                return el.get_text(strip=True) if el else "N/A"
            job_data = {
                "title": safe_find(soup, "h1.t-24"),
                "company": safe_find(soup, "div.job-details-jobs-unified-top-card__company-name"),
                "location": safe_find(soup, "li.isPIVdmwDPzXeWTPVgoVkQzsJxMxoMMo "),
                "description": safe_find(soup, "div.jobs-box__html-content"),
            }
            print(f"✅ Scraped: {job_data['title']} at {job_data['company']} ({job_data['location']})")
            jobs.append(job_data)
        except Exception as e:
            print(f"⚠️ Error scraping job [{i}]: {e}")
            continue

    return jobs

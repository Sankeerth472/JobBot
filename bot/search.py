from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def search_jobs(driver, query="Data Science Intern", location="United States"):
    print("🔍 Inside search_jobs")
    driver.get("https://www.linkedin.com/jobs")
    wait = WebDriverWait(driver, 15)

    try:
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)

        job_box = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@aria-label='Search by title, skill, or company']")))
        job_box.clear()
        job_box.send_keys(query)
        job_box.send_keys(Keys.RETURN)
        """
        loc_box = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//input[@aria-label='City, state, or zip code']")))
        driver.execute_script("arguments[0].value = '';", loc_box)
        time.sleep(0.5)
        loc_box.send_keys(Keys.CONTROL + "a")
        loc_box.send_keys(Keys.BACKSPACE)
        loc_box.send_keys(location)
        loc_box.send_keys(Keys.DOWN)
        loc_box.send_keys(Keys.RETURN)
  
        search_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@aria-label='Search']")))
        search_button.click()
        """
        print("✅ Search submitted.")
        time.sleep(5)

    except Exception as e:
        print(f"❌ Error during search: {e}")

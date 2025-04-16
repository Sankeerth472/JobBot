from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def handle_easy_apply(driver):
    print("⚡ Inside easy_apply")
    driver.get("https://www.linkedin.com/jobs")
    wait = WebDriverWait(driver, 15)

    try:
        # Enter job title
        job_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Search by title, skill, or company']")))
        job_box.clear()
        time.sleep(3)
        job_box.send_keys("Data Science Intern")
        job_box.send_keys(Keys.RETURN)

        # Apply Easy Apply filter
        easy_apply_filter = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Easy Apply filter.']"))
        )
        easy_apply_filter.click()
        print("✅ Selected Easy Apply filter")
        time.sleep(3)

        # Process job cards
        job_cards = driver.find_elements(By.CLASS_NAME, "job-card-container")
        for card in job_cards:
            try:
                card.click()
                time.sleep(2)

                easy_apply_btn = wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'jobs-apply-button')]"))
                )
                easy_apply_btn.click()
                print("📨 Opened Easy Apply form")

                # Auto-navigate through steps
                while True:
                    try:
                        time.sleep(2)
                        next_btn = WebDriverWait(driver, 3).until(
                            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Continue to next step']"))
                        )
                        next_btn.click()
                        print("➡️ Clicked 'Next' to proceed")
                    except TimeoutException:
                        try:
                            submit_btn = WebDriverWait(driver, 3).until(
                                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Submit application']"))
                            )
                            submit_btn.click()
                            print("✅ Application Submitted")
                            break
                        except TimeoutException:
                            print("⚠️ Neither 'Next' nor 'Submit' found. Possibly incomplete form.")
                            break
            except Exception as e:
                print(f"⚠️ Skipping job due to error: {e}")
                continue

    except Exception as e:
        print(f"❌ Error in Easy Apply flow: {e}")

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def handle_easy_apply(driver):
    print("⚡ Inside easy_apply")
    driver.get("https://www.linkedin.com/jobs")
    wait = WebDriverWait(driver, 15)

    try:
        # Clear previous filters if any
        clear_filters = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Clear all filters']")))
        clear_filters.click()
        print("🧹 Cleared existing filters")
        time.sleep(2)
    except:
        print("ℹ️ No filters to clear")

    try:
        # Select "Easy Apply" filter
        all_filters = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'All filters')]")))
        all_filters.click()
        time.sleep(2)

        easy_apply_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@for='f_AL-2']")))
        easy_apply_checkbox.click()
        print("✅ Selected Easy Apply filter")

        apply_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-control-name='all_filters_apply']")))
        apply_button.click()
        print("🔍 Filtered by Easy Apply")

        time.sleep(3)

        # Click and apply on the first job
        job_cards = driver.find_elements(By.CLASS_NAME, "job-card-container")
        for card in job_cards:
            try:
                card.click()
                time.sleep(2)

                easy_apply_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'jobs-apply-button')]")))
                easy_apply_btn.click()
                print("📨 Opened Easy Apply form")

                # You can extend this logic to fill out questions dynamically using form inputs
                # Example: Auto fill and submit first step only
                submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Submit application']")))
                submit_btn.click()
                print("✅ Application Submitted")
                break
            except Exception as e:
                print(f"⚠️ Skipping job due to error: {e}")
                continue

    except Exception as e:
        print(f"❌ Error in Easy Apply flow: {e}")
import undetected_chromedriver as uc
import pickle
import os
import time

COOKIE_PATH = "cookies.pkl"

def linkedin_login():
    driver = uc.Chrome()
    driver.get("https://www.linkedin.com/")

    if os.path.exists(COOKIE_PATH):
        print("🍪 Loading cookies...")
        cookies = pickle.load(open(COOKIE_PATH, "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://www.linkedin.com/feed/")
        time.sleep(3)

        # verify login success
        if "login" in driver.current_url:
            print("🔐 Cookie login failed, manual login required.")
        else:
            print("✅ Logged in with cookies.")
            return driver

    print("🛂 Please log in manually...")
    driver.get("https://www.linkedin.com/login")
    input("➡️  After logging in, press Enter to continue...")

    # save cookies
    print("💾 Saving cookies...")
    pickle.dump(driver.get_cookies(), open(COOKIE_PATH, "wb"))

    return driver

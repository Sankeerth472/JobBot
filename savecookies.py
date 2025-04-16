# Step 1: Run this once to manually login and save cookies
driver.get("https://www.linkedin.com/login")
input("👉 Log in manually and press ENTER here once you're on the homepage...")

# Save cookies
import pickle
pickle.dump(driver.get_cookies(), open("linkedin_cookies.pkl", "wb"))

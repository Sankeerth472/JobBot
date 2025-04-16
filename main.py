from bot.login import linkedin_login
from bot.search import search_jobs
from bot.scrape import scrape_jobs

print("🚀 Running main.py...")

if __name__ == "__main__":
    driver = linkedin_login()  # removed EMAIL, PASSWORD

    search_jobs(driver)
    jobs = scrape_jobs(driver)

    for i, job in enumerate(jobs, 1):
        print(f"\nJob {i}: {job['title']} at {job['company']} ({job['location']})\n{job['description'][:250]}...\n")

    driver.quit()

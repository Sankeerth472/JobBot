from bot.login import linkedin_login
from bot.search import search_jobs
from bot.scrape import scrape_jobs
from bot.db import create_jobs_table, save_job
from bot.easyApply import handle_easy_apply  

print("🚀 Running main.py...")

if __name__ == "__main__":
    driver = linkedin_login()

    user_input = input("⚙️ Do you want to use Easy Apply mode? (yes/no): ").strip().lower()

    if user_input == "yes":
        handle_easy_apply(driver)
    else:
        create_jobs_table()
        search_jobs(driver)
        jobs = scrape_jobs(driver)

        for i, job in enumerate(jobs, 1):
            print(f"\nJob {i}: {job['title']} at {job['company']} ({job['location']})\n{job['description'][:250]}...\n")
            save_job(job)

    driver.quit()


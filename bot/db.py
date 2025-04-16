import psycopg2
from psycopg2 import sql

# Update these with your own PostgreSQL config
DB_CONFIG = {
    'dbname': 'job_scraper',
    'user': 'postgres',
    'password': 'Saai@472',
    'host': 'localhost',
    'port': 5432
}

def connect():
    return psycopg2.connect(**DB_CONFIG)

def create_jobs_table():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS jobs (
                    id SERIAL PRIMARY KEY,
                    title TEXT,
                    company TEXT,
                    location TEXT,
                    description TEXT
                );
            """)
        conn.commit()

def save_job(job):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO jobs (title, company, location, description)
                VALUES (%s, %s, %s, %s);
            """, (
                job['title'],
                job['company'],
                job['location'],
                job['description']
            ))
        conn.commit()

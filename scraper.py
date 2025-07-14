import requests
import json
import time
import random
from tqdm import tqdm

# ============ CONFIG ============
MAX_PAGES = 150 # Maximum number of pages to fetch
SAVE_PATH = "data/raw/104_swe_jobs.json"

# HTTP request headers to simulate a real browser visit
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0.0.0 Safari/537.36",
    "Referer": "https://www.104.com.tw/",
}

# Optional cookies to bypass basic protection or popup prompts
cookies = {
    "isExpatsConfirmIgnored": "1",
    "test_cookie": "CheckForPermission"
}

BASE_URL = "https://www.104.com.tw/jobs/search/list"

# Create directory
import os
os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)

all_jobs = []

for page in tqdm(range(1, MAX_PAGES + 1), desc="Fetching"):
    params = {
        "ro": "0",  # 0: All job types (full-time, part-time)
        "kwop": "7", # Keyword matching mode
        "jobcat": "2007001015,2007001016,2007001017,2007001004,2007001025", # Specific job category codes for SWE
        "order": "15", # Sorting rule (15 = by relevance or post date)
        "asc": "0", # Descending order
        "page": str(page), # Current page number
        "mode": "s", # Search mode
        "jobsource": "2018indexpoc" # Job source (default value from site)
    }

    try:
        # Send HTTP GET request to fetch one page of job listings
        resp = requests.get(BASE_URL, headers=headers, cookies=cookies, params=params)
        data = resp.json()

         # Extract job list from response
        jobs = data.get('data', {}).get('list', [])
        if not jobs:
            print(f"No data on page {page}, stopping fetch.")
            break

        all_jobs.extend(jobs)

        # Random delay to avoid blocking
        time.sleep(random.uniform(0.8, 1.5))

    except Exception as e:
        print(f"Failed to fetch page {page}: {e}")
        continue

# Save JSON
with open(SAVE_PATH, "w", encoding="utf-8") as f:
    json.dump(all_jobs, f, ensure_ascii=False, indent=2)

print(f"Done. Total {len(all_jobs)} job postings saved to {SAVE_PATH}")
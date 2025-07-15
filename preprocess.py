import json
import pandas as pd
import os
import re

# File paths
RAW_PATH = "data/raw/104_swe_jobs.json"
SAVE_PATH = "data/processed/104_swe_jobs_clean.csv"

# List of technical skills to search for
TECH_KEYWORDS = [
    "Python", "Java", "Javascript", "C#", "C++", "Typescript", "Node.js",
    "React", "Vue", "Angular", ".NET", "Django", "Spring", "SQL", "AWS",
    "Azure", "Git", "HTML", "CSS", "RWD", "Oracle", "MongoDB", "PostgreSQL"
]

# Compile regex patterns to match skills precisely
TECH_REGEX = [
    (re.compile(rf"(?<![a-zA-Z]){re.escape(skill)}(?![a-zA-Z])", re.IGNORECASE), skill)
    for skill in TECH_KEYWORDS
]

# Ensure output directory exists
os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)

# Load raw job data from JSON
with open(RAW_PATH, "r", encoding="utf-8") as f:
    raw_jobs = json.load(f)

# Extract and clean relevant fields
cleaned_jobs = []

for job in raw_jobs:
    description = job.get("description", "")
    tech_found = []
    for pattern, skill in TECH_REGEX:
        if pattern.search(description):
            tech_found.append(skill)

    cleaned_jobs.append({
        "jobName": job.get("jobName", ""),
        "jobAddrNoDesc": job.get("jobAddrNoDesc", ""),
        "custName": job.get("custName", ""),
        "tech_skills": ", ".join(sorted(set(tech_found))),
        "periodDesc": job.get("periodDesc", ""),
        "coIndustryDesc": job.get("coIndustryDesc", ""),
        "optionEdu": job.get("optionEdu", "")
    })

# Save to CSV
df = pd.DataFrame(cleaned_jobs)
df.to_csv(SAVE_PATH, index=False, encoding="utf-8-sig")

print(f"Cleaning complete. {len(df)} job records saved to {SAVE_PATH}")
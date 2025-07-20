import json
import pandas as pd
import os
import re
from translation import location_map, experience_map, edu_map, industry_map

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

    raw_location = job.get("jobAddrNoDesc", "")
    period = job.get("periodDesc", "")
    industry = job.get("coIndustryDesc", "")
    edu = job.get("optionEdu", "")

    # Extract only city/country name (remove district/area)
    known_locations = sorted(location_map.keys(), key=lambda x: -len(x))
    loc_key = next((loc for loc in known_locations if raw_location.startswith(loc)), raw_location)

    cleaned_jobs.append({
        "jobName": job.get("jobName", ""),
        "jobAddrNoDesc": loc_key,
        "jobAddrNoDesc_en": location_map.get(loc_key, loc_key),
        "custName": job.get("custName", ""),
        "tech_skills": ", ".join(sorted(set(tech_found))),
        "periodDesc": period,
        "periodDesc_en": experience_map.get(period, period),
        "coIndustryDesc": industry,
        "coIndustryDesc_en": industry_map.get(industry, industry),
        "optionEdu": edu,
        "optionEdu_en": edu_map.get(edu, edu)
    })

# Save to CSV
df = pd.DataFrame(cleaned_jobs)
df.to_csv(SAVE_PATH, index=False, encoding="utf-8-sig")

print(f"Cleaning complete. {len(df)} job records saved to {SAVE_PATH}")
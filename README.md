![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3776AB?style=for-the-badge&logo=plotly&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C808C?style=for-the-badge&logo=seaborn&logoColor=white)

# Engineer Market Analyzer

This project is a full pipeline data analysis tool for understanding Taiwan's software engineer job market using data scraper from the 104 Job Bank.

## 🧩 Project Structure

```
engineer-market-analyzer/
├── data/
│   ├── raw  
│   │   └── 104_swe_jobs.json        # Original crawled JSON data
│   └── processed
│       └── 104_swe_jobs_clean.csv   # Cleans raw data, extracts tech skills, filters relevant fields
├── scraper.py                       # Extracts software engineer job postings from 104 using API
├── translation.py                   # Converts Mandarin fields to English for analysis
├── preprocess.py                    # Script to clean and extract key fields from raw data
├── analyze.ipynb                    # Jupyter Notebook for visual analysis
├── README.md                        # Project introduction and guide
├── LICENSE
```

## 🕸️ Source

The data comes from real job postings on [104人力銀行 (104 Job Bank)](https://www.104.com.tw/), focused on software engineering roles.

---

## 🧼 Data Cleaning Logic (`preprocess.py`)

* Extracted and retained only relevant fields:

  * `jobName`, `jobAddrNoDesc`, `custName`, `periodDesc`, `coIndustryDesc`, `optionEdu`
* Created a new field `tech_skills` by scanning the `description` field for 25+ common technical keywords (e.g., Python, React, AWS).
* Ensured that "Java" and "Javascript" are distinguished accurately using regular expressions.

Output CSV file: `data/processed/104_swe_jobs_clean.csv`

---

## 📊 Data Analysis (`analyze.ipynb`)

You can view the full analysis notebook here:
👉 [View on nbviewer](https://nbviewer.org/github/bolin0330/engineer-market-analyzer/blob/main/analyze.ipynb)

### Included Visualizations:

* **📍 Job distribution by city** (Pie Chart)
* **🛠️ Top 15 technical skills** (Bar Chart)
* **🕓 Experience requirement** (Histogram)
* **🏭 Industry type distribution** (Treemap + Word Cloud)
* **🎓 Education level requirement** (Pie Chart)
* **🏙️ Top 4 industries in major cities** (Stacked Bar)

---

## 📦 Requirements

```bash
pip install pandas matplotlib seaborn squarify wordcloud
```

---

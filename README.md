# Data-Science-Job-Salaries
Exploratory Data Analysis using dataset of Data Science Job Salaries


# Data Science Job Salaries — EDA

This repository contains a polished Exploratory Data Analysis (EDA) notebook for the **Data Science Job Salaries** dataset.

## Files
- `Data science Job salaries.ipynb` — The Jupyter notebook with full EDA, visuals, and conclusions.
- `Data Science Job Salaries.csv` — Raw dataset (as uploaded by the user).

## Overview
This project inspects job postings and salary information to:
- Clean and standardize salary values.
- Visualize salary distribution and outliers.
- Compare salaries across job titles and experience levels.
- Explore geographic and remote-work trends.
- Provide actionable recommendations.

## How to run
1. Clone or upload files to a GitHub repo.
2. Open the notebook `Dat science Job salaries.ipynb` in Google Colab or Jupyter.
3. Ensure dependencies are installed:
```bash

pip install pandas matplotlib seaborn

pip install -r requirements.txt #for all the libariries in one txt

#To create and activate a Python virtual environment (venv) in your Codespace, use these #commands in your terminal:

python3 -m venv .venv
source .venv/bin/activate 

# to run  your streamlit  file
streamlit run Streamlit_DS_Salaries.py

```
4. Run all cells.

## Notes
- The notebook includes code to coerce salary text to numeric (`_salary_num`). Double-check currency and ranges for your use-case.
- If your dataset has differently named columns, the notebook attempts to detect likely column names automatically. Adjust cell code if necessary.

## Conclusion
See the notebook's **Conclusion & Actionable Insights** section for final recommendations.

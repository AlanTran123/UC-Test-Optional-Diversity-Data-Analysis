# UC Test-Optional Admissions & Racial Diversity Analysis

This project analyzes University of California admissions data from 2016–2024 to evaluate whether the shift to **test-optional (2021)** and **test-blind (2023)** admissions policies was associated with measurable changes in applicant racial diversity.

📘 **Main analysis:**  
[UC Research Project.ipynb](UC%20Research%20Project.ipynb)

---

## Research Question
How did the University of California’s transition from test-required to test-optional and test-blind admissions influence the racial diversity of first-year and transfer applicants?

---

## Data
- Publicly available UC admissions data
- Applicant counts broken down by race/ethnicity and year
- Two applicant populations:
  - First-year applicants
  - Transfer applicants
- Time period: **2016–2024**

---

## Methods
- Data cleaning and wrangling using **Python (pandas, NumPy)**
- Exploratory data analysis and visualization with **matplotlib**
- Diversity quantified using:
  - **Shannon Diversity Index (H')**
  - **Simpson Diversity Index (1 − D)**
- Predefined thresholds used to identify meaningful changes in diversity

---

## Key Findings
- **First-year applicants:**  
  No meaningful change in racial diversity following the implementation of test-optional or test-blind policies.
- **Transfer applicants:**  
  A decline in diversity was observed after 2021, though results are likely influenced by external factors such as the COVID-19 pandemic rather than admissions policy alone.

---

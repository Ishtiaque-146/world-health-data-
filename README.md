# world-health-data-
## Build from sources 
1. Clone the repo
```bash
git clone https://github.com/Ishtiaque-146/world-health-data-.git
```
2. Install and activate virtual environment
```bash
python -m venv venv
.\venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Download Chromedriver from : https://chromedriver.chromium.org/downloads

5. run scrapper
```bash
python Scripts/healthcare.py --chromedrive_path<path_to_chromedriver>
python Scripts/life_expectency.py --chromedrive_path<path_to_chromedriver>
python Scripts/obesity.py --chromedrive_path<path_to_chromedriver>

```
6. You will get files named `best_healthcare_systems_by_country.csv` , `life_expectancy_by_country_2024 .csv` and `obesity_by_country.csv`. Alternatively check the data from  "https://github.com/Ishtiaque-146/world-health-data-/tree/main/selenium_scrapper/Data"

# Tableau public dashboard link: 
https://public.tableau.com/views/Worldwidehealthcaredata/CountryWiseHealthcaredata?:language=en-GB&:sid=&:display_count=n&:origin=viz_share_link

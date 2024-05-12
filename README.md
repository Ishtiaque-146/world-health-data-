# world-health-data-

## Problem Statement:
The Goal of this project is to gather data by scrapping from 3 different dynamic websites in order to do data analysis on the quality of healthcare systems around the world and understand what makes the healthcare systems of top countries better. Also, get a correlation between life expectancy and health care systems of countries around the world.

## The sources for these data are:
1. Health care rankings of countries around the world from, [This website](https://ceoworld.biz/2024/04/02/countries-with-the-best-health-care-systems-2024/)
2. Life Expectancy data from, [This website](https://worldpopulationreview.com/country-rankings/life-expectancy-by-country)
3. World wide Obesity rate data from, [This website](https://data.worldobesity.org/rankings/?age=a&sex=m)

## Please visit public Dashboards to Check out the analysis:

1. For country wise healthcare data visit [This link](https://public.tableau.com/views/Worldwidehealthcaredata/CountryWiseHealthcaredata?:language=en-US&:sid=&:display_count=n&:origin=viz_share_link)
2. For relations between obesity and healthcare system visit [This link](https://public.tableau.com/shared/R79J3K82Y?:display_count=n&:origin=viz_share_link)
3. For relations between life expectancy and health care and life expectancy visit [This link](https://public.tableau.com/shared/C2MY698MZ?:display_count=n&:origin=viz_share_link)

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

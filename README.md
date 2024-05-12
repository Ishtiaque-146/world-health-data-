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

## 1.
![Dashboard 1](https://github.com/Ishtiaque-146/world-health-data-/assets/169515556/9c376001-24f0-4c6d-b35f-af4d8675ff6f)

### This dashboard consists of 4 different graphs:
1. A world map consisting of the Health care index of all the countries.
2. A bar chart showing the rankings of Government Readiness points ranking.
3. Multiple charts that showing Health care system ranks of country wise vs all other attributes
4. A stacked bar chart showing the Country wise healthcare index count.

### Findings from the Dashboard:
1. World map showing the health care index of all the countries. Which can easily be browsed by the users.
2. Japan has the highest Government readiness points. Scoring 98.74 out of 100. Also, Oman has the lowest Government readiness points scoring only 43.32.
3. The Average Government readiness index of the countries around the world is 65.55 out of 100.
4. Multiple charts shows the the correlations between the Rank and Government Readiness, Medical Infrastructures, and  Professionals as well as Medicine availability and cost.
5. Taiwan and South Korea Has the highest health care index (overall). Both scoring 76.02 out of 100. While Nepal, El Salvador and Honduras scoring the lowest Which is 18.1.

# 2.

![Dashboard 2](https://github.com/Ishtiaque-146/world-health-data-/assets/169515556/f23594b1-95e0-4e86-a9ab-28d0d966bbe1)

### This Dashboard consists of 4 different graphs:

1. Obesity level world map
2. A bar chart of Country wise Obesity percentage index.
3. A line chart of the Relation Between Life Expectancy and Obesity percentage
4. Relation between Health care index and Obesity percentage Country wise

### Findings from the Dashboard:
1. A world map that shows the obesity percentage of the countries around the globe.
2. United states of America has the highest Obesity percentage. 41.64% of the entire population are obese.
3. Vietnam has the lowest Obesity rate aorund the globe with only 1.97%.
4. 22.19% is the average obesity rate amongst the countries world wide.
5. There isn't much correlation between Life expectency and Obesity percentage. The country with highest obesity percentage has Life expectancy of 79.89 years. Also the country with lowest obesity rate has life expectancy of 74.90. Both of them having 70+ years of life expectancy.
6. Same goes for Relation between health care index and Obesity percentage.

# 3.![Dashboard 3](https://github.com/Ishtiaque-146/world-health-data-/assets/169515556/17e2fb06-f653-434c-834f-74b9015f7620)

### The Dashboard consists of 4 different graphs and charts:

1. A bar chart that shows Country wise average life expectancy rate.
2. A line chart of Health care index vs average life expactency rate countrywise.
3. Multiple line charts showing the correlation between All health care index and Health care index overall.
4. A world map showing country wise life expectancy.

### Findings from the dashboard:

1. Average Life expectancy world wide is 77.07 years.
2. Hong kong has the highest average Life expectancy rate of the world with 86.0 years. And Nigeria has the lowest average life expectancy rate with 54.1 years.
3. The line graph shows the average life expectancy rate gradually decreases as the Overall health care index decreases.
4. Multiple line graphs that shows different relations between Life Expectancy world wide and Government Readiness, Medical Infrastructures, and  Professionals as well as Medicine availability and cost as well as the overall Index of health care index overall.
5. Coloured world map showing all the country's life expectation.
   

















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

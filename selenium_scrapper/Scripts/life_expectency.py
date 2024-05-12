import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--chromedrive_path", type=str, help="check where your chromedriver.exe is located")
args = parser.parse_args()


def get_life_expectancy_details(row):
    details = row.split(' ')
    contents = {}
    contents["Rank"] = details[0]
    contents["Country"] = ' '.join(details[1:-2])
    contents["Life Expectancy"] = details[-1]
    return contents

def main():
    print("Starting...")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
    url = "https://worldpopulationreview.com/country-rankings/life-expectancy-by-country"
    driver.get(url)
    rows = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tbody')))
    rows = rows.text.split('\n')
    life_expectancy_data = []
    for row in rows:
        life_expectancy_data.append(get_life_expectancy_details(row))
    driver.close()

    df = pd.DataFrame(data=life_expectancy_data, columns=["Rank", "Country", "Life Expectancy"])
    df.to_csv("life_expectancy_by_country.csv", index=False)
    print("Data saved to 'life_expectancy_by_country.csv'")
    return

if __name__ == "__main__":
    main()

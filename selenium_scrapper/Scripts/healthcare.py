import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--chromedrive_path", type=str, help="check where your chromedriver.exe is located")
args = parser.parse_args()


def get_healthcare_details(row):
    details = row.split(' ')
    contents = {}
    contents["Rank"] = details[0]
    contents["Country"] = ' '.join(details[1:-4])
    contents["Medical Infrastructure and Professionals"] = details[-4]
    contents["Medicine Availability and Cost"] = details[-3]
    contents["Government Readiness"] = details[-2]
    contents["Health Care Index (Overall)"] = details[-1]
    return contents

def main():
    print("Starting...")
    driver = webdriver.Chrome(service=Service(executablepath="chromedriver.exe"))
    url = "https://ceoworld.biz/2024/04/02/countries-with-the-best-health-care-systems-2024/"
    driver.get(url)
    rows = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tbody')))
    rows = rows.text.split('\n')
    healthcare_data = []
    for row in rows:
        healthcare_data.append(get_healthcare_details(row))
    driver.close()

    df = pd.DataFrame(data=healthcare_data, columns=["Rank", "Country", "Medical Infrastructure and Professionals", "Medicine Availability and Cost", "Government Readiness", "Health Care Index (Overall)"])
    df.to_csv("best_healthcare_systems_by_country.csv", index=False)
    print("Data saved to 'best_healthcare_systems_by_country.csv'")
    return

if __name__ == "__main__":
    main()


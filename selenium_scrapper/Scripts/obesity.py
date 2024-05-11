import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

def get_obesity_details(row):
    details = row.split(' ')
    contents = {}
    contents["Rank"] = details[0]
    contents["Country"] = ' '.join(details[1:-1])
    contents["Obesity %"] = details[-1]
    return contents

def main():
    print("Starting...")
    driver = webdriver.Chrome(service=Service(executablepath="chromedriver.exe"))
    url = "https://data.worldobesity.org/rankings/?age=a&sex=m"
    driver.get(url)
    rows = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tbody')))
    rows = rows.text.split('\n')
    obesity_data = []
    for row in rows:
        # print(row)
        obesity_data.append(get_obesity_details(row))
    driver.close()

    df = pd.DataFrame(data=obesity_data, columns=["Rank", "Country", "Obesity %"])
    df.to_csv("obesity_by_country.csv", index=False)
    print("Data saved to 'obesity_by_country.csv'")
    return

if __name__ == "__main__":
    main()
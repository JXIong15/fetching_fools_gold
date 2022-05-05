from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# maybe add a env file?
driver.get("http://sdetchallenge.fetchrewards.com/")

def main():
    print(driver.title)
    assert "React" in driver.title
    goldBars = driver.find_elements(By.XPATH, "//div[@class='coins']/button")

    for gb in goldBars:
        print(gb.text)
    # print(goldBars)
    driver.close()

main()

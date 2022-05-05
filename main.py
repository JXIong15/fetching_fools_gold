from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://sdetchallenge.fetchrewards.com/")

def main() :
    print(driver.title)
    driver.close()

main()

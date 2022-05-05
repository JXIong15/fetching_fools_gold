from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# maybe add a env file?
driver.get("http://sdetchallenge.fetchrewards.com/")

def main():
    assert "React" in driver.title
    goldBars = driver.find_elements(By.XPATH, "//div[@class='coins']/button")
    ans = None

    if len(goldBars) % 2 != 0:
        extra = goldBars[len(goldBars)-1]
        # print(extra.text)
        goldBars.pop()

    halfway = int(len(goldBars) / 2)
    print(halfway)

    pile1 = []
    pile2 = []

    for i in range(0, len(goldBars)):
        if i < halfway:
            pile1.append(goldBars[i])
        else:
            pile2.append(goldBars[i])

        # weigh pile1 and pile2
        # if piles are equal: set ans = extra and return
        # else: take lighter pile and repeat for loop


    # for gb in goldBars:
    #     print(gb.text)
    # print(len(goldBars))
    driver.close()

main()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
# maybe add a env file?
driver.get("http://sdetchallenge.fetchrewards.com/")

def main():
    assert "React" in driver.title
    goldBars = driver.find_elements(By.XPATH, "//div[@class='coins']/button")
    ans = None

    while ans == None:
        extra = None
        if len(goldBars) % 2 != 0:
            extra = goldBars[len(goldBars)-1]
            goldBars.pop()

        left = []
        right = []
        halfway = int(len(goldBars) / 2)

        # make sure board is empty before every weighing
        driver.find_element(By.XPATH, "//button[contains(text(),'Reset')]").click()

        # split bars in two equal piles for weighing
        for i in range(0, len(goldBars)):
            id = ""
            if i < halfway:
                left.append(goldBars[i])
                id = f"left_{i}"
            else:
                right.append(goldBars[i])
                id = f"right_{i}"
                
            # input values to weigh
            driver.find_element(By.ID, id).send_keys(goldBars[i].text)

        # weigh left and right piles
        driver.find_element(By.ID, "weigh").click()

        # WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='game-info']/li")))
        time.sleep( 5 ) # IDK why this works and the above don't
        res = driver.find_element(By.XPATH, "//div[@class='result']/button")

        # compare piles
        if res.text == "=":
            ans = extra
        elif res.text == "<":
            goldBars = left
            if len(left) == 1:
                ans = left[0]
        elif res.text == ">":
            goldBars = right
            if len(right) == 1:
                ans = right[0]
        
    print(ans.text)
    # driver.close()
    # driver.quit()

main()
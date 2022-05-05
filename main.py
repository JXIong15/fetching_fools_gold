from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# maybe add a env file?
driver.get("http://sdetchallenge.fetchrewards.com/")

def main():
    assert "React" in driver.title
    goldBars = driver.find_elements(By.XPATH, "//div[@class='coins']/button")
    resetBtn = driver.find_element(By.XPATH, "//button[contains(text(),'Reset')]")
    ans = None

    while ans == None:
        extra = None
        if len(goldBars) % 2 != 0:
            extra = goldBars[len(goldBars)-1]
            goldBars.pop()

        left = []
        right = []
        halfway = int(len(goldBars) / 2)
        resetBtn.click()    # make sure board is empty before every weighing

        for i in range(0, len(goldBars)):
            id = ""
            if i < halfway:
                left.append(goldBars[i])
                id = f"left_{i}"
            else:
                right.append(goldBars[i])
                id = f"right_{i}"
            
            # input values to weigh
            inputSQR = driver.find_element(By.ID, id)
            inputSQR.send_keys(str(i))

        # weigh left and right piles
        driver.find_element(By.ID, "weigh").click()
        weighRes = driver.find_element(By.XPATH, "//div[@class='result']/button").text

        # compare piles
        if weighRes == "=":
            ans = extra
        elif weighRes == "<":
            goldBars = left
        else:
            goldBars = right

    print(ans)
    driver.close()

main()

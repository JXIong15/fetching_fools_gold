from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("http://sdetchallenge.fetchrewards.com/")


 # split bars in two equal piles for weighing
def weighIns(goldBars, left, right):
    halfway = int(len(goldBars) / 2)
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
        
    driver.find_element(By.ID, "weigh").click()


# use weigh in results to determine what to do next
def compare(goldBars, left, right, extra, ans):
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
    
    return goldBars, ans


# prints results to console
def results(ans):
    print("Fake Gold Bar: ", ans.text)

    weighings = driver.find_elements(By.XPATH, "//div[@class='game-info']/ol/li")
    w = []
    for weighing in weighings:
        w.append(weighing.text)
    print("Weighing Results: ", w)

    driver.find_element(By.ID, f"coin_{ans.text}").click()
    alert = driver.switch_to.alert
    print("Alert Text: ", alert.text)
    alert.accept()


def main():
    goldBars = driver.find_elements(By.XPATH, "//div[@class='coins']/button")
    ans = None

    while ans == None:
        extra = None
        left = []
        right = []

        if len(goldBars) % 2 != 0:
            extra = goldBars[len(goldBars)-1]
            goldBars.pop()

        # make sure board is empty before every weighing
        driver.find_element(By.XPATH, "//button[contains(text(),'Reset')]").click()
        weighIns(goldBars, left, right)
        time.sleep( 2 )
        goldBars, ans = compare(goldBars, left, right, extra, ans)
        
    results(ans)
    driver.close()
    driver.quit()

main()
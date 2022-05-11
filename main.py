from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math


driver = webdriver.Chrome()
driver.get("http://sdetchallenge.fetchrewards.com/")


def main():
    gold_bars = driver.find_elements(By.XPATH, "//div[@class='coins']/button")
    ans = find_fake(gold_bars)
    results(ans, len(gold_bars))
    driver.close()
    driver.quit()


def find_fake(gold_bars):
    ans = None
    extra = None

    while ans == None:
        left = []
        right = []

        if len(gold_bars) % 2 != 0:
            extra = gold_bars[len(gold_bars)-1]
            gold_bars.pop()

        # make sure board is empty before every weighing
        driver.find_element(By.XPATH, "//button[contains(text(),'Reset')]").click()
        weigh_ins(gold_bars, left, right)
        time.sleep(1)   # wait for weigh-in result to process
        gold_bars, ans = compare(gold_bars, left, right, extra)

    return ans


 # split bars in two equal piles for weighing
def weigh_ins(gold_bars, left, right):
    halfway = int(len(gold_bars) / 2)
    for i in range(0, len(gold_bars)):
        id = ""
        if i < halfway:
            left.append(gold_bars[i])
            id = f"left_{i}"
        else:
            right.append(gold_bars[i])
            id = f"right_{i}"
                
        # input values to weigh
        driver.find_element(By.ID, id).send_keys(gold_bars[i].text)

    driver.find_element(By.ID, "weigh").click()


# use weigh-in results to determine what to do next
def compare(gold_bars, left, right, extra):
    ans = None
    res = driver.find_element(By.XPATH, "//div[@class='result']/button")

    # compare piles
    if res.text == "=":
        ans = extra
    elif res.text == "<":
        gold_bars = left
        if len(left) == 1:
            ans = left[0]
    elif res.text == ">":
        gold_bars = right
        if len(right) == 1:
            ans = right[0]

    return gold_bars, ans


# prints results to console
def results(ans, n):
    print("Fake Gold Bar: ", f"#{ans.text}")

    weighings = driver.find_elements(By.XPATH, "//div[@class='game-info']/ol/li")
    assert len(weighings) > 0
    w = []
    for weighing in weighings:
        w.append(weighing.text)
    print("Weighing Result(s): ", w)
    print("Number of Weighing(s): ", len(w))
    assert len(w) <= min_weighings(n)

    driver.find_element(By.ID, f"coin_{ans.text}").click()
    alert = driver.switch_to.alert
    print("Results Message: ", alert.text)
    assert "Yay!" in alert.text
    alert.accept()


# calculates the minimum amount of weighings to find fake bar of gold
def min_weighings(n):
    return math.floor(math.log2(n))


main()
from selenium import webdriver
from selenium.webdriver.support import ui
from bs4 import BeautifulSoup
import argparse
import time
import re


def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") is not None


def page_reached(driver, url):
    while driver.current_url != url:
        time.sleep(20)


parser = argparse.ArgumentParser()
parser.add_argument("url", help="url for the page to ctf")
args = parser.parse_args()

base_url = args.url
login_url = "/".join([base_url, "login"])
challenge_url = "/".join([base_url, "challenges"])

options = webdriver.ChromeOptions()
options.add_argument("disable-infobars")
driver = webdriver.Chrome(options=options)
wait = ui.WebDriverWait(driver, 10)
driver.get(login_url)
wait.until(page_is_loaded)
# wait until user logs in
page_reached(driver, challenge_url)

challenge_page_soup = BeautifulSoup(driver.page_source, "html.parser")
challenges_board = challenge_page_soup.find("div", id="challenges-board")

buttons = challenges_board.find_all("button")

for button in buttons:
    id_attr = button.parent.attrs['id']
    xpath = f'//*[@id="{id_attr}"]/button'
    button_element = driver.find_element_by_xpath(xpath)
    button_element.click()
    wait.until(page_is_loaded)
    soup = BeautifulSoup(driver.page_source, "html.parser")


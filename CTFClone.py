from selenium import webdriver
from selenium.webdriver.support import ui
from bs4 import BeautifulSoup
import argparse
import time
import re
from Challenge import Challenge
import os

def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") is not None


def page_reached(driver, url):
    while driver.current_url != url:
        time.sleep(20)


def download_file(driver, link):
    """
    Download link with selenium driver
    """
    pass
    file_path = ""
    return file_path


parser = argparse.ArgumentParser()
parser.add_argument("url", help="url for the page to ctf")
parser.add_argument("--ctf-name", "-n", help="Name of the ctf (to be used as a directory name")
args = parser.parse_args()

parent_path = args.ctf_name if args.ctf_name is not None else os.path.join(os.getcwd(), "cloned_ctf")
os.makedirs(parent_path, exist_ok=True)

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
challenge_page_links = set(challenge_page_soup.find_all("a"))
challenges_board = challenge_page_soup.find("div", id="challenges-board")

buttons = challenges_board.find_all("button")

for button in buttons:
    id_attr = button.parent.attrs['id']
    xpath = f'//*[@id="{id_attr}"]/button'
    button_element = driver.find_element_by_xpath(xpath)
    button_element.click()
    wait.until(page_is_loaded)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    this_challenge_page_links = set(soup.find_all("a"))
    new_links = list(this_challenge_page_links - challenge_page_links)
    files_and_links = [i for i in new_links
                       if re.match(r'#(challenge|solves)', i.attrs['href']) is None]

    downloaded_file_paths = [download_file(driver, link) for link in files_and_links]
    name = ""
    category = ""
    message = ""
    value = ""
    # Challenge(name, category, message, value, downloaded_file_paths, parent_path)
    # re-navigate to challenge_url
    # driver.get(challenge_url)



from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
import sys


def get_links(url: str) -> list:
    """Find all links on page at the given url.
    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    browser.get(url)
    link_list = browser.find_element(By.TAG_NAME, 'a')
    set_hyperlink = set()
    for link in link_list:
        temp_link = link.get_attribute('href')
        if temp_link is not None:
            if '#' in temp_link:
                temp_link = temp_link.split('#')[0]
            elif '?' in temp_link:
                temp_link = temp_link.split('?')[0]
            set_hyperlink.add(temp_link)
    return list(set_hyperlink)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('Usage: python3 link_scan.py url')
        sys.exit()
    browser: WebDriver = webdriver.Chrome('C:/ISP/chromedriver')
    url = sys.argv[1]
    link = get_links(url)

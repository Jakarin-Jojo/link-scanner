import os
from typing import List
from urllib import request
from urllib.error import HTTPError, URLError


from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium import webdriver
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


def is_valid_url(url: str) -> bool:
    """Check if the url is valid and reachable or not.

       Returns:
           True if the URL is OK, False otherwise.
       """
    try:
        request.urlopen(url)
    except HTTPError as e:
        if e.getcode() != 403:
            return False
    except URLError:
        return False
    return True


def invalid_urls(urllist: List[str]) -> List[str]:
    """Validate the urls in urllist and return a new list containing
    the invalid or unreachable urls.
    Args:
        urllist(List[str]): The List of urls which will check.
    Returns:
        List[str]: A new list of the invalid or unreachable urls.
    """
    list_badlink = []
    for url in urllist:
        if not is_valid_url(url):
            list_badlink.append(url)
    return list_badlink


if __name__ == "__main__":
    if len(sys.argv) != 2:
        filename = os.path.basename(sys.argv[0])
        print(f'Usage: python3 {filename} url\n\nTest all hyperlinks on the given url.')
        sys.exit()
    PATH = 'C:/ISP/chromedriver.exe'
    browser: WebDriver = webdriver.Chrome(PATH)
    url = sys.argv[1]
    list_link = get_links(url)
    list_bad_link = invalid_urls(list_link)
    print('Show The list of Good link.')
    for url in list_link:
        print(url)
    print('Show The list of Bad link.')
    for url in list_bad_link:
        print(url)

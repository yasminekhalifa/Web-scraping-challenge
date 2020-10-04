from bs4 import BeautifulSoup as bs
from time import sleep
import time 
import pandas as pd
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import requests
from urllib.request import urlopen as uReq


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
    mars_dict = {}
    # ## NASA Mars News
    url = "https://mars.nasa.gov/news"
    browser.visit(url)
    time.sleep(5)

    html = browser.html

    news_soup = bs(html, 'html.parser')

    slide_elem = news_soup.select('ul.item_list li.slide')

    title = slide_elem[0].find('div', class_="content_title").text
    teaser = slide_elem[0].find('div', class_="article_teaser_body").text

    # ## JPL Mars Space Images - Featured Image
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    browser.find_by_id("full_image").click()
    time.sleep(5)
    html = browser.html
    soup = bs(html, 'html.parser')

    img_elem = soup.select_one('img.fancybox-image').get('src')

    featured_image_url = f"https://www.jpl.nasa.gov{img_elem}"
    print(featured_image_url)

    url = 'https://space-facts.com/mars/'
    browser.visit(url)

    tables = pd.read_html(url)


    df = tables[0]
    df.columns = ['factor','value']
    df.head()

    df.set_index('factor', inplace=True)
    df.head()

    html_table = df.to_html()
    html_table

    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')

    titles = soup.find_all("h3")
    titles_list = []
    for t in titles:
        print(t.text)
        titles_list.append(t.text)  

    links = []
    for b in titles_list:
        try:
            browser.click_link_by_partial_text(b)
            sleep(1)
            html = browser.html
            soup = bs(html, 'html.parser')
            link = soup.li.a["href"]
            links.append(link)
            browser.back()
        except:
            print("skip")

    for link in links:
        print(link)

    Hemisphere_image_url = [ {'Title': titles_list[i], 'image_url': links[i] } for i in range(len(links)) ]
    print(Hemisphere_image_url)

    mars_dict = {
        "title": title,
        "teaser": teaser,
        "featured_image_url": featured_image_url,
        "table": html_table,
        "Hemisphere_image_url": Hemisphere_image_url}

    browser.quit()
    return mars_dict







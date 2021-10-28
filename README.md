# Web Scraping Homework - Mission to Mars


I created a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.
* Scraped the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text.
* Used splinter to navigate the site and find the image url for the current Featured Mars Image[here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) 
* Used Pandas to scrape the table containing facts about the planet including Diameter, Mass from the Mars Facts webpage [here](https://space-facts.com/mars/) 
* Scraped the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.


Secondly, Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

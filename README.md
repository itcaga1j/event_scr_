# **Scraping Eventim using Scrapy**
Scrapy is free and open source Python framework used for web scraping websites. It provides tools needed to efficiently extract data from web pages, process and store it in a wanted format and structure.

Using Scrapy you can easily build highly scalable scrapers that will retrieve a pages HTML, parse and process the data, and store it the file format and location of your choice.

#### Why & When Should You Use Scrapy? ####

Although, there are other Python libraries also used for web scraping:

- Python Requests/BeautifulSoup: Good for small scale web scraping where the data is returned in the HTML response. Would need to build you own spider management functionality to manage concurrency, retries, data cleaning, data storage.

- Python Request-HTML: Combining Python requests with a parsing library, Request-HTML is a middle-ground between the Python Requests/BeautifulSoup combo and Scrapy.

- Python Selenium: Use if you are scraping a site if it only returns the target data after the Javascript has rendered, or you need to interact with page elements to get the data.

Python Scrapy has lots more functionality and is great for large scale scraping right out of the box:

- CSS Selector & XPath Expressions Parsing
- Data formating (CSV, JSON, XML) and Storage (FTP, S3, local filesystem)
- Robust Encoding Support
- Concurrency Managment
- Automatic Retries
- Cookies and Session Handling
- Crawl Spiders & In-Built Pagination Support

You just need to customise it in your settings file or add in one of the many Scrapy extensions and middlewares that developers have open sourced.

The learning curve is initially steeper than using the Python Requests/BeautifulSoup combo, however, it will save you a lot of time in the long run when deploying production scrapers and scraping at scale.

## Assignment

Scraping Eventim website

Link: https://www.eventim.de/en/

## Installation and starting in Google Colab

#### Step 1: Install Scrapy in virtual environment

![image](https://user-images.githubusercontent.com/92359665/186121663-b463dc07-9ca3-4529-9d81-d382142ae864.png)

#### Step 2: Creating Our Scrapy Project

![image](https://user-images.githubusercontent.com/92359665/186122134-a8249e44-ab7b-4ac8-bc31-70a53141a5d7.png)

#### Step 3: Creating the Spider

![image](https://user-images.githubusercontent.com/92359665/186122371-d72ab30c-d583-4286-bbd7-652a93d702d6.png)

#### Step 4: Scrapy Shell: Finding CSS Selectors

![image](https://user-images.githubusercontent.com/92359665/186122789-213c14cd-aaa3-4eb6-b7ef-2e693286ec36.png)

#### Step 5: Running Spider





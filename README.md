# Realtor Web Scraper

The Realtor Web Scraper is a powerful tool for extracting real estate data from Realtor.com. This Python-based web scraping project allows you to define custom parameters to filter and collect specific real estate listings and related information according to your preferences. Whether you're a real estate investor, researcher, or simply curious about the market, this scraper simplifies the process of obtaining valuable data for your analysis.


## Tech Stack

The Realtor Web Scraper utilizes a combination of Python libraries and tools to provide powerful web scraping capabilities and data analysis. Here's an overview of the tech stack used in this project:

- **Python**: The core programming language for building and running the scraper.

- **Beautiful Soup 4 (bs4)**: A Python library for web scraping and parsing HTML and XML documents. It enables you to extract structured data from web pages.

- **NumPy (numpy)**: A fundamental library for numerical computing in Python. While not directly related to web scraping, it is valuable for data manipulation and analysis after data extraction.

- **Pandas (pandas)**: A popular Python library for data manipulation and analysis. It's used for cleaning, transforming, and analyzing the scraped data.

- **Selenium (selenium)**: A web testing framework that allows you to automate web interactions, such as navigating websites and filling out forms. In this project, Selenium is used to interact with web pages when necessary.

- **Streamlit (streamlit)**: A Python library for creating interactive web applications with minimal code. You can use Streamlit to build user-friendly interfaces for displaying and analyzing the scraped data.

- **Undetected Chromedriver (undetected_chromedriver)**: A library that helps bypass bot detection mechanisms on websites that use ChromeDriver. This is particularly useful when using Selenium for web scraping.

These libraries and tools have been carefully chosen to provide a robust and efficient solution for web scraping, data extraction, and data analysis in your Realtor Web Scraper project.

## Run Locally
I'm having issue to upload this to streamlit cloud but you still can run it locally, make sure you have streamlit installed on your device.

Clone the project

```bash
  git clone https://github.com/kevinfernaando/realtor-web-scraper
```

Go to the project directory

```bash
  cd realtor-web-scraper
```


Start the server

```bash
  streamlit run app.py
```


## Screenshots

This is going to be the first page that you see

<img width="1002" alt="Screenshot 2023-09-27 at 11 38 46" src="https://github.com/kevinfernaando/realtor-web-scraper/assets/77948222/0fd8e9b0-46a4-414b-a57e-69f15e7b860e">


You must input the location with [City, State] format like London, KY then you can fill the filter as needed

<img width="1002" alt="Screenshot 2023-09-27 at 11 31 34" src="https://github.com/kevinfernaando/realtor-web-scraper/assets/77948222/2417cc2a-4e2e-4d3f-8bf5-3807fd2d1b6d">


You just need to clik "Scrape Data" button and the app will scrape the data and return a dataframe, you also can download the scraped data into csv file by pressing "Download Data" button

<img width="1002" alt="Screenshot 2023-09-27 at 11 50 08" src="https://github.com/kevinfernaando/realtor-web-scraper/assets/77948222/214cbbac-8e72-4d1f-85d1-332335eeaf4a">


## Authors

- [@kevinfernaando](https://github.com/kevinfernaando)

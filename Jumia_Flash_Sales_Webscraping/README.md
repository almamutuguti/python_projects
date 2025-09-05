# Jumia Flash Sales Web Scraping Project

## Project Overview
The Jumia Flash Sales Web Scraping project aims to automatically extract essential product information from Jumia's Flash Sales section. The project uses Selenium to load dynamic web pages and BeautifulSoup to parse and extract product data. The scraped data will be stored in a CSV file for further analysis.

## Objectives
The primary objective of this project is to create an automated scraper that gathers information about products listed in Jumia’s Flash Sales. This information can be used to analyze discounts, monitor stock availability, and track pricing trends.

## Data to be Collected
The scraper will collect the following information for each product:
- Product name  
- Old price (if available)  
- New price  
- Discount percentage (or 'No discount' if not available)  
- Rating (if available)  
- Number of ratings (if available)  
- Stock level (if displayed)  
- URL to the product details page  

## Tools and Technologies
- Python 3  
- Selenium (for handling dynamic content and navigation)  
- BeautifulSoup (for parsing HTML content)  
- CSV module (for saving extracted data into CSV format)  

## Workflow
1. Use Selenium to open Jumia’s Flash Sales page in headless mode.  
2. Extract the page source and pass it to BeautifulSoup for parsing.  
3. Identify and extract product details such as name, price, discount, etc.  
4. Save the extracted data into a structured CSV file.  
5. Repeat the process for multiple pages until all products are scraped.  
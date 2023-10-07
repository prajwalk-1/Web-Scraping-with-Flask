## Web-Scraping-with-Flask

This is a Flask-based web application that allows users to fetch data from the website and display it in an HTML table. 
Users can specify the range of pages and the number of items to retrieve using a web form.

# Features
- Fetch data from archive.org based on user-defined parameters.
- Display fetched data in an HTML table.
- Input validation to ensure valid page numbers and item counts.
- Error handling for failed requests.

# Usage

1. Access the web application in your browser by visiting http://localhost:5000/.
2. You will see a form where you can input the following parameters:
  a. page_start: The starting page number.
  b. page_end: The ending page number.
  c. count: The number of items to retrieve for each page.
3. Click the "Submit" button to fetch data from archive.org based on your input.
4. The fetched data will be displayed in an HTML table on the same page.

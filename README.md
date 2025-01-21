### Web Scraper for Employee Contact Information

This project is a Python web scraper designed to extract email addresses and phone numbers from any target website. The script dynamically asks the user to input the target URL and then scrapes the content of the webpage to find the desired contact information. The scraper uses regular expressions and the BeautifulSoup library to parse HTML and extract data.

Features
Dynamic Input: The script prompts the user to enter the target website URL.
Email and Phone Number Extraction:
Extracts emails using regex patterns.
Finds phone numbers in formats like (123) 456-7890, 123-456-7890, or 123.456.7890.
ANSI Header: Displays a visually appealing header with the developer's name.
Error Handling: Handles connection errors, invalid URLs, and empty results gracefully.
De-duplication: Ensures no duplicate emails or phone numbers in the results.
Prerequisites
Before running the script, ensure you have the following:

Python 3.6+ installed on your system.
Required Python libraries:
requests: For making HTTP requests to the target website.
BeautifulSoup4: For parsing and scraping HTML content.
You can install the required libraries by running:
bash

pip install requests beautifulsoup4
How to Use
Clone or download this repository to your local system.
Open a terminal or command prompt and navigate to the folder containing the script.
Run the script using Python:
bash

python webx.py
When prompted, enter the target website URL. For example:
bash

Enter the target website URL (e.g., https://example.com): https://example.com
The script will fetch the website data, extract email addresses and phone numbers, and display the results in the terminal.




python
Copy
Edit
def print_header():
    header = """
    ███████╗███████╗██████╗ ██╗      █████╗ ███████╗███████╗
    ...
    """
    print(header)
Dynamic Input:

The script prompts the user for the target URL:
python
Copy
Edit
target_url = input("Enter the target website URL (e.g., https://example.com): ").strip()
Regex for Email and Phone Extraction:

Finds email addresses using:
regex
Copy
Edit
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
Finds phone numbers using:
regex

\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}
Result Display:

Results are displayed in a clean, numbered list.
Limitations
Dynamic Web Pages: This script does not handle JavaScript-rendered content. Use tools like Selenium for such scenarios.
Anti-Scraping Protections: If the target site uses CAPTCHAs or IP blocking, consider implementing proxies or CAPTCHA-solving mechanisms.

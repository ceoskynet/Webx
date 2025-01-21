import requests
from bs4 import BeautifulSoup
import re

# ANSI Regular Font Header
def print_header():
    header = """
    \033[1;34m
    ██     ██ ███████ ██████  ██ 
██     ██ ██      ██   ██  ██ ██  
██  █  ██ █████   ██████    ███   
██ ███ ██ ██      ██   ██  ██ ██  
 ███ ███  ███████ ██████  ██   ██
         \033[1;92mDeveloped by Shaheer Yasir\033[0m
    """
    print(header)


# Function to scrape for emails and phone numbers
def scrape_web_x(target_url):
    try:
        print(f"\033[1;33m[+] Sending request to {target_url}...\033[0m")
        response = requests.get(target_url)

        if response.status_code == 200:
            print("\033[1;32m[+] Successfully connected to the target website!\033[0m")

            # Parse the HTML using BeautifulSoup
            soup = BeautifulSoup(response.content, "html.parser")
            
            # Extract emails and phone numbers
            employees = []

            # Use regex to find emails and phone numbers in the HTML
            email_matches = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', soup.get_text())
            phone_matches = re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', soup.get_text())

            # Combine results into a unique list
            for email in set(email_matches):
                employees.append({"email": email, "phone": None})

            for phone in set(phone_matches):
                employees.append({"email": None, "phone": phone})

            # Print results
            print("\033[1;36m[+] Contact Information Found on the Target Website:\033[0m")
            if employees:
                for i, emp in enumerate(employees, 1):
                    print(f"\033[1;37m{i}. Email: {emp['email']}, Phone: {emp['phone']}\033[0m")
            else:
                print("\033[1;31m[-] No emails or phone numbers found.\033[0m")

        else:
            print(f"\033[1;31m[-] Failed to connect to the target website. Status code: {response.status_code}\033[0m")
    
    except Exception as e:
        print(f"\033[1;31m[-] Error occurred: {e}\033[0m")


# Main function
if __name__ == "__main__":
    # Print the header
    print_header()
    
    # Ask the user for the target website URL
    target_url = input("\033[1;34mEnter the target website URL (e.g., https://example.com): \033[0m").strip()
    
    if target_url:
        # Scrape the target website
        scrape_web_x(target_url)
    else:
        print("\033[1;31m[-] No URL provided. Exiting...\033[0m")

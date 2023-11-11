# practice here: https://www.scrapethissite.com/

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import requests 
import json

def scrape_website(url, username, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # Open a new page
        page = context.new_page()

        # Navigate to the login page
        page.goto(url)
        # Wait for navigation to complete
        page.wait_for_load_state()
        # Fill in the login form
        #page.fill('username', username)
        #page.fill('password', password)
        page.get_by_placeholder("Username").fill(username)
        page.get_by_placeholder("Password").fill(password)
        page.click('button[type="submit"]')

        # Click the login button
        #page.click('button[type="submit"]')

        # Wait for navigation to complete
        #page.wait_for_load_state('load')
        page.wait_for_load_state()

        # Now, you can scrape the data from the logged-in page
        # Get the HTML content after logging in
        logged_in_html = page.content()

        # Use Beautiful Soup to parse the HTML
        soup = BeautifulSoup(logged_in_html, 'html.parser')
        with open("output.txt", 'w', encoding='utf-8') as file:
            file.write(soup.prettify())
        
       # Get the cookies from the browser context
        cookies = context.cookies()

        # Use requests library to make a request with the obtained cookies
        response = requests.get('https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/directory/employees?limit=14&offset=0', cookies={cookie['name']: cookie['value'] for cookie in cookies})

        # Process the response
        print(response.text)
        data_dict = json.loads(response.text)

        # Save the dictionary to a JSON file
        output_file = "output.json"
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(data_dict, json_file, ensure_ascii=False, indent=4)

        # Close the browser
        # browser.close()

if __name__ == "__main__":
    url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    username = "Admin"
    password = "admin123"

    scrape_website(url, username, password)

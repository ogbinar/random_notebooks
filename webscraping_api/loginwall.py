from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import requests 
import json

def scrape_website(url, username, password):
    # Launch Playwright browser
    with sync_playwright() as p:
        # Create a new browser context
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # Open a new page
        page = context.new_page()

        # Navigate to the login page
        page.goto(url)
        # Wait for navigation to complete
        page.wait_for_load_state()

        # Fill in the login form
        page.get_by_placeholder("Username").fill(username)
        page.get_by_placeholder("Password").fill(password)
        page.click('button[type="submit"]')

        # Wait for navigation to complete after clicking the login button
        page.wait_for_load_state()

        # Get the HTML content after logging in
        logged_in_html = page.content()

        # Use Beautiful Soup to parse the HTML
        soup = BeautifulSoup(logged_in_html, 'html.parser')
        
        # Save the parsed HTML to a file for inspection
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

    # Call the function to scrape the website
    scrape_website(url, username, password)


    """
    Advantages of the Provided Web Scraping Code:

The code leverages Playwright for browser automation, providing a realistic emulation of user interactions and dynamic content loading. This approach is advantageous when dealing with websites that heavily rely on JavaScript for rendering content or require user authentication for access. By automating the login process and utilizing a headless browser, the code can effectively handle complex scenarios, such as those involving session management and anti-bot mechanisms. Additionally, the use of browser automation allows for the extraction of data from dynamically generated pages, which might be challenging with static HTTP requests.

Disadvantages of the Provided Web Scraping Code:

Despite its advantages, the code has notable drawbacks. Browser automation introduces resource-intensive overhead, making it less suitable for large-scale scraping tasks or environments with limited resources. The reliance on cookies from the browser context may pose challenges in scenarios with complex cookie management. Additionally, the code's dependence on rendering entire pages, even in headless mode, can lead to slower execution compared to more lightweight HTTP-based solutions. The complexity of maintaining browser automation scripts, potential legal and ethical concerns, and limitations in scalability further highlight the need for careful consideration of alternative scraping approaches based on specific use cases and requirements.
    """
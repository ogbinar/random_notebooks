import requests
from bs4 import BeautifulSoup

def scrape_blog(url):
    # Make a request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all article titles (adjust the selector based on the structure of the website)
        article_titles = soup.find_all('h3', class_='post-title entry-title')

        # Print the titles
        for title in article_titles:
            print(title.text)
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    # Replace this URL with the actual URL of the website you want to scrape
    target_url = "https://cofibean.blogspot.com/"

    scrape_blog(target_url)

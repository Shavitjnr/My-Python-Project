import requests
from bs4 import BeautifulSoup
import csv
import json

# Example: Scrape news headlines from BBC News homepage
NEWS_URL = 'https://www.bbc.com/news'


def scrape_news():
    print("Scraping news headlines from BBC News...")
    response = requests.get(NEWS_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = []
    for item in soup.find_all('h3'):
        text = item.get_text(strip=True)
        if text and text not in headlines:
            headlines.append(text)
    print(f"Found {len(headlines)} headlines.")
    return headlines

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow([row])
    print(f"Saved to {filename}")

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved to {filename}")

def main():
    print("Web Scraper")
    print("1. Scrape news headlines (BBC News)")
    # You can add more options for jobs/products with more code
    choice = input("Choose an option: ")
    if choice == '1':
        data = scrape_news()
    else:
        print("Invalid choice.")
        return

    print("How would you like to save the data?")
    print("1. CSV\n2. JSON\n3. Display in CLI")
    out = input("Choose an option: ")
    if out == '1':
        save_to_csv(data, 'news_headlines.csv')
    elif out == '2':
        save_to_json(data, 'news_headlines.json')
    elif out == '3':
        for i, headline in enumerate(data, 1):
            print(f"{i}. {headline}")
    else:
        print("Invalid output option.")

if __name__ == "__main__":
    main()

from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("http://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
quotes = soup.findAll("span", attrs={"class": "text"})
authors = soup.findAll("small", attrs={"class": "author"})


def write_quotes_to_txt():
    """Scrapes quotes and authors and writes them to a text file."""
    file_path = "C:/Users/Owner/Desktop/ScrapedQuotes.txt"

    try:
        # Using 'with' ensures the file is closed automatically.
        # encoding='utf-8' is good practice for text files.
        with open(file_path, "w", encoding="utf-8") as file:
            # zip() pairs each quote with its corresponding author.
            for quote, author in zip(quotes, authors):
                # Need to write the .text content of the BeautifulSoup tags.
                line = f'"{quote.text}" - {author.text}\n'
                file.write(line)
                print(line, end="")
        print(f"\n\nSuccessfully wrote quotes to {file_path}")
    except IOError as e:
        # Catching potential file writing errors.
        print(f"An error occurred while writing to the file: {e}")


if __name__ == "__main__":
    write_quotes_to_txt()

import pandas as pd

from webScraper.Scraper import Scraper

def main():
    quotes = []
    for i in range(1, 11):
        scraperQuotes = Scraper(f'https://quotes.toscrape.com/page/{i}/')
        soup = scraperQuotes.scrapPage()

        quoteHtml = soup.find_all('div', {
            'class': 'quote'
        })

        for element in quoteHtml:
            quote = {}

            quote["text"] = element.find('span', class_='text').text
            quote["author"] = element.find('small', class_='author').text

            tagsA = element.find_all('a', class_='tag')
        
            quote["tags"] = []
            for a in tagsA:
                quote["tags"].append(a.text)

            quotes.append(quote)

    df = pd.DataFrame(quotes, columns=['text', 'author', 'tags'])
    df.to_csv('quotes.csv', index=False)

if __name__ == "__main__":
    main()

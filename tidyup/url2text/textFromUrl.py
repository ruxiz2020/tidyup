import requests
from bs4 import BeautifulSoup
#import base64
#from langdetect import detect


class TextFromUrl:

    def __init__(self, url):
        """
        Extract text data from url
        """
        self._url = url

    def extract_text_from_html(self):

        response = requests.get(self._url)
        data = response.content.decode('utf-8', errors="replace")

        soup = BeautifulSoup(data, "lxml")
        page = soup.findAll('p')

        sentences = []
        for pp in page:

            text = pp.getText()
            if text.strip() != '':
                sentences.append(text + " ")
            # print(text)

        paragraph = ' '.join(sentences)
        return paragraph


if __name__ == "__main__":

    url = "https://pets.webmd.com/cats/cat-fip-feline-infectious-peritonitis#1"
    #url = "https://mp.weixin.qq.com/s/mvmbJsORjsLjGfpz5yScWg"
    print(url)

    extractText = TextFromUrl(url)
    text = extractText.extract_text_from_html()

    print(text)

    file = open("../read_it/test.txt", "w")
    file.write(text)
    file.close() #This close() is important

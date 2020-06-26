import logging


from urllib.request import Request, urlopen

logger = logging.getLogger(__name__)


class Scraper:

    def __init__(self, storage):
        self.storage = storage

    def scrape(self):
        """ Gives the text from CoronaVirus website """

        url = "https://www.worldometers.info/coronavirus/"
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        dataAsBytes = urlopen(req).read()
        data = dataAsBytes.decode("utf8")

        # save scraped objects here
        # you can save url to identify already scrapped objects
        self.storage.save_raw_data(data)


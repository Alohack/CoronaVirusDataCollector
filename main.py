"""

To run the file you can use your ide or terminal:
python main.py gather
python main.py parse
python main.py stats

"""

import pandas as pd
import matplotlib.pyplot as plt
import sys
import logging
from csv import writer

from scraper import Scraper
from storage import Persistor
from parsers import Parser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

RAW_DATA_FILE = "CovidData/CovidData.txt"
CSV_DATA_FILE = "CovidData/CovidData.csv"


def addRow(newRow):
    # Open file in append mode
    with open(CSV_DATA_FILE, 'a+', newline='', encoding='utf-8') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(newRow)


def gather():
    logger.info("gather")

    coronaVirusPersistor = Persistor(RAW_DATA_FILE, CSV_DATA_FILE)
    coronaVirusScraper = Scraper(coronaVirusPersistor)
    coronaVirusScraper.scrape()


def parser_to_csv(coronaVirusDataParser):
    # Here are the names of the parameters
    columnTitles = ["TotalCases", "NewCases", "TotalDeaths", "NewDeaths",
                    "TotalRecovered", "ActiveCases", "SeriousCritical", "Total1M",
                    "Deaths1M", "TotalTests", "Tests1M", "Population", "Mainland"]
    addRow(columnTitles)

    # add to csv row by row
    for nextData in coronaVirusDataParser:
        addRow(nextData)


def parse():
    # parse gathered data and save as csv
    logger.info("parse")

    coronaVirusPersistor = Persistor(RAW_DATA_FILE, CSV_DATA_FILE)
    coronaVirusData = coronaVirusPersistor.read_raw_data()
    coronaVirusParser = Parser(coronaVirusData)

    coronaVirusPersistor.create_csv()
    # Turning parser to csv file
    parser_to_csv(coronaVirusParser)


# Here I displayed 8 countries with the largest amounts of total cases of corona-virus
def stats():
    logger.info("stats")

    df = pd.read_csv(CSV_DATA_FILE)
    df = df.sort_values(by=['TotalDeaths'], ascending=[False])

    df.head(8).plot.pie(y='TotalDeaths', figsize=(5, 5))
    plt.show()


if __name__ == '__main__':
    logger.info("Work started")

    gather()
    parse()
    stats()

    logger.info("work ended")

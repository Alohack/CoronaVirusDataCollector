"""

Your task is to gather data from the Internet,
parse it and save to a csv file

To run the file you can use your ide or terminal:
python3 -m main gather
python3 -m main parse

The logging package helps you to better track how the processes work
It can also be used for saving the errors that arise

"""

import pandas as pd
import matplotlib.pyplot as plt
import sys
import logging

from scraper import Scraper
from storage import Persistor
from parsers import Parser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

FILE_NAME = "CovidData"

def gather():
    logger.info("gather")

    coronaVirusPersistor = Persistor(FILE_NAME)
    coronaVirusScraper = Scraper(coronaVirusPersistor)
    coronaVirusScraper.scrape()

def parser_to_csv(coronaVirusDataParser):
    # Here are the names of the parameters
    coronaVirusAsCSV = "TotalCases,NewCases,TotalDeaths,NewDeaths,TotalRecovered,ActiveCases,SeriousCritical,Total1M," \
                       "Deaths1M,TotalTests,Tests1M,Population\n "
    for nextData in coronaVirusDataParser:
        coronaVirusAsCSV += nextData.property_1 + ","
        coronaVirusAsCSV += nextData.property_2 + ","
        coronaVirusAsCSV += nextData.property_3 + ","
        coronaVirusAsCSV += nextData.property_4 + ","
        coronaVirusAsCSV += nextData.property_5 + ","
        coronaVirusAsCSV += nextData.property_6 + ","
        coronaVirusAsCSV += nextData.property_7 + ","
        coronaVirusAsCSV += nextData.property_8 + ","
        coronaVirusAsCSV += nextData.property_9 + ","
        coronaVirusAsCSV += nextData.property_10 + ","
        coronaVirusAsCSV += nextData.property_11 + ","
        coronaVirusAsCSV += nextData.property_12 + ","
        coronaVirusAsCSV += nextData.property_13 + "\n"
    return coronaVirusAsCSV

def parse():
    # parse gathered data and save as csv
    logger.info("parse")


    coronaVirusPersistor = Persistor(FILE_NAME)
    coronaVirusData = coronaVirusPersistor.read_raw_data()
    coronaVirusParser = Parser(coronaVirusData)


    # Turning parser to csv file
    coronaVirusAsCSV = parser_to_csv(coronaVirusParser)
    coronaVirusPersistor.save_csv(coronaVirusAsCSV)


# Here I displayed 8 countries with the largest amounts of total cases of Coronavirus
def stats():
    """ If you have time, you can calculate some statistics on the data gathered """
    logger.info("stats")
    coronaVirusPersistor = Persistor(FILE_NAME)

    df = pd.read_csv(coronaVirusPersistor.csv_file_name())
    df = df.sort_values(by=['TotalDeaths'], ascending=[False])

    plot = df.head(8).plot.pie(y='TotalDeaths', figsize=(5, 5))
    plt.show()

    # Your code here
    # Load pandas DataFrame and print to stdout different statistics about the data.
    # Try to think about the data and use as different methods applicable to DataFrames.
    # Ask yourself what would you like to know about this data (most frequent word, average price, e.t.c.)


if __name__ == '__main__':
    """
    What does the line above mean
    https://stackoverflow.com/questions/419163/what-does-if-name-main-do
    
    logger.info("Work started")
    print("Hello")
    gather()

    logger.info("work ended")
"""

    logger.info("Work started")

    gather()
    parse()
    stats()

    logger.info("work ended")

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


def gather():
    logger.info("gather")

    coronaVirusPersistor = Persistor()
    coronaVirusScraper = Scraper(coronaVirusPersistor)
    coronaVirusScraper.scrape()

def parsed_object_to_csv(coronaVirusDataParsed):
    # Here are the names of the parameters
    coronaVirusAsCSV = "TotalCases,NewCases,TotalDeaths,NewDeaths,TotalRecovered,ActiveCases,SeriousCritical,Total1M," \
                       "Deaths1M,TotalTests,Tests1M,Population\n "
    for i in range(213):
        coronaVirusAsCSV += coronaVirusDataParsed.property_1[i] + ","
        coronaVirusAsCSV += coronaVirusDataParsed.property_2[i] + ","
        coronaVirusAsCSV += coronaVirusDataParsed.property_3[i] + ","
        coronaVirusAsCSV += coronaVirusDataParsed.property_4[i] + ","
        coronaVirusAsCSV += coronaVirusDataParsed.property_5[i] + ","
        coronaVirusAsCSV += coronaVirusDataParsed.property_6[i] + ","
        coronaVirusAsCSV += coronaVirusDataParsed.property_7[i] + ","
        coronaVirusAsCSV += coronaVirusDataParsed.property_8[i] + ","
        coronaVirusAsCSV += coronaVirusDataParsed.property_9[i] + ","
        coronaVirusAsCSV += coronaVirusDataParsed.property_10[i] + ","
        coronaVirusAsCSV += coronaVirusDataParsed.property_11[i] + ","
        coronaVirusAsCSV += coronaVirusDataParsed.property_12[i] + ","
        coronaVirusAsCSV += coronaVirusDataParsed.property_13[i] + "\n"
    return coronaVirusAsCSV

def parse():
    # parse gathered data and save as csv
    logger.info("parse")


    coronaVirusPersistor = Persistor()
    coronaVirusParser = Parser()

    coronaVirusData = coronaVirusPersistor.read_raw_data()

    # Here I could not manage to parse every single object separately
    # so I parsed the whole file instead
    coronaVirusDataParsed = coronaVirusParser.parse_object(coronaVirusData)

    # Then I turned this all to a csv format string
    coronaVirusAsCSV = parsed_object_to_csv(coronaVirusDataParsed)
    coronaVirusPersistor.save_csv(coronaVirusAsCSV)


# Here I displayed 8 countries with the largest amounts of total cases of Coronavirus
def stats():
    """ If you have time, you can calculate some statistics on the data gathered """
    logger.info("stats")
    coronaVirusPersistor = Persistor()

    df = pd.read_csv("CovidData.csv")
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

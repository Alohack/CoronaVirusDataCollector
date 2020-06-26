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


# adding new row to the csv file
def add_row(new_row):
    # Open file in append mode
    with open(CSV_DATA_FILE, 'a+', newline='', encoding='utf-8') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(new_row)


# this function gathers raw data from the internet
# and saves it to the RAW_DATA_FILE
def gather():
    logger.info("gather")

    # creating a persistor which will save our data
    corona_virus_persistor = Persistor(RAW_DATA_FILE, CSV_DATA_FILE)
    # creating a scraper which will scrape our data to the persistor
    corona_virus_scraper = Scraper(corona_virus_persistor)
    # scraping the data to the designated persistor
    corona_virus_scraper.scrape()


# this function turns parser object to a csv file
def parser_to_csv(corona_virus_parser):
    # Here are the names of the parameters
    column_titles = ["TotalCases", "NewCases", "TotalDeaths", "NewDeaths",
                     "TotalRecovered", "ActiveCases", "SeriousCritical", "Total1M",
                     "Deaths1M", "TotalTests", "Tests1M", "Population", "Mainland"]
    # adding as a first row for the csv file
    add_row(column_titles)

    # add to csv row by row the next data
    for next_data in corona_virus_parser:
        add_row(next_data)

# this function parses raw data to the csv file
def parse():
    # parse gathered data and save as csv
    logger.info("parse")

    # this persistor helps us to read from raw data file and write to csv data file
    corona_virus_persistor = Persistor(RAW_DATA_FILE, CSV_DATA_FILE)

    # this is our raw data as a string
    corona_virus_data = corona_virus_persistor.read_raw_data()

    corona_virus_persistor.create_csv()
    # creating a parser object which will help us to turn raw data to csv
    corona_virus_parser = Parser(corona_virus_data)

    # Turning parser to csv file
    parser_to_csv(corona_virus_parser)


# Here I displayed 8 countries with the largest amounts of total cases of corona-virus
def stats():
    logger.info("stats")

    df = pd.read_csv(CSV_DATA_FILE)
    df = df.sort_values(by=['TotalDeaths'], ascending=[False])

    df.head(8).plot.pie(y='TotalDeaths', figsize=(5, 5))
    plt.show()


if __name__ == '__main__':
    logger.info("Work started")

    if sys.argv[1] == 'gather':
        gather()
    elif sys.argv[1] == 'parse':
        parse()
    elif sys.argv[1] == 'stats':
        stats()

    logger.info("work ended")

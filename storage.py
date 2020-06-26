from abc import ABC
from contextlib import contextmanager


class Persistor(ABC):

    def __init__(self, rawDataFile, csvDataFile):
        self.rawDataFile = rawDataFile
        self.csvDataFile = csvDataFile

    # this method provides the tool for using context manager
    @contextmanager
    def get_session(self, file_name, mode):
        try:
            session = open(file_name, mode, encoding="utf-8")
            yield session
        finally:
            session.close()

    # returns csv file name
    def csv_file_name(self):
        return self.csvDataFile

    # returns txt file name
    def txt_file_name(self):
        return self.rawDataFile

    # reads raw data
    def read_raw_data(self):
        with self.get_session(self.txt_file_name(), "r") as f:
            coronaVirusData = f.read()
        return coronaVirusData

    # saves raw data
    def save_raw_data(self, data):
        with self.get_session(self.txt_file_name(), "w") as f:
            f.write(data)

    # this function simply creates a csv file if it does not exist
    # if it exists it will simply remove it's content
    @contextmanager
    def create_csv(self):
        try:
            session = open(self.csv_file_name(), "w", encoding="utf-8")
        finally:
            session.close()

    # this function helps to read the csv file
    def read_csv(self):
        with self.get_session(self.csv_file_name(), "r") as f:
            data = f.read()
        return data

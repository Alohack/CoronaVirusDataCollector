from abc import ABC, abstractmethod


class Persistor(ABC):

    def __init__(self, rawDataFile, csvDataFile):
        self.rawDataFile = rawDataFile
        self.csvDataFile = csvDataFile

    def csv_file_name(self):
        return self.csvDataFile

    def txt_file_name(self):
        return self.rawDataFile

    def read_raw_data(self):
        f = open(self.txt_file_name(), "r", encoding="utf-8")
        coronaVirusData = f.read()
        f.close()
        return coronaVirusData

    def save_raw_data(self, data):
        f = open(self.txt_file_name(), "w", encoding="utf-8")
        f.write(data)
        f.close()

    def create_csv(self):
        f = open(self.csv_file_name(), 'w', encoding="utf-8")
        f.close()

    def read_csv(self):
        f = open(self.csv_file_name(), 'r', encoding="utf-8")
        data = f.read()
        f.close()
        return data

from abc import ABC, abstractmethod

class Persistor(ABC):

    def __init__(self, fileName):
        self.fileName = fileName

    def csv_file_name(self):
        return self.fileName + ".csv"

    def txt_file_name(self):
        return self.fileName + ".txt"

    def read_raw_data(self):
        f = open(self.txt_file_name(), "r", encoding="utf-8")
        coronaVirusData = f.read()
        f.close()
        return coronaVirusData

    def save_raw_data(self, data):
        f = open(self.txt_file_name(), "w", encoding="utf-8")
        f.write(data)
        f.close()

    def save_csv(self, data):
        f = open(self.csv_file_name(), 'w', encoding="utf-8")
        f.write(data)
        f.close()

    def read_csv(self):
        f = open(self.csv_file_name(), 'r', encoding="utf-8")
        data = f.read()
        f.close()
        return data


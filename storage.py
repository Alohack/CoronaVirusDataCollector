from abc import ABC, abstractmethod

class Persistor(ABC):

    def __init__(self):
        self.fileName = "CovidData"

    def read_raw_data(self):
        f = open(self.fileName + ".txt", "r", encoding="utf-8")
        coronaVirusData = f.read()
        f.close()
        return coronaVirusData

    def save_raw_data(self, data):
        f = open(self.fileName + ".txt", "w", encoding="utf-8")
        f.write(data)
        f.close()

    def save_csv(self, data):
        f = open(self.fileName + ".csv", 'w', encoding="utf-8")
        f.write(data)
        f.close()

    def read_csv(self):
        f = open(self.fileName + ".csv", 'r', encoding="utf-8")
        data = f.read()
        f.close()
        return data


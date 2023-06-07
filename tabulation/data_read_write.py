# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd


class TabulationProcess:
    def __int__(self, file):
        self.file = file

    def tabul_dataframe(self):
        if '.csv' in self.file:
            data = pd.read_csv(self.file)
        elif '.xls' or '.xlsx' or '.xlsm' in self.file:
            data = pd.read_excel(self.file)
        return data

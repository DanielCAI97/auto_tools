# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd


class TableReadWrite:
    def __int__(self, file):
        self.file = file

    # read files of distinctive extensions and turn the files into panda data frame
    def file_to_dataframe(self):
        if '.csv' in self.file:  # read csv files
            data = pd.read_csv(self.file)
        elif '.xls' or '.xlsx' or '.xlsm' or '.xlt' in self.file:  # read excel files
            data = pd.read_excel(self.file)
        return data




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

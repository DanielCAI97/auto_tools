import os
from colorama import Fore
import pandas as pd
import shutil
import pathlib
import numpy as np
from check_os import judge_os
from tqdm import tqdm, trange
import time

class FileProcess:
    def __init__(self, orig_files, output_files):
        self.orig_files = orig_files
        self.output_files = output_files
        if judge_os.get_platform() == 'Windows':
            self.delimiter = '\\'
        elif judge_os.get_platform() == 'OS X' or judge_os.get_platform() == 'Linux':
            self.delimiter = '/'
        # self.trg_dir = trg_dir
        # self.exist_files = []  # create a list to contain the existing files in the specific directory

    @classmethod
    def iter_dir(cls, trg_dir):  # to validate the existence of the files
        cls.exist_files = []
        for orig_file in os.listdir(trg_dir):
            if '.' in orig_file:
                cls.exist_files.append(orig_file)
        return cls.exist_files

    def chg_dir(self, trg_dir):
        table = dict(zip(self.orig_files, self.output_files))  # convert 2 lists into 1 dictionary
        for (k, v) in tqdm(table.items()):  # i:index, k:key, v:value
            if k in self.orig_files:
                shutil.move(trg_dir + self.delimiter + k, v)  # move files to dir
                time.sleep(1)
                # tqdm.write(str(k, v))




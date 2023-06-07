import os
from sys import platform

class FileProcess:
    def __int__(self, file_conven, orig_dir, output_dir):
        self.file_conven = file_conven
        self.orig_dir = orig_dir
        self.output_file = output_dir

    def chg_dir(self):
        with os.scandir(self.orig_dir) as entries:
            for entry in entries:
                


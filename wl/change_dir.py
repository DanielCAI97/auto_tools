# //                   _ooOoo_
# //                  o8888888o
# //                  88" . "88
# //                  (| -_- |)
# //                  O\  =  /O
# //               ____/`---'\____
# //             .'  \\|     |//  `.
# //            /  \\|||  :  |||//  \
# //           /  _||||| -:- |||||-  \
# //           |   | \\\  -  /// |   |
# //           | \_|  ''\---/''  |   |
# //           \  .-\__  `-`  ___/-. /
# //         ___`. .'  /--.--\  `. . __
# //      ."" '<  `.___\_<|>_/___.'  >'"".
# //     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
# //     \  \ `-.   \_ __\ /__ _/   .-` /  /
# //======`-.____`-.___\_____/___.-`____.-'======
# //                   `=---='
# //
# //^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# //          Author            Daniel
# //           Email      danielcaiyongjie@gmai.com
# //         buddha Bless        Never Crash
import pandas as pd
from tabulation import data_read_write as drw
from work_with_files import files_chg_dirs as fc
import os
from colorama import Fore
from check_os import judge_os


if __name__ == '__main__':
    trg_dir = input("Please input where the files store at this moment:")

    ##---- Specify distinctive delimiters by the OS ----##
    if judge_os.get_platform() == 'Windows':
        delimiter = '\\'
    elif judge_os.get_platform() == 'OS X' or judge_os.get_platform() == 'Linux':
        delimiter = '/'
    #----------------------end---------------------------#

    files = fc.FileProcess.iter_dir(trg_dir)
    table = ""
    for file in files:
        if file.endswith('.xls') or file.endswith('.xlsx') or file.endswith('.xlsm') or file.endswith('.xlt') or file.endswith('.csv'):
            table = file
    if table is None:
        print(Fore.RED + "Missing the tabulation file" + Fore.RESET)
    else:
        excel = drw.TableReadWrite(trg_dir + '/' + table).file_to_dataframe()
        files = list(excel.iloc[:, 0])
        paths = list(excel.iloc[:, 1])
        process_file = fc.FileProcess(files, paths).chg_dir(trg_dir)





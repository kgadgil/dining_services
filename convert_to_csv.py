import pandas as pd
import sys, os

origin=os.getcwd()
os.chdir("data/Dining data Virginia Tech/Atomic Pizza/2014-2015/April 2015")
xls_file= "04-01-15.3"
csv_file = xls_file.replace(".xls",".csv")
data_xls = pd.read_excel(xls_file, 'Sheet0', index_col=None)
data_xls.to_csv(csv_file, encoding='utf-8')

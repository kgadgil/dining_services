import pandas as pd
import sys
xls_file= sys.argv[1]
csv_file = xls_file.replace(".xls",".csv")
data_xls = pd.read_excel(xls_file, 'Sheet0', index_col=None)
data_xls.to_csv(csv_file, encoding='utf-8')

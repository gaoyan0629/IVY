import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import sys
import getpass
# user = getpass.getuser()
# passwd = getpass.getpass('Please input TD passwd: ')
# conn = 'teradata://{}:{}@10.89.140.97'.format(user,passwd)
# td = create_engine(conn)
td = create_engine('teradata://datamodeller:datamodeller@10.89.140.97')













database = \
{1:"BIP_TDB",
2:"BIP_ADM_TDB",
3:"BIP_XTR_TDB",
4:"BIP_XTR_VTDB",
5:"BIP_SMBB_VTDB",
6:"BIP_ADM_TDB",
7:"BIP_XTR_TDB",
8:"BIP_XTR_VTDB",
9:"BIP_SMBB_VTDB",
10:"BIPHK_TDB",
11:"BIPHK_ADM_TDB",
12:"BIPHK_VTDB",
13:"BIPHK_ADM_VTDB",
14:"BIPIN_TDB",
15:"BIPIN_ADM_TDB",
16:"BIPIN_VTDB",
17:"BIPIN_ADM_VTDB",
18:"BIPID_TDB",
19:"BIPID_ADM_TDB",
20:"BIPID_VTDB",
21:"BIPID_ADM_VTDB",
22:"BIP_VTDB"}

#===================================================
# customization area start

db = database[22]

sql = """SELECT * FROM DBC.TABLES WHERE DATABASENAME = '{}'""".format(db)

sql = """SELECT TOP 2000 * FROM bip_vtdb.V0521_FIN_EVENT""" 

table = pd.read_sql(sql,td)
print 'Query completed'

# customization area end
#===================================================

import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import sys
# run this script using %run sys[argv[0]] from ipython
#td = create_engine('teradata://gaoyangao:~WeiFang123@10.89.140.97')
td = create_engine('teradata://datamodeller:datamodeller@10.92.139.28')













#===================================================
# customization area start
sql = {}
sql['V0177'] = """\
        select * from \
        bip_vtdb.v0177_data_source_type
        """
sql[1] = ''

if len(sys.argv) < 2:
    qry = sql['V0177']
else:
    qry = sql[sys.argv[1].upper()]

table = pd.read_sql(qry,td)
print "Query completed"

# customization area end
#=======================================
